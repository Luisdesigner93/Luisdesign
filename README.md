# luisdesign.cl

Sitio de Luis Vicencio, diseñador y Product Owner: branding estratégico, UX/UI, gestión de producto y sitios web. Sitio estático (HTML, CSS y JS sin frameworks ni dependencias) basado en el design system **Frost Glass**, el mismo de AuditorWeb 21.719.

## Páginas

| Archivo | Contenido |
|---|---|
| `index.html` | Inicio (landing Marcas): hero, logos, manifiesto, servicios, proyectos, sobre mí y contacto |
| `producto-digital.html` | Landing Producto digital (empresas de software, startups e innovación) |
| `en/digital-product.html` | Versión en inglés de Producto digital (traducción pendiente de revisión) |
| `index-v2.html` | Versión alternativa del inicio, solo como referencia (`noindex`) |
| `proyectos.html` | Listado de proyectos |
| `proyectos/*.html` | Casos de estudio (Fuchi Chao, Bytequest, LAB*502, Sustentando, Yomecontrolo, AuditorWeb, Uvenergy, Botes Salvavidas y Khronos) con la plantilla de `tools/narrativa/` |
| `privacidad.html` | Política de privacidad y cookies (Ley 21.719) |
| `404.html` | Página de error (usa rutas absolutas porque se sirve desde cualquier URL) |

## Estructura

```
css/styles.css     Tokens y componentes de Frost Glass + componentes del portafolio
js/main.js         Header que se oculta al bajar, menú móvil y año del pie
img/icons.svg      Sprite de íconos de línea (se usa con <use href="img/icons.svg#i-…">)
img/marca/         Logo "luy design" y retrato
img/proyectos/     Imágenes de cada caso (recuperadas del respaldo del sitio anterior, optimizadas)
fonts/             Plus Jakarta Sans variable autoalojada (licencia OFL en fonts/OFL.txt)
.htaccess          HTTPS, cabeceras de seguridad (CSP, HSTS…), caché y 404 para Apache/cPanel
tools/serve.mjs    Servidor local de vista previa (no se publica)
tools/generador/   Generador de las páginas HTML (no se publica)
```

Los `.html` se generan con `tools/generador/`: no los edites a mano, porque el próximo build los sobrescribe.

## Generar las páginas

Requiere Python 3.9 o superior, sin dependencias.

```bash
python3 tools/generador/build.py
```

- `tools/generador/build.py`: cabecera, contacto y pie compartidos por todas las páginas.
- `tools/generador/pages/0_data.py`: proyectos (textos, imágenes, rol, cliente) y piezas del inicio.
- `tools/generador/pages/*.py`: una página o caso por archivo, en orden alfabético.
- `tools/generador/fragmentos/`: contenido de privacidad, 404 e inicio v2, que se edita directamente ahí.

Para comprobar un cambio sin tocar el sitio: `python3 tools/generador/build.py /ruta/temporal` y compara con `diff -r`.

## Vista previa local

Requiere Node.js 18 o superior.

```bash
node tools/serve.mjs
```

Abre http://localhost:4173. El servidor local envía la misma CSP que `.htaccess`, para detectar a tiempo estilos o scripts en línea (no están permitidos).

## Publicación (cPanel)

1. Sube a `public_html/` todo el contenido **excepto** `tools/`, `.claude/`, `README.md` y `.gitignore` (de todos modos `.htaccess` bloquea su acceso).
2. Verifica que el certificado SSL esté activo; `.htaccess` redirige todo a HTTPS.
3. Revisa las cabeceras con AuditorWeb o con `curl -I https://luisdesign.cl`.

## Antes de publicar

Busca `EDITAR` en los archivos y completa:

- Imágenes de Bytequest, LAB*502, Bowraps y AuditorWeb (marcadores `media-ph` y `ph-mark`); buscar `EDITAR` en `tools/generador/` para el resto.
- RUT, domicilio y correo de contacto del responsable en `privacidad.html`.
- Proveedores de hosting y correo, y el país de sus servidores, en `privacidad.html`.
- URL pública de AuditorWeb en `proyectos/auditorweb.html`.

## Privacidad y seguridad

- Sin cookies, sin rastreadores, sin formularios y sin recursos de terceros.
- CSP estricta: `script-src 'self'` y `style-src 'self'`, sin `unsafe-inline`. No uses atributos `style` ni `<script>` en línea.
- Si en el futuro agregas analítica o un formulario, actualiza la política de privacidad y, si usa cookies no esenciales, agrega consentimiento previo.
