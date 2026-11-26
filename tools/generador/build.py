"""Generador del sitio luisdesign.cl.

Arma cada página con el mismo header, contacto y footer, y ejecuta los scripts de pages/ en orden alfabético.
Los scripts comparten un mismo espacio de nombres: 0_data.py define los proyectos y las piezas comunes.

Uso (desde la raíz del proyecto):
    python3 tools/generador/build.py            # escribe en la raíz del proyecto
    python3 tools/generador/build.py <destino>  # escribe en otra carpeta (útil para comparar)

En el texto de cada página, {p} se reemplaza por la ruta a la raíz (''/'../'/'/') y {home} por el enlace al inicio.
"""
import json
import posixpath
import re
from urllib.parse import quote
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else HERE.parent.parent
SITE = 'https://luisdesign.cl/'

HEAD = '''<!doctype html>
<html lang="{html_lang}" class="{html_class}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{title}</title>
  <meta name="description" content="{desc}">
{robots}  <link rel="canonical" href="{url}">
{alternates}  <meta property="og:type" content="{ogtype}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:locale" content="{og_locale}">
  <meta property="og:image" content="{og_image}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="{og_alt}">
  <meta name="twitter:card" content="summary_large_image">
{jsonld}  <meta name="theme-color" content="#ffffff">
  <link rel="icon" href="{p}favicon.png" type="image/png" sizes="64x64">
  <link rel="apple-touch-icon" href="{p}apple-touch-icon.png">
  <link rel="preload" href="{p}fonts/plus-jakarta-sans.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{p}css/styles.css">
{extra_css}{ab_script}  <script src="{p}js/intro.js"></script>
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
      <image href="{p}img/webp/marca/logo-luis-design-500.webp" width="500" height="265" mask="url(#loader-ink)"/>
      <image class="loader-design" href="{p}img/webp/marca/logo-luis-design-500.webp" width="500" height="265" clip-path="url(#loader-word)"/>
    </svg>
  </div>
  <a class="skip-link" href="#contenido">Saltar al contenido</a>

  <header class="site-header">
    <div class="header-inner">
      <a class="brand" href="{home}" aria-label="Luis Vicencio, inicio">
        <img class="brand-logo" src="{p}img/marca/logo-luis-design.png" width="500" height="265" alt="">
        <span class="brand-tagline">Branding, UX/UI<br>y Producto</span>
      </a>
      <nav class="main-nav" id="main-nav" aria-label="Principal">
        <p class="nav-title" aria-hidden="true">Luis Design<span>Branding, UX/UI y Producto</span></p>
{nav_servicios}        <a href="{proyectos_href}"{cur_proyectos}>Proyectos</a>
        <a href="{blog_href}"{cur_noticias}>Blog</a>
        <a href="{sobre_href}"{cur_sobre}>Sobre mí</a>
        <div class="nav-foot">
          <div class="nav-foot-row">
            {lang_switch}
            <div class="nav-social-row">
              <a class="nav-social" href="https://www.linkedin.com/in/luisvicenciodesign" rel="noopener noreferrer" target="_blank"><svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-linkedin"/></svg><span class="sr-only">LinkedIn (se abre en una pestaña nueva)</span></a>
              <a class="nav-social" href="https://wa.me/56958217041" rel="noopener noreferrer" target="_blank"><svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-whatsapp"/></svg><span class="sr-only">WhatsApp (se abre en una pestaña nueva)</span></a>
            </div>
          </div>
        </div>
      </nav>
      <div class="header-actions">
        {lang_switch}
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
{contact_buttons}        </div>
        <p class="section-cta-note"><span>+56 9 5821 7041</span><span>Analítica solo con tu permiso</span><span>Respuesta en 1 a 2 días hábiles</span></p>
      </div>
    </section>
'''

