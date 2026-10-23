LOREM_S = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
LOREM_M = 'Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.'
LOREM_L = 'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam.'

# cats: categorías del filtro de Proyectos ('branding', 'ux-ui').
# Orden de aparición. AuditorWeb y Bytequest tienen contenido real; el resto usa texto provisorio (EDITAR).
# images: (archivo, ancho, alto, alt, leyenda, encajar). encajar=True muestra la imagen completa (envases, piezas recortadas).
def img(slug, name, w, h, alt, caption, fit=False):
    return dict(src=f'img/proyectos/{slug}/{name}', w=w, h=h, alt=alt, caption=caption, fit=fit)

PROJECTS = [
    dict(slug='auditorweb', cats=['ux-ui'], title='AuditorWeb 21.719', mark=None, kind='Producto digital', year='2026', featured=True,
         summary='Auditor automatizado que revisa 30 controles de cumplimiento de la Ley de Protección de Datos Personales y entrega un plan de acción priorizado.',
         tags=['Producto', 'UX/UI', 'Ley 21.719'], images=[], role='Producto, UX/UI y desarrollo asistido con IA', client='Producto propio'),
    dict(slug='bytequest', cats=['branding', 'ux-ui'], title='Bytequest', mark='Bq', kind='Producto e innovación', year='2025 – 2026', featured=False,
         summary='Liderazgo de producto e innovación: un módulo de IA para atención por chatbot, productos para el ámbito legislativo, municipal y de excelencia operacional, e identidades de marca.',
         tags=['Product Owner', 'Scrum', 'Branding'], images=[], role='Product Owner y Brand Manager', client='Bytequest SpA'),
    dict(slug='sustentando', cats=['branding'], title='Sustentando', mark='Su', kind='Consultoría en calidad · Branding y web', year='2022 – 2026', featured=True,
         summary='Desde 2022 acompaño a Sustentando como aliado estratégico. Partimos por entender sus necesidades y fuimos escalando el servicio hasta consolidar una comunicación que eleva el valor percibido de su trabajo.',
         tags=['Branding', 'Web', 'Comunicación'], role='Identidad, web, comunicación B2B y diseño gráfico', client='Sustentando',
         images=[img('sustentando', '01.jpg', 1600, 899, 'Piezas de Sustentando con los servicios de implementación, cursos, gestión de proveedores y proyectos de cultura y calidad.', 'Sistema de piezas para los servicios de Sustentando.'),
                 img('sustentando', '02.jpg', 1200, 1200, 'Logotipo de Sustentando sobre piezas gráficas y el sitio web en un teléfono.', 'Identidad y sitio web en móvil.'),
                 img('sustentando', '05.png', 800, 575, 'Llaveros, carpeta y piezas impresas de Sustentando OTEC.', 'Aplicaciones de marca para Sustentando OTEC.', True),
                 img('sustentando', '04.jpg', 1600, 899, 'Página de artículo del sitio web de Sustentando.', 'Página de artículo del sitio web.'),
                 img('sustentando', '03.jpg', 1600, 899, 'Plantillas de redes sociales de Sustentando organizadas por nivel de comunicación.', 'Plantillas de redes sociales por nivel de comunicación.'),
                 img('sustentando', '06.jpg', 1000, 939, 'Publicación de Sustentando en LinkedIn sobre un curso de auditores internos de calidad.', 'Publicación para LinkedIn.')]),
    dict(slug='yomecontrolo', cats=['branding', 'ux-ui'], title='Yomecontrolo', mark='Ym', kind='Salud preventiva · Branding y UX/UI', year='2023 – 2024', featured=True,
         summary='Estrategia, experiencia y expresión de marca para Yomecontrolo, una startup chilena de salud preventiva. Una marca que deja atrás la carga negativa de ir al médico y acompaña a las personas a cuidar su salud mucho antes de que llegue la enfermedad.',
         tags=['Branding', 'UX/UI', 'Producto'], role='Estrategia de marca, identidad y UX/UI', client='Yomecontrolo',
         images=[img('yomecontrolo', '05.jpg', 1672, 941, 'Sitio de Yomecontrolo en un portátil junto a la tarjeta de resultado de la calculadora de edad del corazón.', 'Calculadora de edad del corazón.'),
                 img('yomecontrolo', '06.jpg', 1629, 966, 'Logotipo de Yomecontrolo con el tagline “vivir más y mejor” sobre fondo celeste.', 'Logotipo.'),
                 img('yomecontrolo', '07.jpg', 906, 1736, 'Teléfono con la pantalla “Controla tus indicadores de salud” de la web app de Yomecontrolo.', 'Web app: indicadores de salud.'),
                 img('yomecontrolo', '08.jpg', 1122, 1402, 'Ícono de Yomecontrolo en la pantalla de inicio de un teléfono.', 'Acceso directo en el teléfono.')]),
    dict(slug='uv-energy', cats=['ux-ui'], title='UV Energy', mark='UV', kind='Energía solar · Sitio web', year='20XX', featured=False, summary=LOREM_S, tags=['Web', 'Contenidos'],
         images=[img('uv-energy', '01.jpg', 1600, 899, 'Página de artículo del sitio web de UV Energy sobre el mantenimiento de plantas fotovoltaicas.', 'Página de artículo del sitio web.')]),
    dict(slug='botes-salvavidas', cats=['branding'], title='Botes Salvavidas de Valparaíso', mark='BS', kind='Comunicación digital', year='20XX', featured=False, summary=LOREM_S, tags=['Redes sociales', 'Comunicación'],
         images=[img('botes-salvavidas', '01.jpg', 864, 1080, 'Pieza para redes sociales: rescatista en moto de agua con el mensaje “A las emergencias en el mar”.', 'Pieza para redes sociales.'),
                 img('botes-salvavidas', '02.jpg', 864, 1080, 'Pieza para redes sociales con un salvavidas y el mensaje “¡Estar preparados para el rescate!”.', 'Pieza para redes sociales.')]),
    dict(slug='khronos', cats=['branding'], title='Cerveza Khronos', mark='Kh', kind='Cerveza artesanal · Rebranding y packaging', year='2023', featured=True,
         summary='Rebranding para una cervecería artesanal nacida en las bierfest. Buscamos el sentido de su nombre en su raíz griega, khronos, tiempo, y lo convertimos en el concepto que guía la marca: tómate el tiempo.',
         tags=['Rebranding', 'Estrategia', 'Packaging'], role='Estrategia, concepto, identidad y packaging', client='Cervecería Khronos',
         # EDITAR: sumar las nuevas imágenes del proyecto a medida que estén listas
         images=[img('khronos', '05.jpg', 1672, 941, 'Logotipo de Cerveza Khronos con el tagline “Tómate el tiempo” en blanco sobre un muro naranja.', 'Logotipo.'),
                 img('khronos', '01.jpg', 1672, 941, 'Cuatro botellas de Cerveza Khronos flotando: American Pale Ale, Stout, IPA y Golden Ale.', 'Línea de cervezas.'),
                 img('khronos', '02.jpg', 1254, 1254, 'Fila de botellas Khronos con etiquetas de colores para cada variedad.', 'Un color por variedad.'),
                 img('khronos', '03.jpg', 1254, 1254, 'Botella de Cerveza Khronos Stout sobre un bloque de piedra.', 'Etiqueta Stout.'),
                 img('khronos', '04.jpg', 1254, 1254, 'Botella de Cerveza Khronos American Pale Ale con el tagline “Tómate el tiempo” sobre fondo naranja.', 'Etiqueta American Pale Ale.')]),
    dict(slug='fuchi-chao', cats=['branding'], title='Fuchi Chao', mark='Fc', kind='Productos para mascotas · Naming y packaging', year='2021', featured=False,
         summary='Naming, identidad y packaging para Citrex, emprendedoras locales que llevaron su experiencia en eliminación de olores al mundo de las mascotas. Una marca para quienes ven a su mascota como uno más del hogar, pero sin la parte fuchi.',
         tags=['Naming', 'Branding', 'Packaging', 'Comunicación'], role='Naming, identidad, packaging y comunicación', client='Citrex',
         images=[img('fuchi-chao', '01.jpg', 1397, 1400, 'Detergente, eliminador de olores y jabón anti olores Fuchi Chao sobre fondo rosado.', 'Línea de productos.'),
                 img('fuchi-chao', '04.jpg', 2000, 896, 'Construcción del logotipo de Fuchi Chao en tres versiones con su área de resguardo.', 'Construcción del logotipo.'),
                 img('fuchi-chao', '02.jpg', 2000, 1132, 'Tres teléfonos con el perfil y publicaciones de Instagram de Fuchi Chao.', 'Redes sociales.'),
                 img('fuchi-chao', '03.jpg', 2000, 1128, 'Envase del jabón anti olores Fuchi Chao junto a su etiqueta extendida con medidas.', 'Etiqueta del jabón anti olores.')]),
    dict(slug='builder-app', cats=['ux-ui'], title='Builder App', mark='Ba', kind='Lorem ipsum', year='20XX', featured=False, summary=LOREM_S, tags=['Lorem', 'Ipsum'], images=[]),
]

