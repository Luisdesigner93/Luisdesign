# Plan de implementación: nueva narrativa de luisdesign.cl

Este documento es la guía para implementar en el código la narrativa definida con Luis. Los textos finales están en esta misma carpeta:

| Archivo | Contenido |
| --- | --- |
| `01-narrativa-y-casos.md` | Documento de trabajo completo: diagnóstico, decisiones, SEO, casos redactados y ajustes por caso. Es la fuente para los casos de estudio. |
| `02-landing-marcas.md` | Texto final de la home (landing para pymes). |
| `03-landing-producto-digital.md` | Texto final de la nueva landing `/producto-digital` (y su versión en inglés). |

Si un texto de `01` contradice a `02` o `03`, mandan `02` y `03` (son más recientes).

## Reglas de trabajo (obligatorias)

1. **Consultar antes de cambiar código.** Luis quiere aprobar cada cambio. Trabaja por fases: muestra el plan de la fase y los archivos que tocarás, espera su visto bueno, aplica y muestra el diff.
2. **Las páginas se generan.** Los `.html` salen de `tools/generador/` (ver `README.md`). No edites los `.html` a mano: cambia `tools/generador/build.py`, `tools/generador/pages/*.py` y `tools/generador/fragmentos/`, y luego ejecuta `python3 tools/generador/build.py`.
3. **CSP estricta.** Sin `style=""` ni `<script>` en línea, sin recursos de terceros, sin dependencias nuevas.
4. **Sin control de versiones.** La carpeta no tiene git. Antes de la fase 1, propón a Luis hacer `git init` y un primer commit del estado actual (o un respaldo comprimido) para poder volver atrás. Revisa que `.gitignore` siga cubriendo `.env`, `.DS_Store`, etc. No hagas push a ningún remoto sin que lo pida.
5. **Sin secretos ni datos sensibles** en el código. El RUT y el domicilio de `privacidad.html` los completa Luis.
6. **Español neutro** en todos los textos. Respeta los textos de `02` y `03` palabra por palabra; si algo no calza en el diseño, propón el ajuste en vez de reescribir por tu cuenta.
7. **La palabra "brecha"** aparece como máximo una vez por landing (en el manifiesto de la home). No la agregues en otros lugares.

## Mapa del sitio objetivo

| Página | Archivo | Estado |
| --- | --- | --- |
| Marcas (home) | `index.html` | Reescribir con `02` |
| Producto digital | `producto-digital.html` | Nueva, con `03` |
| Producto digital (inglés) | `en/digital-product.html` | Nueva, traducción de `03` (Luis la revisa) |
| Proyectos | `proyectos.html` | Ajustar filtros y tarjetas |
| Casos | `proyectos/*.html` | Reescribir y sumar casos |
| Sobre mí | `sobre-mi.html` | Nueva (historia completa, trayectoria, formación, CV) |
| Privacidad | `privacidad.html` | Se mantiene |
| Servicios | `servicios.html` | **Eliminar** (el sitio no está publicado: no hacen falta redirecciones) |

Menú y pie: **Marcas · Producto digital · Proyectos · Sobre mí · Contacto**.

## Fases

### Fase 0: reconocimiento (sin cambios)

- Lee `README.md`, `tools/generador/build.py`, `pages/0_data.py`, `pages/1_index.py`, `pages/3_proyectos.py` y `fragmentos/index-v2.html`.
- Aclara con Luis qué versión de la home es la vigente: `index.html` (página `1_index.py`) o `index-v2.html` (fragmento). La home nueva se construye sobre una sola.
- Entrega a Luis un resumen de la estructura actual y confirma el orden de las fases.

### Fase 1: estructura y navegación

- Menú y pie compartidos en `build.py` con los cinco enlaces nuevos.
- Eliminar `pages/2_servicios.py` y `servicios.html`; reemplazar todos los enlaces a `servicios.html` (están en `build.py`, `pages/1_index.py` y `fragmentos/index-v2.html`) por su landing: branding y web → `index.html#servicios`; UX/UI y Product Owner → `producto-digital.html`.
- Actualizar `sitemap.xml` y `404.html`.

### Fase 2: home (landing Marcas)

- Implementar las 7 secciones de `02-landing-marcas.md` en orden.
- El bloque de testimonios queda preparado pero oculto hasta tener las frases.
- Mensaje de WhatsApp precargado codificado en la URL `wa.me`.

### Fase 3: landing Producto digital

- Nueva página con las 6 secciones de `03`.
- Versión en inglés con `hreflang` entre ambas; marca la traducción para revisión de Luis.
- Contacto por `mailto:` con asunto precargado.