FOOT = '''  </main>

  <footer class="site-footer container">
    <div class="footer-grid">
      <div>
        <a class="brand" href="{home}" aria-label="Luis Vicencio, inicio"><img class="brand-logo" src="{p}img/marca/logo-luis-design.png" width="500" height="265" alt=""><span class="brand-tagline">Branding, UX/UI<br>y Producto</span></a>
        <p class="footer-intro">Luis Vicencio, diseñador de marca y UX/UI en Chile. Branding estratégico, identidad corporativa, diseño de productos digitales y páginas web para empresas y startups.</p>
        <ul class="footer-social"><li><a href="tel:+56958217041">+56 9 5821 7041</a></li><li><a href="mailto:{email}">{email}</a></li></ul>
        <ul class="footer-social footer-redes"><li><a href="https://www.linkedin.com/in/luisvicenciodesign" rel="noopener noreferrer" target="_blank" aria-label="LinkedIn" title="LinkedIn"><svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-linkedin"/></svg></a></li><li><a href="https://www.behance.net/LuisHVicencio" rel="noopener noreferrer" target="_blank" aria-label="Behance" title="Behance"><svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-behance"/></svg></a></li><li><a href="https://wa.me/56958217041" rel="noopener noreferrer" target="_blank" aria-label="WhatsApp" title="WhatsApp"><svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-whatsapp"/></svg></a></li></ul>
      </div>
      <nav aria-labelledby="f-sitio">
        <h2 id="f-sitio">Sitio</h2>
        <ul><li><a href="{proyectos_href}">Proyectos</a></li><li><a href="{blog_href}">Blog</a></li><li><a href="{sobre_href}">Sobre mí</a></li><li><a href="{contact_href}">Contacto</a></li></ul>
      </nav>
      <nav aria-labelledby="f-legal">
        <h2 id="f-legal">Legal</h2>
        <ul><li><a href="{p}privacidad.html"{cur_privacidad}>Política de privacidad</a></li><li><a href="{p}privacidad.html#cookies">Cookies</a></li></ul>
      </nav>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> Luis Vicencio · luisdesign.cl</span>
      <span>Branding, UX/UI y Producto Digital · Chile</span>
    </div>
  </footer>

{dialogo}  <section class="cookie-banner" id="cookie-banner" data-gtm="{gtm_id}" data-ga="{ga_id}" data-clarity="{clarity_id}" aria-labelledby="cookie-title" hidden>
    <div class="cookie-banner-text">
      <h2 id="cookie-title">Cookies y analítica</h2>
      <p>Uso Google Tag Manager, Google Analytics y Microsoft Clarity solo si los aceptas. Si no, no se cargan ni se guardan cookies de analítica. Tu elección queda guardada en una cookie técnica. <a href="{p}privacidad.html#cookies">Más información</a>.</p>
    </div>
    <div class="cookie-banner-actions">
      <button class="btn btn-secondary" type="button" data-consent="rechazado">Rechazar</button>
      <button class="btn btn-primary" type="button" data-consent="aceptado">Aceptar</button>
    </div>
  </section>
  <script src="{p}js/consent.js" defer></script>
</body>
</html>
'''

CTA_TITLE = 'Conversemos sobre <strong>tu proyecto</strong>.'
CTA_LEAD = 'Agendemos una reunión para que hablemos de lo que está pasando con tu marca y hacia dónde la quieres llevar. El presupuesto viene después de conversar.'
WA_HREF = 'https://wa.me/56958217041'
OG_DEFAULT = 'img/og/general.jpg'
OG_ALT = 'Luis Vicencio, diseñador y Product Owner'
# EDITAR: reactivar la casilla contacto@luisdesign.cl antes de publicar
EMAIL = 'contacto@luisdesign.cl'
# EDITAR: ID del contenedor de Google Tag Manager (formato GTM-XXXXXXX). Mientras diga XXXX, no se carga nada de Google.
GTM_ID = 'GTM-M8GHZ2BZ'
# ID de medición de Google Analytics 4 (flujo "Luis Design - GA4"). Se carga solo con consentimiento, igual que GTM.
GA_ID = 'G-42SV1ZZ5S1'
# EDITAR: ID del proyecto de Microsoft Clarity (Configuración → Información general). Vacío: no se carga. Solo con consentimiento.
CLARITY_ID = 'zgo49leb9c'
_EXT = ' rel="noopener noreferrer" target="_blank"'
_NEW_TAB = '<span class="sr-only"> (se abre en una pestaña nueva)</span>'

