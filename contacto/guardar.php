<?php
// Formulario de contacto de la home (Conversemos). Recibe un POST, valida todo en el servidor, guarda el mensaje
// en MySQL y, si está configurado, envía una copia por correo. No usa cookies ni sesiones.
// La configuración real vive fuera de public_html (ver tools/config/luisdesign-config.example.php).
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

const LIMITE_POR_IP = 5;          // mensajes permitidos por IP dentro de la ventana
const VENTANA_MINUTOS = 10;
const VERSION_CONSENTIMIENTO = '2026-10';

function responder(int $codigo, string $mensaje): never
{
    http_response_code($codigo);
    echo json_encode(['ok' => $codigo === 200, 'mensaje' => $mensaje], JSON_UNESCAPED_UNICODE);
    exit;
}

function limpiar(string $texto, bool $conSaltos = false): string
{
    $patron = $conSaltos ? '/[^\P{C}\n\r\t]/u' : '/\p{C}/u';
    return trim((string) preg_replace($patron, ' ', $texto));
}

function escribirLinea($socket, string $linea): void
{
    fwrite($socket, $linea . "\r\n");
}

// Lee la respuesta SMTP (incluidas las líneas multilínea) y verifica el código esperado.
function esperarRespuesta($socket, string $esperado, string $etapa): void
{
    do {
        $linea = fgets($socket, 515);
        if ($linea === false) {
            throw new RuntimeException($etapa . ': sin respuesta');
        }
    } while (isset($linea[3]) && $linea[3] === '-');

    if (!str_starts_with($linea, $esperado)) {
        throw new RuntimeException($etapa . ': respuesta inesperada');
    }
}

function comandoSmtp($socket, string $linea, string $esperado, string $etapa): void
{
    escribirLinea($socket, $linea);
    esperarRespuesta($socket, $esperado, $etapa);
}

// Envía la copia por SMTP autenticado (TLS directo, puerto 465) con PHP nativo.
// Los errores lanzan RuntimeException con solo la etapa fallida: nunca incluyen credenciales.
function enviarCopiaSmtp(array $smtp, string $remitente, string $destino, string $asunto, string $cuerpo, string $replyTo): void
{
    if (empty($smtp['host']) || empty($smtp['puerto']) || empty($smtp['usuario']) || empty($smtp['clave'])) {
        throw new RuntimeException('configuracion incompleta');
    }

    $socket = @stream_socket_client('ssl://' . $smtp['host'] . ':' . $smtp['puerto'], $errno, $errstr, 15);
    if ($socket === false) {
        throw new RuntimeException('conexion');
    }
    stream_set_timeout($socket, 15);

    try {
        esperarRespuesta($socket, '220', 'saludo');
        comandoSmtp($socket, 'EHLO ' . substr(strrchr($remitente, '@'), 1), '250', 'ehlo');
        comandoSmtp($socket, 'AUTH LOGIN', '334', 'auth');
        comandoSmtp($socket, base64_encode($smtp['usuario']), '334', 'usuario');
        comandoSmtp($socket, base64_encode($smtp['clave']), '235', 'clave');
        comandoSmtp($socket, 'MAIL FROM:<' . $remitente . '>', '250', 'remitente');
        comandoSmtp($socket, 'RCPT TO:<' . $destino . '>', '250', 'destinatario');
        comandoSmtp($socket, 'DATA', '354', 'data');

        // Normaliza saltos de línea y escapa las líneas que empiezan con punto (RFC 5321)
        $lineas = array_map(
            fn (string $linea): string => str_starts_with($linea, '.') ? '.' . $linea : $linea,
            explode("\n", str_replace(["\r\n", "\r"], "\n", $cuerpo))
        );
        $cabeceras = "From: {$remitente}\r\n"
            . "To: {$destino}\r\n"
            . "Reply-To: {$replyTo}\r\n"
            . "Subject: {$asunto}\r\n"
            . 'Date: ' . date('r') . "\r\n"
            . "MIME-Version: 1.0\r\n"
            . "Content-Type: text/plain; charset=UTF-8\r\n"
            . "\r\n";

        fwrite($socket, $cabeceras . implode("\r\n", $lineas) . "\r\n.\r\n");
        esperarRespuesta($socket, '250', 'fin');
    } finally {
        @fwrite($socket, "QUIT\r\n");
        fclose($socket);
    }
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    responder(405, 'Método no permitido.');
}