AUDITOR_ART = '''<div class="mini-window">
                <div class="mini-bar"><i></i><i></i><i></i><span></span></div>
                <div class="mini-report">
                  <div class="mini-gauge"><span>78</span></div>
                  <div class="mini-lines"><span class="sk sk-w80"></span><span class="sk sk-w60"></span><span class="sk sk-w40"></span><div class="mini-pills"><span>Cumple</span><span>Art. 14 ter</span></div></div>
                </div>
              </div>'''


def img_tag(im, cls='', lazy=True):
    c = (cls + (' fit-contain' if im['fit'] else '')).strip()
    src, w, h, alt = im['src'], im['w'], im['h'], im['alt']
    return (f'<img src="{{p}}{src}" width="{w}" height="{h}" alt="{alt}"'
            + (f' class="{c}"' if c else '') + (' loading="lazy"' if lazy else '') + ' decoding="async">')


def project_art(pr, lazy=True):
    if pr['images']:
        return img_tag(pr['images'][0], lazy=lazy)
    if pr['mark'] is None:
        return AUDITOR_ART
    # EDITAR: reemplazar por una imagen del proyecto (<img src="..." alt="" width height>)
    return f'''<div class="ph-art"><span class="ph-mark">{pr['mark']}</span><span class="sk-stack"><span class="sk sk-w80"></span><span class="sk sk-w55"></span></span></div>'''