# Textos del menú, el contacto y el pie para las páginas en inglés (pares español → inglés, en orden)
EN_CHROME = [
    ('Saltar al contenido', 'Skip to content'),
    ('aria-label="Luis Vicencio, inicio"', 'aria-label="Luis Vicencio, home"'),
    ('Branding, UX/UI<br>y Producto', 'Branding, UX/UI<br>and Product'),
    ('aria-label="Principal"', 'aria-label="Main"'),
    ('<span>Branding, UX/UI y Producto</span>', '<span>Branding, UX/UI and Product</span>'),
    ('>Marcas</a>', '>Brands</a>'),
    ('>Marcas</a></li>', '>Brands</a></li>'),
    ('>Proyectos</a>', '>Projects</a>'),
    ('aria-label="Categorías de proyectos"', 'aria-label="Project categories"'),
    ('>Sobre mí</a>', '>About</a>'),
    ('>Contacto</a>', '>Contact</a>'),
    (' (se abre en una pestaña nueva)', ' (opens in a new tab)'),
    ('>Conversemos</a>', '>Let’s talk</a>'),
    ('<mark class="pl-mark">¡Hablemos</mark> <br>de tu <br>proyecto!</h2>', '<mark class="pl-mark">Let’s talk</mark> <br>about your <br>project!</h2>'),
    ('Agendemos una reunión para que hablemos de lo que está pasando con tu marca y hacia dónde la quieres llevar. El presupuesto viene después de conversar.',
     'Let’s schedule a meeting to talk about what is happening with your brand and where you want to take it. The budget comes after we talk.'),
    ('>Nombre</label>', '>Name</label>'), ('>Correo</label>', '>Email</label>'), ('>Mensaje</label>', '>Message</label>'),
    ('No completes este campo', 'Leave this field empty'),
    ('Acepto que guarden mi nombre, correo y mensaje para responderme. Lo explico en la <a', 'I agree that my name, email and message are stored so I can reply. See the <a'),
    ('>política de privacidad</a>.</span>', '>privacy policy</a>.</span>'),
    ('>Enviar</button>', '>Send</button>'),
    ('aria-label="Agendar una reunión"', 'aria-label="Schedule a meeting"'),
    ('aria-label="Mes anterior"', 'aria-label="Previous month"'), ('aria-label="Mes siguiente"', 'aria-label="Next month"'),
    ('aria-label="Paso 1 de 3"', 'aria-label="Step 1 of 3"'),
    ('>Agendemos meet</p>', '>Let’s book a Meet</p>'), ('data-titulo>Elige un día</h3>', 'data-titulo>Pick a day</h3>'),
    ('20 min · Google Meet · hora de Chile', '20 min · Google Meet · Chile time'),
    ('aria-label="Volver"', 'aria-label="Back"'),
    ('aria-label="Volver a la agenda"', 'aria-label="Back to scheduling"'),
    ('>o solo envíame un mensaje</button>', '>or just send me a message</button>'),
    ('>Escríbeme</h3>', '>Write to me</h3>'),
    ('>Cuéntame de tu proyecto (opcional)</label>', '>Tell me about your project (optional)</label>'),
    ('Acepto que usen mis datos para agendar la reunión en Google Calendar. Lo explico en la <a', 'I agree that my data is used to schedule the meeting in Google Calendar. See the <a'),
    ('>Confirmar reunión</button>', '>Confirm meeting</button>'),
    ('>Reunión agendada</p>', '>Meeting scheduled</p>'),
    ('aria-label="Cerrar"', 'aria-label="Close"'),
    ('alt="Persona subiendo una escalera de bloques de concreto junto a paneles de vidrio y un arco verde lima con una flecha."',
     'alt="A person climbing a staircase of concrete blocks beside glass panels and a lime green arc with an arrow."'),
    ('alt="Silueta de perfil de una persona entre paneles de vidrio translúcido y esmerilado, con un panel verde lima detrás."',
     'alt="Profile silhouette of a person between translucent and frosted glass panels, with a lime green panel behind."'),
    ('aria-label="Abrir menú"', 'aria-label="Open menu"'),
    ('Escríbeme por WhatsApp', 'Message me on WhatsApp'),
    ('Respuesta en 1 a 2 días hábiles', 'Reply within 1 to 2 business days'),
    ('<p class="footer-intro">Luis Vicencio, diseñador de marca y UX/UI en Chile. Branding estratégico, identidad corporativa, diseño de productos digitales y páginas web para empresas y startups.</p>', '<p class="footer-intro">Luis Vicencio, brand and UX/UI designer in Chile. Strategic branding, corporate identity, digital product design and websites for companies and startups.</p>'),
    ('<span>Analítica solo con tu permiso</span>', '<span>Analytics only with your permission</span>'),
    ('>Sitio</h2>', '>Site</h2>'),
    ('>Política de privacidad</a>', '>Privacy policy (Spanish)</a>'),
    ('Branding, UX/UI y Producto Digital · Chile', 'Branding, UX/UI and Digital Product · Chile'),
    ('Cookies y analítica', 'Cookies and analytics'),
    ('Uso Google Tag Manager, Google Analytics y Microsoft Clarity solo si los aceptas. Si no, no se cargan ni se guardan cookies de analítica. Tu elección queda guardada en una cookie técnica.',
     'I use Google Tag Manager, Google Analytics and Microsoft Clarity only if you accept. If not, no analytics cookies are loaded or stored. Your choice is saved in a technical cookie.'),
    ('>Más información</a>', '>More information</a>'),
    ('data-consent="rechazado">Rechazar<', 'data-consent="rechazado">Decline<'),
    ('data-consent="aceptado">Aceptar<', 'data-consent="aceptado">Accept<'),
]