$rutaConfig = dirname(__DIR__, 2) . '/luisdesign-config.php';
if (!is_file($rutaConfig)) {
    error_log('contacto: falta el archivo de configuración fuera de public_html');
    responder(500, 'No pude guardar tu mensaje en este momento. Escríbeme a contacto@luisdesign.cl.');
}
$config = require $rutaConfig;

try {
    // 1) Origen: solo se aceptan envíos desde el propio sitio (sin cookies de por medio)
    $origen = $_SERVER['HTTP_ORIGIN'] ?? '';
    if ($origen !== '' && $origen !== $config['origen']) {
        responder(403, 'Solicitud no permitida.');
    }

    // 2) Campo trampa: los robots lo completan, las personas no lo ven
    if (($_POST['web'] ?? '') !== '') {
        responder(200, 'Gracias. Recibí tu mensaje.');
    }

    // 3) Validación de datos
    $nombre = limpiar((string) ($_POST['nombre'] ?? ''));
    $correo = limpiar((string) ($_POST['correo'] ?? ''));
    $mensaje = limpiar((string) ($_POST['mensaje'] ?? ''), true);

    if (mb_strlen($nombre) < 2 || mb_strlen($nombre) > 100) {
        responder(422, 'Revisa tu nombre: entre 2 y 100 caracteres.');
    }
    if (mb_strlen($correo) > 150 || filter_var($correo, FILTER_VALIDATE_EMAIL) === false) {
        responder(422, 'Revisa tu correo: debe tener un formato válido.');
    }
    if (mb_strlen($mensaje) < 10 || mb_strlen($mensaje) > 2000) {
        responder(422, 'Revisa tu mensaje: entre 10 y 2000 caracteres.');
    }
    if (($_POST['consentimiento'] ?? '') !== '1') {
        responder(422, 'Necesito que aceptes el uso de tus datos para responder tu mensaje.');
    }

    // 4) Conexión y límite de envíos por IP (guardada como hash, nunca en claro)
    $ipHash = hash_hmac('sha256', (string) ($_SERVER['REMOTE_ADDR'] ?? ''), $config['secreto']);
    $pdo = new PDO($config['db_dsn'], $config['db_usuario'], $config['db_clave'], [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_EMULATE_PREPARES => false,
    ]);

    $consulta = $pdo->prepare('SELECT COUNT(*) FROM consultas WHERE ip_hash = ? AND creado_en >= NOW() - INTERVAL ' . VENTANA_MINUTOS . ' MINUTE');
    $consulta->execute([$ipHash]);
    if ((int) $consulta->fetchColumn() >= LIMITE_POR_IP) {
        responder(429, 'Recibí varios mensajes desde tu conexión hace poco. Inténtalo de nuevo en unos minutos.');
    }

    // 5) Guardado
    $insertar = $pdo->prepare('INSERT INTO consultas (nombre, correo, mensaje, ip_hash, consentimiento_version) VALUES (?, ?, ?, ?, ?)');
    $insertar->execute([$nombre, $correo, $mensaje, $ipHash, VERSION_CONSENTIMIENTO]);

    // 6) Copia por correo (opcional, por SMTP de Titan). Si falla, el mensaje ya quedó guardado.
    if (($config['copia_email'] ?? '') !== '') {
        $cuerpo = "Nombre: {$nombre}\nCorreo: {$correo}\n\n{$mensaje}\n";
        try {
            enviarCopiaSmtp($config['smtp'] ?? [], $config['remitente'], $config['copia_email'], 'Nuevo contacto desde luisdesign.cl', $cuerpo, $correo);
        } catch (RuntimeException $error) {
            error_log('contacto: no se pudo enviar la copia por correo (' . $error->getMessage() . ')');
        }
    }

    responder(200, 'Gracias. Recibí tu mensaje y te respondo en 1 a 2 días hábiles.');
} catch (Throwable $error) {
    error_log('contacto: ' . $error->getMessage());
    responder(500, 'No pude guardar tu mensaje en este momento. Escríbeme a contacto@luisdesign.cl.');
}
