# Página de Servicios. Estructura y textos: «Luis design - Presentación de servicios» (PDF). Estilos: css/landing-b.css.
_lb_casos = ['yomecontrolo', 'bowraps', 'temporis-pro', 'sustentando', 'fuchi-chao', 'khronos']
_LB_METODO = {'comprender': (218, 223), 'identificar': (217, 223), 'disenar': (240, 210), 'construir': (229, 206)}
_lb_pasos = [
    ('01', 'Comprender', 'comprender', 'Conozco el negocio, su contexto, sus objetivos, clientes y forma de operar. Busco entender qué está ocurriendo y qué factores influyen en sus desafíos actuales.'),
    ('02', 'Identificar', 'identificar', 'Analizo las oportunidades de negocio, detecto brechas y reconozco dónde el branding y el diseño de producto pueden generar valor. Definimos prioridades y objetivos para orientar el trabajo.'),
    ('03', 'Diseñar', 'disenar', 'Transformo las oportunidades identificadas en estrategias, conceptos y soluciones. Desarrollo propuestas que conectan los objetivos del negocio con las necesidades de las personas.'),
    ('04', 'Construir', 'construir', 'Preparo las soluciones para su producción e implementación, desarrollando recursos gráficos, prototipos y especificaciones. Coordino con proveedores, desarrolladores y otros profesionales para llevar los diseños a la práctica.'),
]


def _lb_paso(n, titulo, icono, texto):
    return (f'\n          <li class="lb-paso"><div class="lb-paso-top"><span class="lb-paso-num">{n}</span>'
            f'<img class="lb-icono" src="{{p}}img/metodo/{icono}.png" width="{_LB_METODO[icono][0]}" height="{_LB_METODO[icono][1]}" alt="" loading="lazy"></div>'
            f'<h3>{titulo}</h3><p>{texto}</p></li>')


def _lb_caso(slug):
    pr = next(x for x in PROJECTS if x['slug'] == slug)
    return (f'\n          <li><a href="{{p}}proyectos/{slug}.html">{project_art(pr)}'
            f'<span>{pr["title"]}<svg class="icon" aria-hidden="true"><use href="{{p}}img/icons.svg#i-arrow"/></svg></span></a></li>')


_lb_servicios = SERVICIOS  # Datos en 0_data.py: también los usa el inicio


_lb_iconos_servicio = SERVICIOS_ICONOS


def _lb_servicio(i, titulo, texto, chips):
    check = '<svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-check"/></svg>'
    lista = ''.join(f'<li>{check}<span>{c}</span></li>' for c in chips)
    return (f'\n          <li class="lb-servicio"><span class="lb-servicio-num">0{i}</span><h3>{titulo}</h3><p>{texto}</p>'
            f'<button class="btn lb-agregar" type="button" data-agregar="{titulo}" data-icono="{_lb_iconos_servicio[titulo]}"><span class="lb-agregar-mas" aria-hidden="true">+</span>{check}'
            f'<span data-agregar-txt>Agregar</span><span class="sr-only"> {titulo}</span></button>'
            f'<div class="lb-incluye"><ul id="incluye-{i}" aria-label="Incluye en {titulo}">{lista}</ul>'
            f'<button class="lb-incluye-btn" type="button" aria-controls="incluye-{i}" aria-expanded="true" hidden><span data-incluye-txt>Ver menos</span>'
            '<svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-chevron"/></svg></button></div></li>')


_lb_combos = [
    ('Marca completa', ['Estrategia de marca', 'Identidad de marca']),
    ('Marca y web', ['Estrategia de marca', 'Identidad de marca', 'Páginas web']),
    ('Producto con marca', ['Estrategia de marca', 'Identidad de marca', 'Diseño de producto']),
    ('Todo', [x[0] for x in _lb_servicios]),
]
_lb_combos_html = ''.join(f'<button type="button" data-combo="{"|".join(s)}" aria-pressed="false">{n}</button>' for n, s in _lb_combos)


_lb_cta = '<a class="btn btn-primary" href="#contacto" data-abrir-contacto>Conversemos <svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-arrow"/></svg></a>'