def _contact_buttons(p, wa_href, email_subject, email_first, email_label):
    wa = (f'<a class="btn {{cls}}" href="{wa_href}"{_EXT}><svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-chat"/></svg>'
          f'Escríbeme por WhatsApp{_NEW_TAB}</a>')
    linkedin = (f'<a class="btn btn-outline" href="https://www.linkedin.com/in/luisvicenciodesign"{_EXT}><svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-user"/></svg>'
                f'LinkedIn{_NEW_TAB}</a>')
    buttons = [wa.replace('{cls}', 'btn-outline' if email_first else 'btn-primary')]
    # Correo solo en las landings que lo piden (email_subject='' agrega el botón sin asunto)
    if email_subject is not None:
        href = f'mailto:{EMAIL}' + (f'?subject={quote(email_subject)}' if email_subject else '')
        email = (f'<a class="btn {"btn-primary" if email_first else "btn-outline"}" href="{href}"><svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-mail"/></svg>'
                 f'{email_label or EMAIL}</a>')
        buttons.insert(0 if email_first else 1, email)
    buttons.append(linkedin)
    return ''.join(f'          {b}\n' for b in buttons)


def fill(template, values):
    """Reemplaza {clave} por su valor sin interpretar otras llaves del HTML."""
    return re.sub(r'\{(\w+)\}', lambda m: values.get(m.group(1), m.group(0)), template)


# ---- Mayúscula en cada palabra solo en los títulos de tarjetas (los títulos de sección quedan como oración) ----
_MINOR = {'y', 'e', 'o', 'u', 'de', 'del', 'a', 'al', 'en', 'el', 'la', 'los', 'las', 'para', 'con', 'por', 'sin',
          'and', 'or', 'for', 'of', 'the', 'to', 'an', 'in', 'on', 'with', 'by'}  # también inglés (en/)


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


