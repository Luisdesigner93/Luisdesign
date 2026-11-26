<?php
// Plantilla de la configuración del formulario de contacto (contacto/guardar.php).
// En el servidor: copiar a /home/<usuario>/luisdesign-config.php, FUERA de public_html, y completar con los valores reales.
// Nunca subir el archivo real al repositorio.
return [
    'db_dsn' => 'mysql:host=localhost;dbname=NOMBRE_BASE;charset=utf8mb4',
    'db_usuario' => 'USUARIO_BASE',
    'db_clave' => 'CLAVE_BASE',
    'secreto' => 'CADENA_ALEATORIA_DE_MAS_DE_32_CARACTERES', // se usa para hashear la IP
    'origen' => 'https://luisdesign.cl',
    'copia_email' => 'contacto@luisdesign.cl', // vacío para no enviar copia por correo
    'remitente' => 'contacto@luisdesign.cl', // debe ser la casilla autenticada en SMTP (Titan)
    'smtp' => [
        'host' => 'smtp.titan.email',
        'puerto' => 465, // SSL directo
        'usuario' => 'contacto@luisdesign.cl',
        'clave' => 'CLAVE_DE_LA_CASILLA',
    ],
    // Agenda con Google Calendar (contacto/agenda.php). Pasos en tools/agenda/README.md.
    // Con 'activa' en false, o sin este bloque, el popup muestra solo el formulario.
    'agenda' => [
        'activa' => false,
        'cliente_id' => 'ID_DE_CLIENTE_OAUTH',
        'cliente_secreto' => 'SECRETO_DE_CLIENTE_OAUTH',
        'refresh_token' => 'REFRESH_TOKEN',
        'calendario' => 'primary', // donde se crean las reuniones
        'calendarios_ocupados' => ['primary'], // calendarios que bloquean horas
        'zona' => 'America/Santiago',
        'duracion' => 20, // minutos
        'dias' => [1, 3, 5], // 1 = lunes, 3 = miércoles, 5 = viernes
        'horas' => ['09:00', '14:00', '17:00'],
        'anticipacion_dias' => 2, // días de calendario
        'semanas' => 4, // semanas visibles
        'dias_bloqueados' => ['2026-12-08', '2026-12-25'], // feriados o vacaciones
    ],
];
