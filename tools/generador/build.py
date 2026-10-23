"""Generador del sitio luisdesign.cl.

Arma cada página con el mismo header, contacto y footer, y ejecuta los scripts de pages/ en orden alfabético.
Los scripts comparten un mismo espacio de nombres: 0_data.py define los proyectos y las piezas comunes.

Uso (desde la raíz del proyecto):
    python3 tools/generador/build.py            # escribe en la raíz del proyecto
    python3 tools/generador/build.py <destino>  # escribe en otra carpeta (útil para comparar)

En el texto de cada página, {p} se reemplaza por la ruta a la raíz (''/'../'/'/') y {home} por el enlace al inicio.
"""
import re
from urllib.parse import quote
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE.parent.parent
SITE = 'https://luisdesign.cl/'

HEAD = '''<!doctype html>
<html lang="es-CL" class="{html_class}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{desc}">
{robots}  <link rel="canonical" href="{url}">
  <meta property="og:type" content="{ogtype}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:locale" content="es_CL">
  <meta name="theme-color" content="#ffffff">
  <link rel="icon" href="{p}favicon.png" type="image/png" sizes="64x64">
  <link rel="apple-touch-icon" href="{p}apple-touch-icon.png">
  <link rel="preload" href="{p}fonts/plus-jakarta-sans.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{p}css/styles.css">
{extra_css}  <script src="{p}js/theme.js"></script>
  <script src="{p}js/main.js" defer></script>
</head>
<body>
  <!-- Pantalla de carga: la firma "luis" se escribe con un trazo que revela el logo (solo la primera página de cada visita) -->
  <div class="loader" id="loader" aria-hidden="true">
    <svg class="loader-logo" viewBox="0 0 500 265" focusable="false">
      <defs>
        <mask id="loader-ink" maskUnits="userSpaceOnUse" x="0" y="0" width="500" height="265">
          <path class="loader-stroke" pathLength="1" fill="none" stroke="#fff" stroke-width="34" stroke-linecap="round" stroke-linejoin="round"
            d="M114 30 L104 61 L93 91 L85 121 L80 151 L78 196 C92 160 112 118 130 97 C127 130 122 165 119 197 C132 160 150 118 170 97 C167 130 162 165 159 197 C172 160 190 118 210 97 C207 130 202 165 198 197 C212 160 230 118 251 93 C247 130 241 170 235 206 C231 214 220 214 222 222 C224 230 238 230 244 220 C246 212 243 205 246 198 C256 186 270 172 290 160"/>
        </mask>
        <clipPath id="loader-word"><rect x="292" y="140" width="208" height="70"/></clipPath>
      </defs>
      <image href="{p}img/marca/logo-luy-design.png" width="500" height="265" mask="url(#loader-ink)"/>
      <image class="loader-design" href="{p}img/marca/logo-luy-design.png" width="500" height="265" clip-path="url(#loader-word)"/>
    </svg>
  </div>
  <a class="skip-link" href="#contenido">Saltar al contenido</a>

  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="{home}" aria-label="Luis Design, inicio">
        <img class="brand-logo" src="{p}img/marca/logo-luy-design.png" width="500" height="265" alt="">
        <span class="brand-tagline">Branding, UX/UI<br>y Producto</span>
      </a>
      <nav class="main-nav" id="main-nav" aria-label="Principal">
        <p class="nav-title" aria-hidden="true">Luis Design<span>Branding, UX/UI y producto</span></p>
        <a href="{home}"{cur_marcas}>Marcas</a>
        <a href="{p}producto-digital.html"{cur_producto}>Producto digital</a>
        <div class="nav-item has-sub">
          <a href="{p}proyectos.html"{cur_proyectos}>Proyectos</a>
          <button class="nav-sub-toggle" type="button" aria-expanded="false" aria-controls="sub-proyectos" aria-label="Categorías de proyectos">
            <svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-chevron"/></svg>
          </button>
          <ul class="nav-sub" id="sub-proyectos">
            <li><a href="{p}proyectos.html?cat=branding">Branding</a></li>
            <li><a href="{p}proyectos.html?cat=ux-ui">UX/UI</a></li>
            <li><a href="{p}proyectos.html?cat=logofolio">Logofolio</a></li>
          </ul>
        </div>
        <a href="{home}#sobre-mi">Sobre mí</a>
        <a href="{contact_href}">Contacto</a>
        <div class="nav-foot">
          <div class="nav-foot-row">
            <button class="theme-toggle nav-theme" type="button" aria-pressed="false" aria-label="Cambiar a modo oscuro">
              <svg class="icon i-moon" aria-hidden="true"><use href="{p}img/icons.svg#i-moon"/></svg>
              <svg class="icon i-sun" aria-hidden="true"><use href="{p}img/icons.svg#i-sun"/></svg>
              <span class="t-dark">Modo oscuro</span><span class="t-light">Modo claro</span>
            </button>
            <a class="nav-social" href="https://www.linkedin.com/in/luisvicenciodesign" rel="noopener noreferrer" target="_blank">LinkedIn<span class="sr-only"> (se abre en una pestaña nueva)</span></a>
            <a class="nav-social" href="https://wa.me/56958217041" rel="noopener noreferrer" target="_blank">WhatsApp<span class="sr-only"> (se abre en una pestaña nueva)</span></a>
          </div>
        </div>
      </nav>
      <div class="header-actions">
        <button class="btn btn-secondary theme-toggle" type="button" aria-pressed="false" aria-label="Cambiar a modo oscuro">
          <svg class="icon i-moon" aria-hidden="true"><use href="{p}img/icons.svg#i-moon"/></svg>
          <svg class="icon i-sun" aria-hidden="true"><use href="{p}img/icons.svg#i-sun"/></svg>
        </button>
        <a class="btn btn-primary" href="{contact_href}">Conversemos</a>
        <button class="btn btn-secondary menu-toggle" type="button" aria-expanded="false" aria-controls="main-nav" aria-label="Abrir menú">
          <svg class="icon i-open" aria-hidden="true"><use href="{p}img/icons.svg#i-menu"/></svg>
          <svg class="icon i-close" aria-hidden="true"><use href="{p}img/icons.svg#i-close"/></svg>
        </button>
      </div>
    </div>
  </header>

  <main id="contenido">
'''