# ---- Imágenes WebP con srcset (las genera tools/generador/webp.py en img/webp/; los JPG/PNG quedan como fuente) ----
SRC_ROOT = HERE.parent.parent
_IMG = re.compile(r'<img\b([^>]*?)\ssrc="((?:\.\./)*|/)?img/((?:proyectos|marca|collage)/[^"]+)\.(?:jpe?g|png)"([^>]*)>')
# Ancho con que se muestra cada imagen según su clase (el resto: media pantalla en escritorio, ancho completo en móvil)
_SIZES = [('lab-img-half', '(max-width: 47.99em) 92vw, min(46vw, 45.75rem)'), ('lab-img', '(max-width: 91.5rem) 96vw, 91.5rem'), ('v2-hero-bg', '100vw'), ('pl-hero-bg', '100vw'), ('ideas-item', '(max-width: 40em) 45vw, 22vw'), ('brand-logo', '120px'),
          ('svc-card-img', '(max-width: 53.75em) 92vw, 46vw'), ('folio-photo', '(max-width: 40em) 150vw, 50vw')]
_SIZES_DEFAULT = '(max-width: 53.75em) 92vw, 46vw'


def _webp(html):
    def swap(m):
        before, prefix, rel, after = m.group(1), m.group(2) or '', m.group(3), m.group(4)
        # Solo <nombre>-<ancho>.webp (evita tomar las de otra imagen cuyo nombre empieza igual, p. ej. luis-vicencio-hombros)
        name = rel.rsplit('/', 1)[-1]
        files = sorted((f for f in SRC_ROOT.glob(f'img/webp/{rel}-*.webp') if re.fullmatch(re.escape(name) + r'-\d+', f.stem)),
                       key=lambda f: int(f.stem.rsplit('-', 1)[1]))
        if not files:
            return m.group(0)  # sin WebP generado: se deja el original
        attrs = before + after
        sizes = next((v for k, v in _SIZES if k in attrs), _SIZES_DEFAULT)
        srcset = ', '.join(f'{prefix}img/webp/{rel}-{f.stem.rsplit("-", 1)[1]}.webp {f.stem.rsplit("-", 1)[1]}w' for f in files)
        return f'<img{before} src="{prefix}img/webp/{rel}-{files[-1].stem.rsplit("-", 1)[1]}.webp" srcset="{srcset}" sizes="{sizes}"{after}>'
    return _IMG.sub(swap, html)


# ---- URLs sin .html: enlaces, canonical, og:url y JSON-LD apuntan a /pagina en vez de /pagina.html ----
# (.htaccess sirve pagina.html para /pagina y redirige con 301 las direcciones antiguas con .html)
_URL_ABS = re.compile(r'(https://luisdesign\.cl/)([^\s"\'<>#?]*?)\.html')
_URL_REL = re.compile(r'(href=")((?!https?:|mailto:|tel:|//)[^"#?]*?)\.html')


def _sin_html(ruta, absoluta=False):
    """sobre-mi → sobre-mi; proyectos/index → proyectos/; index → ./ (o la raíz si es absoluta)."""
    if ruta == 'index' or ruta.endswith('/index'):
        ruta = ruta[:-len('index')]
        return ruta if (ruta or absoluta) else './'
    return ruta


def _urls_limpias(html):
    html = _URL_ABS.sub(lambda m: m.group(1) + _sin_html(m.group(2), True), html)
    return _URL_REL.sub(lambda m: m.group(1) + _sin_html(m.group(2)), html)


EN_PAGES = ('index.html', 'blog.html', 'noticias/', 'sobre-mi.html')


