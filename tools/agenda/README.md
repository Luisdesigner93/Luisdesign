# Conectar la agenda con Google Calendar

Mientras esto no esté hecho, el popup sigue mostrando solo el formulario.

## 1. Crear el acceso en Google Cloud

1. Entra a [Google Cloud Console](https://console.cloud.google.com/) con la cuenta del calendario y crea un proyecto.
2. En **APIs y servicios > Biblioteca**, activa **Google Calendar API**.
3. En **Google Auth Platform**, configura la app como **Externa** y agrega estos permisos:
   - `https://www.googleapis.com/auth/calendar.events`
   - `https://www.googleapis.com/auth/calendar.freebusy`
4. En **Público**, pulsa **Publicar app**. En modo de prueba, Google vence la autorización a los 7 días y la agenda dejaría de funcionar.
5. En **Clientes**, crea un cliente de tipo **App de escritorio** y guarda su ID y su secreto.

Como la app no pasa por la verificación de Google, al autorizar puede aparecer un aviso de app no verificada. Solo lo ves tú, porque las visitas nunca inician sesión en Google.

## 2. Autorizar tu calendario

```bash
php tools/agenda/autorizar-google.php
```

Pega el ID y el secreto, abre el enlace y autoriza. La terminal mostrará el `refresh_token`.

## 3. Configurar el servidor

1. En phpMyAdmin, ejecuta `tools/db/002_reservas.sql`.
2. En `luisdesign-config.php`, fuera de `public_html`, copia el bloque `agenda` de `tools/config/luisdesign-config.example.php`.
3. Completa `cliente_id`, `cliente_secreto` y `refresh_token`, revisa días, horas y feriados, y deja `'activa' => true`.
4. Agrega una tarea mensual con `tools/db/purga_12_meses.sql`, que ya incluye las reservas.

## 4. Probar

Abre el popup, agenda con un correo tuyo y confirma que llegue la invitación con Google Meet. Luego borra ese evento del calendario.