### Fase 4: proyectos y casos

- Filtros de `proyectos.html`: **Marcas · Producto digital · Logofolio** (reemplazan Branding, UX/UI y Logofolio).
- Orden: implementados primero. Khronos con etiqueta "Propuesta".
- Retirar Builder App (`pages`, `proyectos/builder-app.html`, imágenes y referencias).
- Renombrar "UV Energy" a **Uvenergy** en todos los textos (evaluar también renombrar el archivo a `uvenergy.html`).
- Sumar **LAB\*502** (caso completo) y **Bowraps** (ficha corta en Logofolio). Las imágenes de ambos están en Behance; Luis debe entregarlas en alta.
- Reescribir cada caso con la plantilla: ficha (cliente, año, rol, estado) · contexto y desafío · proceso y decisiones · solución · resultado · "Lo que me llevé" (solo Yomecontrolo y Bytequest). Textos en `01-narrativa-y-casos.md`, secciones "Selección de casos", "Caso redactado: …", "Ajustes al caso: …", "Caso Fuchi Chao reescrito en dos etapas" y "Enfoque de aprendizajes".
- Cada caso termina con un botón a su landing.
- Bytequest: no nombrar a la Fiscalía ni al cliente de emergencias; no usar el nombre "Sofía".
- Imágenes pendientes: mantener los marcadores `media-ph` existentes.

### Fase 5: Sobre mí

- Página nueva con la historia completa (versión de `02` + `03`), los aprendizajes, la trayectoria (hoy en la home), la formación (incluir el curso de Product Owner y Scrum de Coursera como curso, no como certificación) y un enlace para descargar el CV (Luis entrega el PDF).

### Fase 6: SEO y búsqueda por IA

- `title` y `meta description` de cada página según `02` y `03`.
- `og:image` y `twitter:card` en todas las páginas (hoy no existen).
- JSON-LD: `Person` y `ProfessionalService` en la home, `Service` en cada landing, `FAQPage` en las preguntas frecuentes y `CreativeWork` en cada caso. Como la CSP no permite scripts en línea, verifica que `<script type="application/ld+json">` sea compatible con la política actual o propón la alternativa.
- `canonical` y `hreflang` correctos.

### Fase 7: mejoras técnicas de la revisión inicial

- Imágenes: convertir a WebP o AVIF con `srcset` (hoy la home pesa unos 4,4 MB; las más pesadas son el retrato, el collage de productos y `hero-fondo.jpg`).
- Accesibilidad: las 9 tarjetas de `proyectos.html` no tienen nombre accesible (usar el patrón "Ver proyecto: …" de la home); el enlace del logo debe llamarse "Luis Vicencio, inicio"; áreas táctiles de al menos 44 px en el pie y en "Ver mi trayectoria".
- Animaciones de entrada: evitar que una sección quede en blanco al bajar rápido.

### Fase 8: verificación

- `python3 tools/generador/build.py` sin errores y `node tools/serve.mjs`.
- Consola sin errores de CSP, sin enlaces rotos, sin referencias a `servicios.html`, Builder App ni "UV Energy".
- Revisar a 375 px de ancho y en escritorio.
- Buscar `EDITAR`, `PENDIENTE` y `[` para listar lo que Luis aún debe completar.
- Informar qué se cambió, qué archivos se tocaron, qué se validó y qué quedó pendiente.

## Pendientes que dependen de Luis

- Testimonios: Sustentando, Citrex (Fuchi Chao), Uvenergy y Bytequest.
- Imágenes en alta: LAB\*502, Bowraps, Botes Salvavidas, Uvenergy, Bytequest/Legisnova.
- Reactivar contacto@luisdesign.cl.
- Ciudad para reuniones presenciales (landing Producto digital).
- Decidir si Sustentando sale de la landing Producto digital (recomendación: sí).
- Confirmar si se mantiene "He trabajado con marcas en Chile, Argentina y Alemania" en Sobre mí.
- CV en PDF para descargar.
- Nombre exacto del curso de Product Owner y Scrum (Coursera) y su año.

## Prompt sugerido para iniciar en Claude Code

> Lee `tools/narrativa/00-PLAN-para-claude-code.md` y los archivos 01, 02 y 03 de esa carpeta. Empieza por la Fase 0: no cambies nada todavía; resúmeme la estructura actual del generador y pregúntame qué versión de la home es la vigente. Después avanzamos fase por fase, mostrándome el plan y el diff de cada una antes de aplicarla.