def project_card(pr, heading='h3'):
    tags = ''.join(f'<li class="tag">{t}</li>' for t in pr['tags'])
    return f'''          <a class="card project" href="{{p}}proyectos/{pr['slug']}.html">
            <div class="project-art" aria-hidden="true">
              {project_art(pr)}
            </div>
            <div class="project-body">
              <span class="eyebrow-text">{pr['kind']} · {pr['year']}</span>
              <{heading} class="title">{pr['title']}</{heading}>
              <p>{pr['summary']}</p>
              <div class="project-meta">
                <ul class="tag-list" aria-label="Disciplinas">{tags}</ul>
                <span class="link-arrow">Ver caso <svg class="icon" aria-hidden="true"><use href="{{p}}img/icons.svg#i-arrow"/></svg></span>
              </div>
            </div>
          </a>
'''


def case_nav(pr):
    i = PROJECTS.index(pr)
    prev, nxt = PROJECTS[i - 1], PROJECTS[(i + 1) % len(PROJECTS)]
    return f'''    <section class="panel panel-plain section" aria-label="Otros proyectos">
      <div class="container">
        <nav class="case-nav" aria-label="Más proyectos">
          <a class="card" href="{prev['slug']}.html"><span>Proyecto anterior</span><strong>{prev['title']}</strong></a>
          <a class="card" href="{nxt['slug']}.html"><span>Proyecto siguiente</span><strong>{nxt['title']}</strong></a>
        </nav>
      </div>
    </section>
'''


# ---- Caso de estudio: composición minimalista (referencia: wama.com.br/cases) ----
# Arriba: columna fija con título, datos, disciplinas y resumen; a la derecha, las imágenes apiladas.
# Abajo: el detalle del caso en una sola columna de lectura.