def _lang_switch(path, lang):
    """Selector ES / EN del encabezado. La versión en inglés existe para el inicio y las noticias; el resto enlaza al inicio en inglés."""
    es_path = path[3:] if path.startswith('en/') else path
    en_path = 'en/' + es_path if es_path in ('index.html', 'blog.html', 'sobre-mi.html') or es_path.startswith('noticias/') else 'en/index.html'
    carpeta = posixpath.dirname(path) or '.'
    es_href = posixpath.relpath(es_path, carpeta)
    en_href = posixpath.relpath(en_path, carpeta)
    es_act = ' aria-current="true"' if lang != 'en' else ''
    en_act = ' aria-current="true"' if lang == 'en' else ''
    return (f'<nav class="lang-switch" aria-label="Idioma / Language">'
            f'<a href="{es_href}" lang="es" hreflang="es"{es_act}>ES</a><span aria-hidden="true">/</span>'
            f'<a href="{en_href}" lang="en" hreflang="en"{en_act}>EN</a></nav>')


# Popup de contacto (Conversemos): está en todas las páginas que cargan css/inicio.css
DIALOGO_CONTACTO = '''      <dialog class="pl-dialog" id="pl-conversemos" aria-labelledby="pl-dialog-title">
        <div class="pl-dialog-grid">
          <div class="pl-dialog-lead">
            <h2 class="pl-dialog-title" id="pl-dialog-title"><mark class="pl-mark">¡Hablemos</mark> <br>de tu <br>proyecto!</h2>
            <p class="pl-dialog-lead-text">Agendemos una reunión para que hablemos de lo que está pasando con tu marca y hacia dónde la quieres llevar. El presupuesto viene después de conversar.</p>
          </div>
          <div class="pl-dialog-body">
            <div class="pl-dialog-head">
              <button class="pl-dialog-close" type="button" data-close aria-label="Cerrar">&times;</button>
            </div>
            <section class="ag" id="pl-agenda" data-endpoint="{p}contacto/agenda.php" aria-label="Agendar una reunión" hidden>
              <div class="ag-cab" data-cab>
                <div class="ag-barra">
                  <button class="ag-flecha" type="button" data-atras aria-label="Volver" hidden>&#8249;</button>
                  <div class="pasos ag-puntos" data-paso role="img" aria-label="Paso 1 de 3"><span class="is-actual"></span><span></span><span></span></div>
                </div>
                <p class="ag-cab-fijo">Agendemos meet</p>
                <h3 class="ag-cab-titulo" data-titulo>Elige un día</h3>
                <p class="ag-zona">20 min · Google Meet · hora de Chile</p>
              </div>
              <div class="ag-mes-vista" data-vista="semana">
                <p class="ag-nota" data-nota role="status" hidden></p>
                <div class="ag-nav">
                  <button class="ag-flecha" type="button" data-mes="-1" aria-label="Mes anterior">&#8249;</button>
                  <p class="ag-titulo" aria-live="polite"></p>
                  <button class="ag-flecha" type="button" data-mes="1" aria-label="Mes siguiente">&#8250;</button>
                </div>
                <div class="ag-semana-dias" data-sem aria-hidden="true"></div>
                <div class="ag-grid" data-grid></div>
              </div>
              <div class="ag-horas-vista" data-vista="horas" hidden>
                <div class="ag-horas" data-horas></div>
              </div>
              <form class="pl-form ag-form" id="ag-form" data-vista="datos" hidden>
                <div class="pl-field"><input id="ag-name" name="nombre" type="text" autocomplete="name" required maxlength="100" placeholder=" "><label for="ag-name">Nombre</label></div>
                <div class="pl-field"><input id="ag-mail" name="correo" type="email" autocomplete="email" required maxlength="150" placeholder=" "><label for="ag-mail">Correo</label></div>
                <div class="pl-field"><textarea id="ag-msg" name="mensaje" maxlength="2000" rows="2" placeholder=" "></textarea><label for="ag-msg">Cuéntame de tu proyecto (opcional)</label></div>
                <div class="pl-hp" aria-hidden="true"><label for="ag-web">No completes este campo</label><input id="ag-web" name="web" type="text" tabindex="-1" autocomplete="off"></div>
                <label class="pl-check"><input type="checkbox" name="consentimiento" value="1" required><span>Acepto que usen mis datos para agendar la reunión en Google Calendar. Lo explico en la <a href="{p}privacidad.html">política de privacidad</a>.</span></label>
                <button class="btn btn-primary" type="submit">Confirmar reunión</button>
                <p class="pl-form-note" data-aviso role="status"></p>
              </form>
              <div class="ag-listo" data-vista="listo" tabindex="-1" hidden>
                <p class="ag-listo-titulo">Reunión agendada</p>
                <p class="ag-listo-texto" data-listo></p>
              </div>
              <div class="ag-pie">
                <button class="ag-mensaje" type="button" data-a-form>o solo envíame un mensaje</button>
                <div class="ag-redes"><a class="pl-linkedin" href="https://www.linkedin.com/in/luisvicenciodesign" rel="noopener noreferrer" target="_blank" aria-label="LinkedIn (se abre en una pestaña nueva)"><svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-linkedin"/></svg></a><a class="pl-linkedin" href="https://wa.me/56958217041" rel="noopener noreferrer" target="_blank" aria-label="WhatsApp (se abre en una pestaña nueva)"><svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-whatsapp"/></svg></a></div>
              </div>
            </section>
            <form class="pl-form" id="pl-form" data-endpoint="{p}contacto/guardar.php" method="dialog" aria-describedby="pl-form-note">
              <button class="ag-flecha pl-form-atras" type="button" data-a-agenda aria-label="Volver a la agenda" hidden>&#8249;</button>
              <h3 class="ag-cab-titulo">Escríbeme</h3>
              <div class="pl-field"><input id="pl-name" name="nombre" type="text" autocomplete="name" required maxlength="100" placeholder=" " autofocus><label for="pl-name">Nombre</label></div>
              <div class="pl-field"><input id="pl-mail" name="correo" type="email" autocomplete="email" required maxlength="150" placeholder=" "><label for="pl-mail">Correo</label></div>
              <div class="pl-field"><textarea id="pl-msg" name="mensaje" required maxlength="2000" rows="4" placeholder=" "></textarea><label for="pl-msg">Mensaje</label></div>
              <div class="pl-hp" aria-hidden="true"><label for="pl-web">No completes este campo</label><input id="pl-web" name="web" type="text" tabindex="-1" autocomplete="off"></div>
              <label class="pl-check"><input type="checkbox" name="consentimiento" value="1" required><span>Acepto que guarden mi nombre, correo y mensaje para responderme. Lo explico en la <a href="{p}privacidad.html">política de privacidad</a>.</span></label>
              <div class="pl-form-acciones">
                <div class="ag-redes"><a class="pl-linkedin" href="https://www.linkedin.com/in/luisvicenciodesign" rel="noopener noreferrer" target="_blank" aria-label="LinkedIn (se abre en una pestaña nueva)"><svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-linkedin"/></svg></a><a class="pl-linkedin" href="https://wa.me/56958217041" rel="noopener noreferrer" target="_blank" aria-label="WhatsApp (se abre en una pestaña nueva)"><svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-whatsapp"/></svg></a></div>
                <button class="btn btn-primary" type="submit">Enviar</button>
              </div>
              <p class="pl-form-note" id="pl-form-note" role="status"></p>
            </form>
          </div>
        </div>
      </dialog>
'''


