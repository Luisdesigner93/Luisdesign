<?php
// Autoriza una vez tu Google Calendar y muestra el refresh token para la configuración del servidor.
// Se ejecuta en tu computador: php tools/agenda/autorizar-google.php
declare(strict_types=1);

if (PHP_SAPI !== 'cli') {
    exit("Solo se ejecuta desde la terminal.\n");
}

const PUERTO = 8765;
$redireccion = 'http://127.0.0.1:' . PUERTO . '/';
$clienteId = trim((string) readline('ID de cliente: '));
$clienteSecreto = trim((string) readline('Secreto de cliente: '));
if ($clienteId === '' || $clienteSecreto === '') {
    exit("Faltan datos.\n");
}

$estado = bin2hex(random_bytes(16));
$servidor = stream_socket_server('tcp://127.0.0.1:' . PUERTO, $errno, $errstr);
if ($servidor === false) {
    exit('No pude abrir el puerto ' . PUERTO . ".\n");
}

echo "\nAbre este enlace, entra con la cuenta del calendario y autoriza:\n\n";
echo 'https://accounts.google.com/o/oauth2/v2/auth?' . http_build_query([
    'client_id' => $clienteId,
    'redirect_uri' => $redireccion,
    'response_type' => 'code',
    'scope' => 'https://www.googleapis.com/auth/calendar.events https://www.googleapis.com/auth/calendar.freebusy',
    'access_type' => 'offline',
    'prompt' => 'consent',
    'state' => $estado,
]) . "\n\nEsperando la autorización…\n";

$conexion = stream_socket_accept($servidor, 300);
if ($conexion === false) {
    exit("Se acabó el tiempo de espera.\n");
}
$linea = (string) fgets($conexion);
preg_match('#^GET (\S+)#', $linea, $coincide);
parse_str((string) parse_url($coincide[1] ?? '', PHP_URL_QUERY), $datos);
fwrite($conexion, "HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=utf-8\r\nConnection: close\r\n\r\nListo. Vuelve a la terminal.");
fclose($conexion);

if (!hash_equals($estado, (string) ($datos['state'] ?? '')) || empty($datos['code'])) {
    exit("La autorización no se completó.\n");
}

$curl = curl_init('https://oauth2.googleapis.com/token');
curl_setopt_array($curl, [
    CURLOPT_POST => true,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POSTFIELDS => http_build_query([
        'code' => $datos['code'],
        'client_id' => $clienteId,
        'client_secret' => $clienteSecreto,
        'redirect_uri' => $redireccion,
        'grant_type' => 'authorization_code',
    ]),
]);
$token = json_decode((string) curl_exec($curl), true);
if (empty($token['refresh_token'])) {
    exit("Google no entregó el refresh token. Revisa el cliente OAuth e inténtalo de nuevo.\n");
}
echo "\nCopia este valor en 'refresh_token' de luisdesign-config.php. No lo compartas:\n\n" . $token['refresh_token'] . "\n";