_lb_body = ('''    <section class="lb-sec lb-desafio frame-grid" id="desafio" aria-labelledby="lb-desafio">
      <div class="lb-desafio-grid">
        <h1 id="lb-desafio">Las <br class="lb-br-movil">empresas <br><span class="lb-subraya">evolucionan.</span> <br>Sus desafíos <br>también.</h1>
        <figure class="lb-desafio-img"><img src="{p}img/landing-b/desafio.webp" width="1086" height="1448" alt="" loading="lazy"><i></i><i></i></figure>
      </div>
      <div class="lb-desafio-pie">
        <a class="btn btn-outline lb-desafio-cta" href="#servicios">Seleccionar servicios <svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-arrow"/></svg></a>
        <div class="lb-mono">
          <p>Los mercados cambian, las personas transforman sus expectativas y la tecnología abre nuevas posibilidades.</p>
          <p><em>En ese escenario, las <mark>empresas</mark> necesitan revisar cómo se presentan, cómo se relacionan con sus <mark>clientes</mark> y cómo desarrollan sus <mark>productos y servicios.</mark></em></p>
        </div>
      </div>
    </section>

    <section class="lb-sec lb-propuesta frame-grid" id="propuesta" aria-labelledby="lb-propuesta">
      <div class="lb-propuesta-grid">
        <div class="lb-propuesta-txt">
          <h2 id="lb-propuesta"><span class="lb-subraya">El diseño</span> tiene un papel fundamental en el proceso</h2>
          <a class="pl-scroll lb-propuesta-bajar" href="#servicios" aria-label="Bajar a mis servicios"><span class="noticia-ovalo" aria-hidden="true"></span></a>
        </div>
        <div class="lb-propuesta-der">
          <div class="lb-tarjetas">
            <article class="card"><div class="pl-tarjeta-foto"><img class="pl-tarjeta-img" src="{p}img/webp/proyectos/khronos/02-960.webp" srcset="{p}img/webp/proyectos/khronos/02-480.webp 480w, {p}img/webp/proyectos/khronos/02-960.webp 960w, {p}img/webp/proyectos/khronos/02-1254.webp 1254w" sizes="(min-width: 70em) 45vw, (min-width: 40em) 60vw, 115vw" width="1254" height="1254" alt="Fila de botellas de Cerveza Khronos con etiquetas de colores para cada variedad." loading="lazy"></div><div class="pl-tarjeta-texto glass"><h3 class="pl-post-title">Construir valor <br>y diferenciación.</h3><p class="pl-post-lead">Desarrollar marcas capaces de expresar lo que hace única a una empresa, fortalecer su posicionamiento y conectar con sus audiencias.</p></div></article>
            <article class="card"><div class="pl-tarjeta-foto"><img class="pl-tarjeta-img" src="{p}img/webp/proyectos/yomecontrolo/11-indicadores-669.webp" srcset="{p}img/webp/proyectos/yomecontrolo/11-indicadores-480.webp 480w, {p}img/webp/proyectos/yomecontrolo/11-indicadores-669.webp 669w" sizes="(min-width: 70em) 50vw, (min-width: 40em) 50vw, 92vw" width="669" height="1046" alt="Mano sosteniendo un teléfono con la pantalla «Controla tus indicadores de salud» de Yo Me Controlo." loading="lazy"></div><div class="pl-tarjeta-texto glass"><h3 class="pl-post-title">Diseñar mejores <br>experiencias y soluciones.</h3><p class="pl-post-lead">Crear o evolucionar productos digitales que respondan a necesidades reales, mejoren experiencias y generen nuevas oportunidades para el negocio.</p></div></article>
          </div>
        </div>
      </div>
    </section>

    <section class="lb-sec lb-servicios" id="servicios" aria-labelledby="lb-servicios">
      <div class="lb-servicios-cab">
        <p class="eyebrow-text">Mis servicios</p>
        <h2 id="lb-servicios">¿En qué puedo <br>ayudarte?</h2>
        <p>Elige uno o combina los que necesites.</p>
        <div class="lb-combos" role="group" aria-label="Combinaciones sugeridas">''' + _lb_combos_html + '''</div>
      </div>
      <ol class="lb-servicios-grid">''' + ''.join(_lb_servicio(i, *x) for i, x in enumerate(_lb_servicios, 1)) + '''
      </ol>
      <p class="sr-only" role="status" data-proyecto-aviso></p>
      <div class="lb-proyecto glass" data-proyecto hidden>
        <div class="lb-proyecto-info"><h3>Tu proyecto <br>busca:</h3><strong data-proyecto-nombres></strong></div>
        <button class="lb-proyecto-vaciar" type="button" data-proyecto-vaciar aria-label="Vaciar selección"><svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-close"/></svg></button>
        <a class="btn btn-primary" href="#contacto" data-abrir-contacto data-servicio="">Conversemos <svg class="icon" aria-hidden="true"><use href="{p}img/icons.svg#i-arrow"/></svg></a>
      </div>
    </section>

    <section class="lb-sec lb-proceso" id="proceso" aria-labelledby="lb-proceso">
      <div class="lb-proceso-fijo">
      <div class="lb-proceso-top">
        <p class="eyebrow-text">Cómo trabajo</p>
        <h2 id="lb-proceso">Cada proyecto requiere una aproximación distinta, pero mantengo una forma de trabajo basada en cuatro momentos:</h2>
      </div>
      <ol class="lb-pasos">''' + ''.join(_lb_paso(*x) for x in _lb_pasos) + '''
      </ol>
      </div>
    </section>

    <section class="lb-sec lb-exp frame-grid" id="experiencia" aria-labelledby="lb-exp">
      <div class="lb-exp-txt">
        <h2 id="lb-exp">Diseño para <br><span class="lb-subraya">impulsar</span> <br><span class="lb-tachado">nuevas <br>posibilidades.<img src="{p}img/landing-b/trazo-negocios.svg" width="816" height="225" alt="negocios" loading="lazy"></span></h2>
        <div class="lb-exp-pie">
          <p class="lb-anios"><strong>+8</strong><span>años de <br>experiencia</span></p>
          <p class="lb-mono">He participado en proyectos de distintas industrias, abordando desafíos de marca, comunicación, experiencia y desarrollo de productos digitales.</p>
        </div>
      </div>
      <ul class="lb-casos" aria-label="Proyectos destacados">''' + ''.join(_lb_caso(s) for s in _lb_casos) + '''
      </ul>
    </section>

    <section class="lb-contacto" id="hablemos" aria-labelledby="lb-hablemos">
      <div class="lb-contacto-top frame-grid">
        <img class="lb-contacto-logo" src="{p}img/landing-b/logo-luis.svg" width="750" height="730" alt="" loading="lazy">
        <h2 id="lb-hablemos">¿Quieres <br>saber más? <br><strong>¡Hablemos!</strong></h2>
        <div class="lb-contacto-cta">
          <p>Agendemos una conversación si estás buscando fortalecer tu marca, desarrollar un producto digital o explorar nuevas formas de conectar tu negocio con las personas.</p>
          ''' + _lb_cta + '''
        </div>
      </div>
      <div class="lb-contacto-pie">
        <div>
          <img class="lb-retrato" src="{p}img/marca/luis-vicencio-escena.png" width="1536" height="1024" alt="Retrato de Luis Vicencio con los brazos cruzados, frente a paneles de vidrio y formas verde lima." loading="lazy">
          <p class="lb-nombre">Luis Vicencio</p>
          <p class="lb-cargo">Branding estratégico y diseño de producto.</p>
          <ul class="lb-datos">
            <li><a href="mailto:{email}">{email}</a></li>
            <li><a href="https://wa.me/56958217041" rel="noopener noreferrer" target="_blank">+56 9 5821 7041</a></li>
            <li><a href="https://luisdesign.cl">www.luisdesign.cl</a></li>
          </ul>
        </div>
      </div>
    </section>
''')

page('servicios.html', 'Servicios de branding, identidad, producto digital y páginas web · Luis Vicencio',
     'Branding estratégico y diseño de productos digitales para empresas y equipos en crecimiento. Más de 8 años de experiencia. Agendemos una conversación.',
     body=_lb_body, current='servicios', contact=False, html_class='motion inicio lb', extra_css=['css/inicio.css', 'css/landing-b.css'],
     og_image='img/og/inicio.jpg', og_alt='Línea de productos Fuchi Chao: detergente, eliminador de olores y jabón anti olores')