def page(path, title, desc, body, current=None, contact=True, cta_title=None, cta_lead=None, ogtype='website',
         noindex=False, absolute=False, html_class='motion', canonical=None, extra_css=None, wa_href=None, email_subject=None,
         email_first=False, email_label=None, lang='es', alternates=None, og_image=None, og_alt=None, jsonld=None, ab=None):
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
        # Una hoja extra o varias (lista), en orden
        'extra_css': ''.join(f'  <link rel="stylesheet" href="{p}{c}">\n' for c in ([extra_css] if isinstance(extra_css, str) else extra_css or [])),
        'contact_href': '#contacto' if contact else home + '#contacto',
        'gtm_id': GTM_ID,
        'ga_id': GA_ID,
        'clarity_id': CLARITY_ID,
        'lang_switch': _lang_switch(path, lang),
        'sobre_href': p + ('en/sobre-mi.html' if lang == 'en' else 'sobre-mi.html'),
        'blog_href': p + ('en/blog.html' if lang == 'en' else 'blog.html'),
        # Página de proyectos (solo en español; en inglés sigue la sección de la home)
        'proyectos_href': home + '#proyectos' if lang == 'en' else p + 'proyectos/index.html',
        'email': EMAIL,
        'cur_noticias': ' aria-current="page"' if current == 'noticias' else '',
        # Servicios solo existe en español: en las páginas en inglés no aparece en el menú
        'nav_servicios': '' if lang == 'en' else f'        <a href="{p}servicios.html"' + (' aria-current="page"' if current == 'servicios' else '') + '>Servicios</a>\n',
        'cur_proyectos': ' aria-current="page"' if current == 'proyectos' else '',
        'cur_sobre': ' aria-current="page"' if current == 'sobre' else '',
        'cur_privacidad': ' aria-current="page"' if current == 'privacidad' else '',
        'cta_title': cta_title or CTA_TITLE, 'cta_lead': cta_lead or CTA_LEAD,
        'contact_buttons': _contact_buttons(p, wa_href or WA_HREF, email_subject, email_first, email_label),
        # Prueba A/B de la landing de inicio (js/ab.js): se carga antes de pintar para evitar parpadeos
        'ab_script': f'  <script src="{p}js/ab.js" data-variante="{ab}"></script>\n' if ab else '',
        'html_lang': 'en' if lang == 'en' else 'es-CL', 'og_locale': 'en_US' if lang == 'en' else 'es_CL',
        # Versiones en otros idiomas (las páginas de producto y proyectos se eliminaron; ver noticias)
        # Imagen para compartir (1200 × 630, en img/og/) y datos estructurados (JSON-LD, bloque de datos que la CSP no ejecuta)
        'og_image': SITE + (og_image or OG_DEFAULT), 'og_alt': og_alt or OG_ALT,
        'jsonld': ''.join('  <script type="application/ld+json">' + json.dumps(d, ensure_ascii=False).replace('</', '<\\/') + '</script>\n' for d in (jsonld or [])),
        'alternates': ''.join(f'  <link rel="alternate" hreflang="{h}" href="{SITE}{u}">\n' for h, u in (alternates or {}).items()),
    }
    hojas = [extra_css] if isinstance(extra_css, str) else extra_css or []
    values['dialogo'] = fill(DIALOGO_CONTACTO, values) if 'css/inicio.css' in hojas else ''
    chrome = [fill(HEAD, values), fill(CONTACT, values) if contact else '', fill(FOOT, values)]
    if lang == 'en':
        for es, en in EN_CHROME:
            chrome = [c.replace(es, en) for c in chrome]
        # En inglés, "Digital product" apunta a la versión en inglés
    html = chrome[0] + fill(body, values) + chrome[1] + chrome[2]
    html = _urls_limpias(_webp(_card_titles(html)))
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding='utf-8')
    print('ok', path)


def fragment(name):
    """Contenido de una página guardado tal cual en fragmentos/ (páginas sin datos compartidos)."""
    return (HERE / 'fragmentos' / name).read_text(encoding='utf-8')


env = {'page': page, 'fragment': fragment, 'EMAIL': EMAIL, 'SITE': SITE, 'quote': quote, '__name__': 'luisdesign_pages'}
for script in sorted((HERE / 'pages').glob('*.py')):
    exec(compile(script.read_text(encoding='utf-8'), str(script), 'exec'), env)