CONTACT = '''
    <!-- CONTACTO -->
    <section class="panel frame-grid cta-final" id="contacto" aria-labelledby="contacto-title">
      <div class="container">
        <span class="icon-tile" aria-hidden="true"><span><svg class="icon"><use href="{p}img/icons.svg#i-chat"/></svg></span></span>
        <h2 class="heading" id="contacto-title">{cta_title}</h2>
        <p class="lead">{cta_lead}</p>
        <div class="btn-row">
          <a class="btn btn-primary" href="{wa_href}" rel="noopener noreferrer" target="_blank"><svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-chat"/></svg>Escríbeme por WhatsApp<span class="sr-only"> (se abre en una pestaña nueva)</span></a>
{contact_email}          <a class="btn btn-outline" href="https://www.linkedin.com/in/luisvicenciodesign" rel="noopener noreferrer" target="_blank"><svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-user"/></svg>LinkedIn<span class="sr-only"> (se abre en una pestaña nueva)</span></a>
        </div>
        <p class="section-cta-note"><span>+56 9 5821 7041</span><span>Sin formularios ni cookies</span><span>Respuesta en 1 a 2 días hábiles</span></p>
      </div>
    </section>
'''

FOOT = '''  </main>

  <footer class="site-footer container">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{home}" aria-label="Luis Design, inicio"><img class="brand-logo" src="{p}img/marca/logo-luy-design.png" width="500" height="265" alt=""><span class="brand-tagline">Branding, UX/UI<br>y Producto</span></a>
        <p>Este sitio no usa cookies ni rastreadores de terceros.</p>
        <ul class="footer-social"><li><a href="https://www.linkedin.com/in/luisvicenciodesign" rel="noopener noreferrer" target="_blank">LinkedIn</a></li><li><a href="https://wa.me/56958217041" rel="noopener noreferrer" target="_blank">WhatsApp</a></li></ul>
      </div>
      <nav aria-labelledby="f-sitio">
        <h2 id="f-sitio">Sitio</h2>
        <ul><li><a href="{home}">Marcas</a></li><li><a href="{p}producto-digital.html">Producto digital</a></li><li><a href="{p}proyectos.html">Proyectos</a></li><li><a href="{home}#sobre-mi">Sobre mí</a></li><li><a href="{contact_href}">Contacto</a></li></ul>
      </nav>
      <nav aria-labelledby="f-legal">
        <h2 id="f-legal">Legal</h2>
        <ul><li><a href="{p}privacidad.html"{cur_privacidad}>Política de privacidad</a></li><li><a href="{p}privacidad.html#cookies">Cookies</a></li></ul>
      </nav>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> Luis Vicencio · luisdesign.cl</span>
      <span>Branding, UX/UI y producto digital · Chile</span>
    </div>
  </footer>
</body>
</html>
'''

CTA_TITLE = 'Conversemos sobre <strong>tu proyecto</strong>.'
CTA_LEAD = 'Cuéntame en qué etapa está tu marca o tu producto y te respondo con una propuesta de alcance, plazos y presupuesto.'
WA_HREF = 'https://wa.me/56958217041'
# EDITAR: reactivar la casilla contacto@luisdesign.cl antes de publicar
EMAIL = 'contacto@luisdesign.cl'


