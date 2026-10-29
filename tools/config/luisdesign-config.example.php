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
    'remitente' => 'no-responder@luisdesign.cl', // debe ser una dirección del dominio, para que el correo no caiga en spam
];