def case_media(pr, placeholders=()):
    """Imágenes apiladas del caso. Sin imágenes: la portada ilustrada y marcadores (EDITAR)."""
    if pr['images']:
        return ''.join(f'\n            <figure>{img_tag(im, lazy=i > 0)}</figure>' for i, im in enumerate(pr['images']))
    out = f'\n            <figure class="case-art" aria-hidden="true">{project_art(pr, lazy=False)}</figure>'
    # EDITAR: reemplazar los marcadores por <img src="..." alt="..." width="..." height="..." loading="lazy">
    out += ''.join(f'\n            <figure><div class="media-ph" role="img" aria-label="Imagen pendiente: {c}"><svg class="icon" aria-hidden="true"><use href="{{p}}img/icons.svg#i-image"/></svg>{c}</div></figure>'
                   for c in placeholders)
    return out


def case_intro(pr, summary, facts, actions=''):
    rows = ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in facts)
    chips = ''.join(f'<li>{t}</li>' for t in pr['tags'])
    return f'''    <section class="case-intro" aria-labelledby="page-title">
      <div class="container case-intro-grid">
        <div class="case-aside">
          <ol class="breadcrumb" aria-label="Ruta"><li><a href="{{home}}">Inicio</a></li><li><a href="{{p}}proyectos.html">Proyectos</a></li><li aria-current="page">{pr['title']}</li></ol>
          <h1 class="case-title" id="page-title">{pr['title']}</h1>
          <dl class="case-meta">{rows}</dl>
          <ul class="case-chips" aria-label="Disciplinas">{chips}</ul>
          <p class="case-summary">{summary}</p>{actions}
        </div>
        <div class="case-media">{case_media(pr, pr.get('placeholders', ('Imagen del proyecto', 'Imagen del proyecto')))}
        </div>
      </div>
    </section>
'''


def case_rows(items):
    """Lista de responsabilidades: nombre y descripción."""
    return '<dl class="case-rows">' + ''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in items) + '</dl>'


def case_steps(items):
    return '<ol class="case-steps">' + ''.join(f'<li><strong>{k}</strong><span>{v}</span></li>' for k, v in items) + '</ol>'


def case_stats(items):
    return '<dl class="case-stats">' + ''.join(f'<div><dt>{n}</dt><dd>{t}</dd></div>' for n, t in items) + '</dl>'


def case_quote(text, cite):
    return f'<blockquote class="case-quote"><p>“{text}”</p><cite>{cite}</cite></blockquote>'


def case_detail(statement, sections):
    """sections: lista de (id, título, html). El título lleva <strong> en la palabra clave."""
    secs = ''.join(f'''
        <section class="case-sec" aria-labelledby="{sid}-title">
          <h2 class="case-sec-title" id="{sid}-title"><span class="numtag">{i:02d}</span>{title}</h2>
          <div class="case-text">{html}</div>
        </section>''' for i, (sid, title, html) in enumerate(sections, 1))
    return f'''
    <article class="case-detail" aria-label="Detalle del caso">
      <div class="container case-read">
        <p class="case-statement">{statement}</p>{secs}
      </div>
    </article>
'''


