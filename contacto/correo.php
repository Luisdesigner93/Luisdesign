<?php
// Envío de correo por SMTP autenticado (Titan), compartido por el formulario (guardar.php) y la agenda (agenda.php).
// Solo define funciones: si alguien lo abre directo desde el navegador, responde 404.
declare(strict_types=1);

if (realpath($_SERVER['SCRIPT_FILENAME'] ?? '') === __FILE__) {
    http_response_code(404);
    exit;
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
            . 'Subject: ' . mb_encode_mimeheader($asunto, 'UTF-8', 'B') . "\r\n"
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
