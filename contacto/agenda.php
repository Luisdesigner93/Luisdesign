<?php
// Agenda del popup de contacto, conectada a Google Calendar.
// GET: devuelve las horas libres agrupadas por semana. POST: valida, reserva y crea el evento con Google Meet.
// El navegador solo habla con este archivo: no carga nada de Google y no usa cookies ni sesiones.
// La configuración real vive fuera de public_html (ver tools/config/luisdesign-config.example.php y tools/agenda/README.md).
declare(strict_types=1);

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

const LIMITE_POR_IP = 3;           // reservas permitidas por IP dentro de la ventana
const VENTANA_MINUTOS = 10;
const LIMITE_FUTURAS_POR_CORREO = 2;
const CACHE_SEGUNDOS = 60;         // evita consultar Google en cada apertura del popup
const VERSION_CONSENTIMIENTO = '2026-11-agenda';

function salir(int $codigo, array $datos): never
{
    http_response_code($codigo);
    echo json_encode($datos, JSON_UNESCAPED_UNICODE);
    exit;
}

function error_json(int $codigo, string $es, string $en, bool $ingles, array $extra = []): never
{
    salir($codigo, ['ok' => false, 'mensaje' => $ingles ? $en : $es] + $extra);
}

function limpiar(string $texto, bool $conSaltos = false): string
{
    $patron = $conSaltos ? '/[^\P{C}\n\r\t]/u' : '/\p{C}/u';
    return trim((string) preg_replace($patron, ' ', $texto));
}

function dirCache(): string
{
    $dir = dirname(__DIR__, 2) . '/.luisdesign-agenda';
    if (!is_dir($dir) && !mkdir($dir, 0700) && !is_dir($dir)) {
        throw new RuntimeException('cache');
    }
    return $dir;
}

function leerCache(string $nombre): ?array
{
    $ruta = dirCache() . '/' . $nombre . '.json';
    if (!is_file($ruta)) {
        return null;
    }
    $datos = json_decode((string) file_get_contents($ruta), true);
    return is_array($datos) && ($datos['vence'] ?? 0) > time() ? $datos['valor'] : null;
}

function guardarCache(string $nombre, array $valor, int $segundos): void
{
    $ruta = dirCache() . '/' . $nombre . '.json';
    file_put_contents($ruta, json_encode(['vence' => time() + $segundos, 'valor' => $valor]), LOCK_EX);
    chmod($ruta, 0600);
}

// Petición HTTP. Los errores solo indican la etapa: nunca incluyen claves ni datos de personas.
function pedir(string $url, array $cabeceras, string $cuerpo, string $etapa): array
{
    $curl = curl_init($url);
    curl_setopt_array($curl, [
        CURLOPT_POST => true,
        CURLOPT_POSTFIELDS => $cuerpo,
        CURLOPT_HTTPHEADER => $cabeceras,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_CONNECTTIMEOUT => 5,
        CURLOPT_TIMEOUT => 12,
    ]);
    $respuesta = curl_exec($curl);
    $estado = (int) curl_getinfo($curl, CURLINFO_RESPONSE_CODE);
    if ($respuesta === false || $estado < 200 || $estado >= 300) {
        throw new RuntimeException($etapa . ': respuesta ' . $estado);
    }
    $datos = json_decode((string) $respuesta, true);
    if (!is_array($datos)) {
        throw new RuntimeException($etapa . ': respuesta ilegible');
    }
    return $datos;
}

function tokenGoogle(array $agenda): string
{
    $guardado = leerCache('token');
    if ($guardado !== null) {
        return $guardado['access_token'];
    }
    $datos = pedir($agenda['google_token_url'] ?? 'https://oauth2.googleapis.com/token', ['Content-Type: application/x-www-form-urlencoded'], http_build_query([
        'client_id' => $agenda['cliente_id'],
        'client_secret' => $agenda['cliente_secreto'],
        'refresh_token' => $agenda['refresh_token'],
        'grant_type' => 'refresh_token',
    ]), 'token');
    if (empty($datos['access_token'])) {
        throw new RuntimeException('token: sin acceso');
    }
    guardarCache('token', ['access_token' => $datos['access_token']], max(60, (int) ($datos['expires_in'] ?? 3600) - 120));
    return $datos['access_token'];
}