def fill(template, values):
    """Reemplaza {clave} por su valor sin interpretar otras llaves del HTML."""
    return re.sub(r'\{(\w+)\}', lambda m: values.get(m.group(1), m.group(0)), template)


# ---- Mayúscula en cada palabra solo en los títulos de tarjetas (los títulos de sección quedan como oración) ----
_MINOR = {'y', 'e', 'o', 'u', 'de', 'del', 'a', 'al', 'en', 'el', 'la', 'los', 'las'}


def _title_case(text):
    def word(m):
        w, i = m.group(0), m.start()
        if any(c.isupper() for c in w[1:]) or w.isupper():
            return w  # siglas o marcas (UX/UI, CEO, QA, AuditorWeb)
        if i > 0 and w.lower() in _MINOR:
            return w.lower()
        return w[:1].upper() + w[1:]
    # Solo el texto fuera de etiquetas HTML
    return re.sub(r'(<[^>]+>)|([^<]+)', lambda m: m.group(1) or re.sub(r"[\wáéíóúñüÁÉÍÓÚÑÜ/.'-]+", word, m.group(2)), text)


def _card_titles(html):
    rules = [
        (r'(<(?:span|h3) class="(?:svc-card-title|card-title)">)(.*?)(</(?:span|h3)>)', None),
        (r'(<(article|li) class="card step">(?:(?!</\2>).)*?<h3 class="title">)(.*?)(</h3>)', 'step'),
        (r'(<li class="card"><span class="icon-key"[^>]*>.*?</span><div><strong>)(.*?)(</strong>)', None),
        (r'(<ol class="career">.*?</ol>)', 'career'),
    ]
    for pattern, kind in rules:
        if kind == 'step':
            html = re.sub(pattern, lambda m: m.group(1) + _title_case(m.group(3)) + m.group(4), html, flags=re.S)
        elif kind == 'career':
            html = re.sub(pattern, lambda m: re.sub(r'(<h3>)([^<]+)( <span class="career-org">)', lambda n: n.group(1) + _title_case(n.group(2)) + n.group(3), m.group(1)), html, flags=re.S)
        else:
            html = re.sub(pattern, lambda m: m.group(1) + _title_case(m.group(2)) + m.group(3), html, flags=re.S)
    return html


def page(path, title, desc, body, current=None, contact=True, cta_title=None, cta_lead=None, ogtype='website',
         noindex=False, absolute=False, html_class='motion', canonical=None, extra_css=None, wa_href=None, email_subject=None):
    depth = path.count('/')
    if absolute:
        p, home = '/', '/'
    else:
        p = '../' * depth
        home = p or './'
    url = SITE + (path if canonical is None else canonical)
    values = {
        'html_class': html_class, 'title': title, 'desc': desc, 'url': url, 'ogtype': ogtype, 'p': p, 'home': home,
        'robots': '  <meta name="robots" content="noindex">\n' if noindex else '',
        'extra_css': f'  <link rel="stylesheet" href="{p}{extra_css}">\n' if extra_css else '',
        'contact_href': '#contacto' if contact else home + '#contacto',
        'cur_marcas': ' aria-current="page"' if current == 'marcas' else '',
        'cur_producto': ' aria-current="page"' if current == 'producto' else '',
        'cur_proyectos': ' aria-current="page"' if current == 'proyectos' else '',
        'cur_privacidad': ' aria-current="page"' if current == 'privacidad' else '',
        'cta_title': cta_title or CTA_TITLE, 'cta_lead': cta_lead or CTA_LEAD,
        'wa_href': wa_href or WA_HREF,
        # Correo solo en las landings que lo piden (email_subject='' agrega el botón sin asunto)
        'contact_email': '' if email_subject is None else
            f'          <a class="btn btn-outline" href="mailto:{EMAIL}' + (f'?subject={quote(email_subject)}' if email_subject else '') +
            f'"><svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-mail"/></svg>{EMAIL}</a>\n',
    }
    html = fill(HEAD, values) + fill(body, values)
    if contact:
        html += fill(CONTACT, values)
    html += fill(FOOT, values)
    html = _card_titles(html)
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding='utf-8')
    print('ok', path)


def fragment(name):
    """Contenido de una página guardado tal cual en fragmentos/ (páginas sin datos compartidos)."""
    return (HERE / 'fragmentos' / name).read_text(encoding='utf-8')


env = {'page': page, 'fragment': fragment, '__name__': 'luisdesign_pages'}
for script in sorted((HERE / 'pages').glob('*.py')):
    exec(compile(script.read_text(encoding='utf-8'), str(script), 'exec'), env)