def lorem_case(pr):
    """Caso de estudio detallado con texto provisorio."""
    return '    <!-- EDITAR: contenido provisorio (lorem ipsum) -->\n' + case_intro(
        pr, LOREM_S,
        [('Cliente', pr.get('client', 'Lorem ipsum')), ('Año', pr['year']), ('Rol', pr.get('role', 'Lorem ipsum'))]
    ) + case_detail(f'{pr["title"]}: <strong>lorem ipsum</strong> dolor sit amet.', [
        ('contexto', 'Contexto y <strong>desafío</strong>', f'<p class="lead">{LOREM_S}</p><p>{LOREM_M}</p><p>{LOREM_L}</p>'),
        ('rol', 'Mi <strong>rol</strong>', f'<p>{LOREM_M}</p>' + case_rows([('Lorem ipsum', LOREM_S), ('Dolor sit amet', LOREM_S), ('Consectetur', LOREM_S)])),
        ('proceso', 'El <strong>proceso</strong>', f'<p class="lead">{LOREM_S}</p>' + case_steps([('Discovery', LOREM_S), ('Estrategia', LOREM_S), ('Diseño', LOREM_S), ('Implementación', LOREM_S)])),
        ('solucion', 'La <strong>solución</strong>', f'<p class="lead">{LOREM_S}</p><p>{LOREM_M}</p><ul><li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li><li>Sed do eiusmod tempor incididunt ut labore et dolore.</li><li>Ut enim ad minim veniam, quis nostrud exercitation.</li></ul>'),
        ('resultados', 'Resultados y <strong>aprendizajes</strong>', f'<p class="lead">{LOREM_S}</p>'
         + case_stats([('00', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'), ('00', 'Sed do eiusmod tempor incididunt ut labore et dolore.'), ('00', 'Ut enim ad minim veniam, quis nostrud exercitation.')])
         + case_quote('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.', 'Lorem ipsum, cargo · Empresa')),
    ]) + case_nav(pr)


# ---- Piezas del inicio compartidas entre index.html e index-v2.html (origen: referencia Stodio) ----
_clients = ['Bytequest', 'Studio Dinoi', 'Sustentando', 'Yomecontrolo', 'Cerveza Khronos', 'Fuchi Chao', 'UV Energy', 'Botes Salvavidas', 'Kimsa', 'Waterman']
# Logotipos para la cinta (nombre → (archivo, ancho, alto)); el resto se muestra como texto.
# EDITAR: idealmente reemplazar por SVG o PNG de mayor resolución (Khronos mide solo 56 × 25 px).
_client_logos = {'Cerveza Khronos': ('khronos.png', 56, 25), 'Sustentando': ('sustentando.png', 218, 64), 'Yomecontrolo': ('yomecontrolo.png', 156, 38)}


def _client_item(name):
    if name in _client_logos:
        f, w, h = _client_logos[name]
        return f'<li class="v2-marquee-logo"><img src="img/logos/{f}" width="{w}" height="{h}" alt="{name}" loading="lazy" decoding="async"></li>'
    return f'<li>{name}</li>'


_marquee = ''.join(_client_item(c) for c in _clients)
HOME_HERO = '''    <!-- HERO -->
    <section class="v2-hero-shell" aria-labelledby="v2-title">
      <div class="v2-hero">
        <img class="v2-hero-bg" src="img/marca/hero-fondo.jpg" width="2000" height="1333" alt="" decoding="async" fetchpriority="high">
        <div class="v2-hero-top">
          <span class="v2-eyebrow"><i aria-hidden="true"></i>Luis Vicencio · Diseñador</span>
          <h1 class="v2-hero-title" id="v2-title">Ayudo a empresas y pymes a <strong>definir su marca, diseñar su producto</strong> y llevarlo a producción con equipos ágiles.</h1>
          <p class="v2-hero-lead">Diseño marcas y productos con mirada de negocio.</p>
        </div>
        <div class="v2-hero-bottom">
          <ul class="v2-hero-meta" aria-label="Especialidades">
            <li>+ Branding</li>
            <li>+ Comunicación</li>
            <li>+ UX/UI</li>
            <li>+ Product Design</li>
            <li>+ Scrum</li>
            <li>+ PO</li>
            <li>+ Packaging</li>
            <li>+ Señalización</li>
            <li>+ IA</li>
          </ul>
          <div class="v2-hero-cta">
            <p>Branding, UX/UI y Product Owner para marcas que quieren destacar</p>
            <div class="btn-row">
              <a class="btn btn-primary v2-btn-light" href="proyectos.html">Ver proyectos <svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg></a>
              <a class="btn v2-btn-ghost" href="#contacto">Conversemos</a>
            </div>
          </div>
        </div>
      </div>
    </section>

'''

HOME_MARQUEE = '''    <!-- CINTA DE CLIENTES -->
    <section class="v2-marquee" aria-label="Marcas con las que he trabajado">
      <p class="v2-marquee-lead">Más de 7 años creando marcas y productos digitales</p>
      <div class="v2-marquee-track">
        <ul>{marquee}</ul>
        <ul aria-hidden="true">{marquee}</ul>
      </div>
    </section>

'''.replace('{marquee}', _marquee)