function google(array $agenda, string $ruta, array $cuerpo, string $etapa): array
{
    $base = rtrim($agenda['google_api_url'] ?? 'https://www.googleapis.com', '/');
    return pedir($base . $ruta, ['Authorization: Bearer ' . tokenGoogle($agenda), 'Content-Type: application/json'], json_encode($cuerpo, JSON_UNESCAPED_UNICODE), $etapa);
}

// Intervalos ocupados [inicio, fin] en timestamp, de todos los calendarios configurados
function ocupados(array $agenda, DateTimeImmutable $desde, DateTimeImmutable $hasta): array
{
    $calendarios = $agenda['calendarios_ocupados'] ?? [$agenda['calendario'] ?? 'primary'];
    $datos = google($agenda, '/calendar/v3/freeBusy', [
        'timeMin' => $desde->format(DATE_RFC3339),
        'timeMax' => $hasta->format(DATE_RFC3339),
        'timeZone' => $agenda['zona'],
        'items' => array_map(fn (string $id): array => ['id' => $id], $calendarios),
    ], 'disponibilidad');
    $intervalos = [];
    foreach ($calendarios as $id) {
        $calendario = $datos['calendars'][$id] ?? null;
        // Si Google no pudo leer un calendario no se ofrecen horas: podrían estar ocupadas
        if ($calendario === null || !empty($calendario['errors'])) {
            throw new RuntimeException('disponibilidad: calendario no disponible');
        }
        foreach ($calendario['busy'] ?? [] as $tramo) {
            $intervalos[] = [strtotime($tramo['start']), strtotime($tramo['end'])];
        }
    }
    return $intervalos;
}

// Todas las horas posibles según los horarios, sin mirar aún el calendario
function horasPosibles(array $agenda, DateTimeImmutable $ahora): array
{
    // Anticipación en días de calendario: hoy lunes, la primera fecha posible es el miércoles
    $minimo = $ahora->setTime(0, 0)->modify('+' . (int) $agenda['anticipacion_dias'] . ' days');
    $lunes = $ahora->setTime(0, 0)->modify('monday this week');
    $bloqueados = $agenda['dias_bloqueados'] ?? [];
    $semanas = [];
    for ($s = 0; $s < (int) $agenda['semanas']; $s++) {
        $inicioSemana = $lunes->modify('+' . ($s * 7) . ' days');
        $dias = [];
        for ($d = 0; $d < 7; $d++) {
            $dia = $inicioSemana->modify('+' . $d . ' days');
            if (!in_array((int) $dia->format('N'), $agenda['dias'], true)) {
                continue;
            }
            $horas = [];
            if (!in_array($dia->format('Y-m-d'), $bloqueados, true)) {
                foreach ($agenda['horas'] as $hora) {
                    [$h, $m] = array_map('intval', explode(':', $hora));
                    $inicio = $dia->setTime($h, $m);
                    if ($inicio >= $minimo) {
                        $horas[] = $inicio;
                    }
                }
            }
            $dias[] = ['fecha' => $dia, 'horas' => $horas];
        }
        $semanas[] = ['lunes' => $inicioSemana, 'dias' => $dias];
    }
    return $semanas;
}

function estaLibre(DateTimeImmutable $inicio, int $duracion, array $intervalos): bool
{
    $a = $inicio->getTimestamp();
    $b = $a + $duracion * 60;
    foreach ($intervalos as [$desde, $hasta]) {
        if ($a < $hasta && $b > $desde) {
            return false;
        }
    }
    return true;
}

function limites(array $semanas): array
{
    $ultima = end($semanas);
    return [$semanas[0]['lunes'], $ultima['lunes']->modify('+7 days')];
}

