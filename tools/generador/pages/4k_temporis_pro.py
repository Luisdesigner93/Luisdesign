# Caso Temporis Pro (2026, Bytequest): marca y definición de producto de una plataforma de inteligencia operacional industrial.
# Composición editorial igual a LAB*502 y Yomecontrolo (Figma «Portfolio», frame Temporis Pro): título grande, rol y empresa,
# imágenes a lo ancho, pares de imágenes y párrafos centrados. Usa las clases lab-* de css/inicio.css (variantes lab-*-tp).
# Textos: entregados por Luis en el diseño.
_tp = next(pr for pr in PROJECTS if pr['slug'] == 'temporis-pro')
_tp_img = {im['src'].rsplit('/', 1)[1].rsplit('.', 1)[0]: im for im in _tp['images']}


def _tp_fig(key, cls='', lazy=True, mitad=False):
    # lab-img / lab-img-half le indican a build.py el ancho real para elegir el tamaño WebP adecuado
    im = _tp_img.get(key)
    if not im:
        return ''
    return f'\n      <figure class="lab-fig{(" " + cls) if cls else ""}">{img_tag(im, "lab-img-half" if mitad else "lab-img", lazy=lazy)}</figure>'


def _tp_par(a, b, cls):
    """Dos imágenes lado a lado (en móvil, una bajo la otra). cls fija la proporción de las columnas."""
    return f'\n      <div class="lab-pair lab-pair-tp {cls}">' + _tp_fig(a, mitad=True) + _tp_fig(b, mitad=True) + '\n      </div>'


def _tp_text(html):
    return f'\n      <div class="lab-text">{html}</div>'


_tp_chips = ''.join(f'<li>{t}</li>' for t in _tp['tags'])
_tp_body = f'''    <section class="lab-head" aria-labelledby="page-title">
      <div class="lab-wide">
        <ol class="breadcrumb" aria-label="Ruta"><li><a href="{{home}}">Inicio</a></li><li><a href="{{p}}proyectos/index.html">Proyectos</a></li><li aria-current="page">{_tp['title']}</li></ol>
        <h1 class="lab-title" id="page-title">Temporis Pro</h1>
        <p class="lab-lead">De datos dispersos a una operación conectada. Unificando dos soluciones para construir una nueva plataforma industrial.</p>
        <div class="lab-meta lab-meta-tp">
          <dl class="lab-facts">
            <div><dt>Rol:</dt><dd>{_tp['role']}</dd></div>
            <div><dt>Empresa:</dt><dd>{_tp['client']}</dd></div>
          </dl>
          <div class="lab-meta-side">
            <ul class="case-chips" aria-label="Disciplinas">{_tp_chips}</ul>
          </div>
        </div>
      </div>
    </section>

    <article class="lab-case lab-wide" aria-label="Detalle del caso">''' + _tp_fig('01-portada', lazy=False) + _tp_text(
    '<p>Temporis Pro nace de la integración de dos softwares y servicios que ya estaban en funcionamiento. La nueva oferta requería una '
    'identidad propia y una definición de producto capaz de unificar sus funcionalidades y proyectar su evolución.</p>'
    '<p>¿Cómo construir un sistema capaz de relacionar la información de una operación industrial y convertirla en una herramienta para '
    'gestionar su desempeño?</p>'
    '<p>El desafío no consistía únicamente en visualizar indicadores, sino en conectar los elementos que componen una operación: personas, '
    'máquinas, puestos de trabajo, productos, procesos, turnos y recursos.</p>'
    '<p>La exploración de usuarios y mercado permitió identificar problemas de fragmentación de información, baja visibilidad operacional y '
    'dificultades para conectar las decisiones de gestión con lo que ocurre en planta.</p>'
    ) + _tp_fig('02-mapa') + _tp_fig('03-wireframes') + _tp_fig('04-logo-construccion') + _tp_text(
    '<p>Desde marca, desarrollé el rebranding de Temporis Pro, construyendo una nueva identidad visual y un lenguaje de comunicación para '
    'representar y posicionar la oferta integrada.</p>'
    '<p>Desde producto, trabajé en la definición de una plataforma concebida como un Sistema Conductor Operacional, capaz de conectar '
    'información, priorizar eventos y coordinar acciones entre producción, mantenimiento y gestión.</p>'
    ) + _tp_fig('05-web-plataforma') + _tp_par('06-tarjetas', '07-lanyard', 'lab-pair-tp-a') + _tp_fig('08-paleta') + _tp_fig('09-tipografia') + _tp_par(
    '10-login', '11-logotipos', 'lab-pair-tp-b') + '\n      <div class="lab-split lab-split-tp">' + _tp_text(
    '<p>A partir de una propuesta tecnológica del líder técnico basada en un modelo de nodos, colaboré con desarrollo en su comprensión '
    'conceptual y en la representación de los componentes y relaciones de una operación industrial.</p>'
    '<p>Este trabajo se tradujo en una arquitectura funcional, flujos de experiencia e interfaces para configurar plantas, gestionar recursos, '
    'registrar producción y dar seguimiento a problemas. También participé en la organización y priorización del backlog y la planificación por etapas.</p>'
    '<p>El resultado fue una nueva identidad de marca y una definición integral de producto. El proyecto avanzó en estrategia y diseño, sin '
    'llegar a implementación productiva ni validación formal en terreno.</p>'
    ) + _tp_fig('12-portatil') + '\n      </div>' + _tp_par('13-web-monitor', '14-tablet', 'lab-pair-tp-c') + _tp_fig('15-monitor') + '''
    </article>
'''

_tp_desc = 'Caso de estudio: rebranding y definición de producto de Temporis Pro, una plataforma B2B de inteligencia operacional industrial de Bytequest.'
page('proyectos/temporis-pro.html', 'Temporis Pro: marca y producto para una plataforma industrial · Luis Vicencio',
     _tp_desc, current='proyectos', ogtype='article', contact=False, html_class='motion inicio caso', extra_css=['css/inicio.css'],
     **case_seo(_tp, _tp_desc), body=_tp_body + case_nav(_tp))
