# Caso Yomecontrolo (2023 – 2024): estrategia, experiencia y expresión de marca, nueva identidad y UX/UI de la web app del MVP.
# Composición editorial igual a LAB*502 (Figma «Portfolio», frame YMC, nodo 1:114): título grande, imágenes a lo ancho,
# pares de imágenes y párrafos centrados entre ellas. Usa las mismas clases lab-* de css/inicio.css.
# Texto: documentos de research, Brand Compass, experiencia de marca y visión creativa entregados por Luis.
_ym = next(pr for pr in PROJECTS if pr['slug'] == 'yomecontrolo')
_ym_img = {im['src'].rsplit('/', 1)[1].rsplit('.', 1)[0]: im for im in _ym['images']}


def _ym_fig(key, cls='', lazy=True, mitad=False):
    # lab-img / lab-img-half le indican a build.py el ancho real para elegir el tamaño WebP adecuado
    im = _ym_img.get(key)
    if not im:
        return ''
    return f'\n      <figure class="lab-fig{(" " + cls) if cls else ""}">{img_tag(im, "lab-img-half" if mitad else "lab-img", lazy=lazy)}</figure>'


def _ym_par(a, b, cls):
    """Dos imágenes lado a lado (en móvil, una bajo la otra). cls fija la proporción de las columnas."""
    return f'\n      <div class="lab-pair {cls}">' + _ym_fig(a, mitad=True) + _ym_fig(b, mitad=True) + '\n      </div>'


def _ym_text(html):
    return f'\n      <div class="lab-text">{html}</div>'


_ym_chips = ''.join(f'<li>{t}</li>' for t in _ym['tags'])
_ym_body = f'''    <section class="lab-head" aria-labelledby="page-title">
      <div class="lab-wide">
        {case_ruta(_ym)}
        <h1 class="lab-title" id="page-title">Yo me controlo</h1>
        <p class="lab-lead">Software de medicina preventiva. Para vivir más y mejor.</p>
        <div class="lab-meta">
          <ul class="case-chips" aria-label="Disciplinas">{_ym_chips}</ul>
          <p class="lab-year"><span class="sr-only">Año: </span>{_ym['year']}</p>
        </div>
      </div>
    </section>

    <article class="lab-case lab-wide" aria-label="Detalle del caso">''' + _ym_fig('01-logo', lazy=False) + _ym_text(
    '<p>Yomecontrolo es una startup tecnológica chilena del área de la salud. Ofrece packs de exámenes preventivos, emite órdenes médicas '
    'y categoriza a cada paciente según su perfil de riesgo, con una meta clara: ayudar a las personas a vivir más y mejor.</p>'
    '<p>En Chile la salud es reactiva: las enfermedades se descubren tarde y muchas personas no terminan sus tratamientos. Además, '
    'el público confundía la marca con su competencia directa y todavía no lograba conectar con sus usuarios.</p>'
    ) + _ym_fig('02-portada') + _ym_fig('03-proceso') + _ym_text(
    '<p>Un proceso de branding por etapas, en el que cada fase alimenta a la siguiente. Con un Brand Compass fijamos su propósito, '
    'diferencial, personalidad y promesa. El público principal: adultos de 30 a 50 años que gestionan la salud de su familia.</p>'
    ) + _ym_par('04-pulmones', '05-objetivo', 'lab-pair-ymc-a') + _ym_fig('06-research') + _ym_text(
    '<p>El desafío fue separar la marca del peso negativo de ir al médico y convertir el autocuidado en algo amable y cercano.</p>'
    ) + _ym_fig('07-stylescapes') + _ym_text(
    '<p>De la experiencia de marca surgieron dos territorios: «Cuidado conectado», la tecnología como una forma de acercar el '
    'acompañamiento médico a las personas y sus familias, y «La Ruta del Bienestar», el cuidado de la salud como un recorrido donde cada paso cuenta.</p>'
    ) + _ym_fig('08-arquitectura') + _ym_fig('09-paleta') + _ym_text(
    '<p>Una marca que funciona como un asistente clínico: acompaña el cuidado personal y familiar mucho antes de que llegue la enfermedad. '
    'Una personalidad inteligente, confiable y empática, resumida en una idea central: «Yo me controlo, hoy por un mejor mañana».</p>'
    ) + _ym_par('10-telefono-inicio', '11-indicadores', 'lab-pair-ymc-d') + _ym_par('12-ilustraciones', '13-telefono-test', 'lab-pair-ymc-b') + _ym_fig('14-iconos') + _ym_fig('15-publicaciones') + _ym_fig('16-portatil') + _ym_text(
    '<p>Diseñé la web app del MVP de 2024: un recomendador que arma la orden médica según el perfil de cada persona, la solicitud de '
    'exámenes en línea y la calculadora de edad del corazón para medir el riesgo cardiovascular.</p>'
    ) + _ym_fig('17-letrero') + _ym_par('18-credencial', '19-ciclista', 'lab-pair-ymc-c') + _ym_fig('20-historias') + _ym_text(
    '<p>La nueva marca sigue en uso hasta hoy. El MVP no llegó a producción porque la empresa tomó otra dirección de producto, pero la '
    'estrategia, el propósito y la identidad siguen guiando su comunicación.</p>'
    '<p>Este proyecto me mostró que una buena estrategia de marca necesita herramientas de producto para llegar a producción. Por eso me '
    'formé en Product Owner y Scrum, y hoy acompaño las dos etapas.</p>'
    ) + '''
    </article>
'''

_ym_desc = 'Caso de estudio: estrategia de marca, nueva identidad y UX/UI del MVP de Yomecontrolo, una startup chilena de salud preventiva.'
page('proyectos/yomecontrolo.html', 'Yomecontrolo: estrategia de marca, identidad y UX/UI para una startup de salud · Luis Vicencio',
     _ym_desc, current='proyectos', ogtype='article', contact=False, html_class='motion inicio caso', extra_css=['css/inicio.css'],
     **case_seo(_ym, _ym_desc), body=_ym_body + case_nav(_ym))