// Aviso por correo a Luis con los datos de la reunión recién agendada (asunto y cuerpo en español)
function avisoReserva(string $nombre, string $correo, string $mensaje, DateTimeImmutable $inicio, int $duracion, bool $ingles, array $evento): array
{
    $dias = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado'];
    $meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];
    $fecha = $dias[(int) $inicio->format('w')] . ' ' . $inicio->format('j') . ' de ' . $meses[(int) $inicio->format('n') - 1] . ' de ' . $inicio->format('Y');
    $asunto = 'Nueva reunión agendada: ' . $nombre . ' · ' . $inicio->format('d/m H:i');
    $cuerpo = "Se agendó una reunión desde luisdesign.cl.\n\n"
        . "Nombre: {$nombre}\n"
        . "Correo: {$correo}\n"
        . "Fecha: {$fecha}\n"
        . 'Hora: ' . $inicio->format('H:i') . ' (' . $inicio->getTimezone()->getName() . ")\n"
        . "Duración: {$duracion} minutos\n"
        . 'Idioma del sitio: ' . ($ingles ? 'inglés' : 'español') . "\n"
        . (!empty($evento['hangoutLink']) ? 'Google Meet: ' . $evento['hangoutLink'] . "\n" : '')
        . (!empty($evento['htmlLink']) ? 'Evento en Google Calendar: ' . $evento['htmlLink'] . "\n" : '')
        . "\nMensaje:\n" . ($mensaje !== '' ? $mensaje : '(sin mensaje)') . "\n";
    return [$asunto, $cuerpo];
}

function configurada(array $config): ?array
{
    $agenda = $config['agenda'] ?? null;
    if (!is_array($agenda) || empty($agenda['activa']) || !function_exists('curl_init')) {
        return null;
    }
    foreach (['cliente_id', 'cliente_secreto', 'refresh_token', 'zona', 'horas', 'dias'] as $clave) {
        if (empty($agenda[$clave])) {
            return null;
        }
    }
    return $agenda + ['duracion' => 20, 'anticipacion_dias' => 2, 'semanas' => 4, 'calendario' => 'primary'];
}

$ingles = ($_REQUEST['idioma'] ?? '') === 'en';
$metodo = $_SERVER['REQUEST_METHOD'] ?? '';
if ($metodo !== 'GET' && $metodo !== 'POST') {
    error_json(405, 'Método no permitido.', 'Method not allowed.', $ingles);
}

// Sin configuración la agenda se declara no disponible y el popup conserva el formulario
$rutaConfig = dirname(__DIR__, 2) . '/luisdesign-config.php';
$config = is_file($rutaConfig) ? require $rutaConfig : [];
$agenda = configurada($config);
if ($agenda === null) {
    if ($metodo === 'GET') {
        salir(200, ['ok' => true, 'disponible' => false]);
    }
    error_json(503, 'La agenda no está disponible. Escríbeme por el formulario.', 'Scheduling is unavailable. Please use the form.', $ingles);
}

