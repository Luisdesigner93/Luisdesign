<?php
// Contador de la prueba A/B de inicio (js/ab.js). Guarda solo totales por día, versión y evento:
// no recibe ni guarda IP, nombres, correos ni identificadores de personas.
declare(strict_types=1);

header('Cache-Control: no-store');

function terminar(int $codigo): never
{
    http_response_code($codigo);
    exit;
}

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') {
    terminar(405);
}

$variante = (string) ($_POST['variante'] ?? '');
$evento = (string) ($_POST['evento'] ?? '');
if (!in_array($variante, ['a', 'b'], true) || !in_array($evento, ['visita', 'conversemos'], true)) {
    terminar(422);
}

$rutaConfig = dirname(__DIR__, 2) . '/luisdesign-config.php';
if (!is_file($rutaConfig)) {
    terminar(204);
}
$config = require $rutaConfig;

$origen = $_SERVER['HTTP_ORIGIN'] ?? '';
if ($origen !== '' && $origen !== ($config['origen'] ?? '')) {
    terminar(403);
}

try {
    $pdo = new PDO($config['db_dsn'], $config['db_usuario'] ?? null, $config['db_clave'] ?? null, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_EMULATE_PREPARES => false,
    ]);
    $fecha = (new DateTimeImmutable('now', new DateTimeZone('America/Santiago')))->format('Y-m-d');
    $sumar = $pdo->prepare('UPDATE ab_resultados SET total = total + 1 WHERE fecha = ? AND variante = ? AND evento = ?');
    $sumar->execute([$fecha, $variante, $evento]);
    if ($sumar->rowCount() === 0) {
        try {
            $pdo->prepare('INSERT INTO ab_resultados (fecha, variante, evento, total) VALUES (?, ?, ?, 1)')->execute([$fecha, $variante, $evento]);
        } catch (PDOException $choque) {
            // Otra visita creó la fila en ese instante
            $sumar->execute([$fecha, $variante, $evento]);
        }
    }
} catch (Throwable $error) {
    error_log('ab: ' . $error->getMessage());
}
terminar(204);