try {
    $zona = new DateTimeZone($agenda['zona']);
    $ahora = new DateTimeImmutable('now', $zona);
    $semanas = horasPosibles($agenda, $ahora);
    [$desde, $hasta] = limites($semanas);

    if ($metodo === 'GET') {
        $libres = leerCache('disponibilidad');
        if ($libres === null) {
            $intervalos = ocupados($agenda, $ahora, $hasta);
            $libres = array_map(fn (array $semana): array => [
                'lunes' => $semana['lunes']->format('Y-m-d'),
                'dias' => array_map(fn (array $dia): array => [
                    'fecha' => $dia['fecha']->format('Y-m-d'),
                    'horas' => array_values(array_map(
                        fn (DateTimeImmutable $h): array => ['inicio' => $h->format(DATE_RFC3339), 'hora' => $h->format('H:i')],
                        array_filter($dia['horas'], fn (DateTimeImmutable $h): bool => estaLibre($h, (int) $agenda['duracion'], $intervalos))
                    )),
                ], $semana['dias']),
            ], $semanas);
            guardarCache('disponibilidad', $libres, CACHE_SEGUNDOS);
        }
        salir(200, ['ok' => true, 'disponible' => true, 'duracion' => (int) $agenda['duracion'], 'semanas' => $libres]);
    }

    // POST: origen, campo trampa y datos
    $origen = $_SERVER['HTTP_ORIGIN'] ?? '';
    if ($origen !== '' && $origen !== ($config['origen'] ?? '')) {
        error_json(403, 'Solicitud no permitida.', 'Request not allowed.', $ingles);
    }
    if (($_POST['web'] ?? '') !== '') {
        salir(200, ['ok' => true, 'mensaje' => $ingles ? 'Meeting scheduled.' : 'Reunión agendada.']);
    }

    $nombre = limpiar((string) ($_POST['nombre'] ?? ''));
    $correo = limpiar((string) ($_POST['correo'] ?? ''));
    $mensaje = limpiar((string) ($_POST['mensaje'] ?? ''), true);
    $textoInicio = (string) ($_POST['inicio'] ?? '');

    if (mb_strlen($nombre) < 2 || mb_strlen($nombre) > 100) {
        error_json(422, 'Revisa tu nombre: entre 2 y 100 caracteres.', 'Check your name: 2 to 100 characters.', $ingles);
    }
    if (mb_strlen($correo) > 150 || filter_var($correo, FILTER_VALIDATE_EMAIL) === false) {
        error_json(422, 'Revisa tu correo: debe tener un formato válido.', 'Check your email: it must be valid.', $ingles);
    }
    if (mb_strlen($mensaje) > 2000) {
        error_json(422, 'Tu mensaje puede tener hasta 2000 caracteres.', 'Your message can have up to 2000 characters.', $ingles);
    }
    if (($_POST['consentimiento'] ?? '') !== '1') {
        error_json(422, 'Necesito que aceptes el uso de tus datos para agendar.', 'Please accept the use of your data to schedule.', $ingles);
    }

    // La hora debe ser una de las ofrecidas: no se confía en lo que envía el navegador
    $inicio = DateTimeImmutable::createFromFormat(DATE_RFC3339, $textoInicio);
    $valida = false;
    if ($inicio !== false) {
        $inicio = $inicio->setTimezone($zona);
        foreach ($semanas as $semana) {
            foreach ($semana['dias'] as $dia) {
                foreach ($dia['horas'] as $hora) {
                    $valida = $valida || $hora->getTimestamp() === $inicio->getTimestamp();
                }
            }
        }
    }
    $tomada = ['actualizar' => true];
    if (!$valida) {
        error_json(409, 'Ese horario ya no está disponible. Elige otro.', 'That time is no longer available. Pick another.', $ingles, $tomada);
    }

    $pdo = new PDO($config['db_dsn'], $config['db_usuario'] ?? null, $config['db_clave'] ?? null, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_EMULATE_PREPARES => false,
    ]);
    $utc = new DateTimeZone('UTC');
    $ahoraUtc = $ahora->setTimezone($utc)->format('Y-m-d H:i:s');
    $inicioUtc = $inicio->setTimezone($utc)->format('Y-m-d H:i:s');

    $ipHash = hash_hmac('sha256', (string) ($_SERVER['REMOTE_ADDR'] ?? ''), $config['secreto']);
    $consulta = $pdo->prepare('SELECT COUNT(*) FROM reservas WHERE ip_hash = ? AND creado_en >= ?');
    $consulta->execute([$ipHash, $ahora->modify('-' . VENTANA_MINUTOS . ' minutes')->setTimezone($utc)->format('Y-m-d H:i:s')]);
    $recientes = (int) $consulta->fetchColumn();
    $consulta->closeCursor();
    if ($recientes >= LIMITE_POR_IP) {
        error_json(429, 'Recibí varias reservas desde tu conexión. Inténtalo en unos minutos.', 'Too many bookings from your connection. Try again in a few minutes.', $ingles);
    }
    $consulta = $pdo->prepare('SELECT COUNT(*) FROM reservas WHERE correo = ? AND inicio >= ?');
    $consulta->execute([mb_strtolower($correo), $ahoraUtc]);
    $futuras = (int) $consulta->fetchColumn();
    $consulta->closeCursor();
    if ($futuras >= LIMITE_FUTURAS_POR_CORREO) {
        error_json(429, 'Ya tienes reuniones agendadas con este correo. Revisa tu invitación.', 'You already have meetings booked with this email. Check your invitation.', $ingles);
    }

    // Una reserva a la vez: entre comprobar la hora y crear el evento nadie más puede tomarla
    $candado = fopen(dirCache() . '/reserva.lock', 'c');
    $conCandado = false;
    for ($intento = 0; $candado !== false && !$conCandado && $intento < 40; $intento++) {
        $conCandado = flock($candado, LOCK_EX | LOCK_NB);
        if (!$conCandado) {
            usleep(250000);
        }
    }
    if (!$conCandado) {
        throw new RuntimeException('candado');
    }
    $fin = $inicio->modify('+' . (int) $agenda['duracion'] . ' minutes');
    if (!estaLibre($inicio, (int) $agenda['duracion'], ocupados($agenda, $inicio->modify('-1 minute'), $fin->modify('+1 minute')))) {
        @unlink(dirCache() . '/disponibilidad.json');
        error_json(409, 'Ese horario ya no está disponible. Elige otro.', 'That time is no longer available. Pick another.', $ingles, $tomada);
    }

    $insertar = $pdo->prepare('INSERT INTO reservas (creado_en, inicio, nombre, correo, mensaje, idioma, ip_hash, consentimiento_version) VALUES (?, ?, ?, ?, ?, ?, ?, ?)');
    $insertar->execute([$ahoraUtc, $inicioUtc, $nombre, mb_strtolower($correo), $mensaje, $ingles ? 'en' : 'es', $ipHash, VERSION_CONSENTIMIENTO]);
    $idReserva = (int) $pdo->lastInsertId();

    try {
        $descripcion = ($ingles ? 'Booked from luisdesign.cl' : 'Agendada desde luisdesign.cl') . ($mensaje !== '' ? "\n\n" . $mensaje : '');
        $evento = google($agenda, '/calendar/v3/calendars/' . rawurlencode((string) $agenda['calendario']) . '/events?conferenceDataVersion=1&sendUpdates=all', [
            'summary' => ($ingles ? 'Meeting with Luis Vicencio · ' : 'Reunión con Luis Vicencio · ') . $nombre,
            'description' => $descripcion,
            'start' => ['dateTime' => $inicio->format(DATE_RFC3339), 'timeZone' => $agenda['zona']],
            'end' => ['dateTime' => $fin->format(DATE_RFC3339), 'timeZone' => $agenda['zona']],
            'attendees' => [['email' => $correo, 'displayName' => $nombre]],
            'guestsCanInviteOthers' => false,
            'guestsCanModify' => false,
            'conferenceData' => ['createRequest' => ['requestId' => bin2hex(random_bytes(12)), 'conferenceSolutionKey' => ['type' => 'hangoutsMeet']]],
        ], 'evento');
    } catch (Throwable $falla) {
        $pdo->prepare('DELETE FROM reservas WHERE id = ?')->execute([$idReserva]);
        throw $falla;
    }

    $pdo->prepare('UPDATE reservas SET google_evento_id = ? WHERE id = ?')->execute([(string) ($evento['id'] ?? ''), $idReserva]);
    @unlink(dirCache() . '/disponibilidad.json');
    flock($candado, LOCK_UN);

    // Aviso por correo a Luis (el mismo destino que las copias del formulario). Si falla, la reunión ya quedó agendada.
    if (($config['copia_email'] ?? '') !== '') {
        try {
            require_once __DIR__ . '/correo.php';
            [$asunto, $cuerpo] = avisoReserva($nombre, $correo, $mensaje, $inicio, (int) $agenda['duracion'], $ingles, $evento);
            enviarCopiaSmtp($config['smtp'] ?? [], $config['remitente'], $config['copia_email'], $asunto, $cuerpo, $correo);
        } catch (Throwable $falla) {
            error_log('agenda: no se pudo enviar el aviso por correo (' . $falla->getMessage() . ')');
        }
    }

    salir(200, ['ok' => true, 'mensaje' => $ingles ? 'Meeting scheduled.' : 'Reunión agendada.']);
} catch (Throwable $error) {
    error_log('agenda: ' . $error->getMessage());
    if ($metodo === 'GET') {
        salir(200, ['ok' => true, 'disponible' => false]);
    }
    error_json(503, 'No pude agendar en este momento. Escríbeme por el formulario.', 'I could not schedule this right now. Please use the form.', $ingles, ['usarFormulario' => true]);
}
