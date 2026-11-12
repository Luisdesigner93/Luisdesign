# Caso LAB*502 (2023), Iquique. Composición editorial propia (Figma «Portfolio», frame LAB502, nodo 7:47):
# encabezado con título grande, imágenes a lo ancho y párrafos centrados entre ellas.
# Se mantiene de la plantilla de casos: ruta (breadcrumb), disciplinas, año y la navegación entre proyectos.
_lab = next(pr for pr in PROJECTS if pr['slug'] == 'lab502')
_lab_img = {im['src'].rsplit('/', 1)[1].rsplit('.', 1)[0]: im for im in _lab['images']}


def _lab_fig(key, cls='', lazy=True):
    """Imagen a lo ancho; si aún no existe (pendiente de exportar desde Figma) no se muestra."""
    im = _lab_img.get(key)
    if not im:
        return ''
    return f'\n      <figure class="lab-fig{(" " + cls) if cls else ""}">{img_tag(im, lazy=lazy)}</figure>'


def _lab_text(html):
    return f'\n      <div class="lab-text">{html}</div>'


_chips = ''.join(f'<li>{t}</li>' for t in _lab['tags'])
_lab_body = f'''    <section class="lab-head" aria-labelledby="page-title">
      <div class="lab-wide">
        <ol class="breadcrumb" aria-label="Ruta"><li><a href="{{home}}">Inicio</a></li><li><a href="{{p}}proyectos/index.html">Proyectos</a></li><li aria-current="page">{_lab['title']}</li></ol>
        <h1 class="lab-title" id="page-title">Lab quinientos dos<span class="sr-only"> (LAB*502)</span></h1>
        <p class="lab-lead">Construir una marca para acercar las experiencias artísticas análogas al norte de Chile.</p>
        <div class="lab-meta">
          <ul class="case-chips" aria-label="Disciplinas">{_chips}</ul>
          <p class="lab-year"><span class="sr-only">Año: </span>{_lab['year']}</p>
        </div>
      </div>
    </section>

    <article class="lab-case lab-wide" aria-label="Detalle del caso">''' + _lab_fig('01-portada', lazy=False) + _lab_text(
    '<p>Lab*502 nació como un laboratorio fotográfico y editorial en Iquique, con una inquietud que iba más allá de ofrecer servicios fotográficos: '
    'acercar las experiencias artísticas, recuperar los oficios análogos y generar nuevos espacios de exploración cultural en el norte del país.</p>'
    '<p>El desafío fue encontrar una identidad capaz de representar esa ambición y, al mismo tiempo, darle estructura a una propuesta que reunía '
    'distintas disciplinas y oportunidades de negocio.</p>') + _lab_fig('02-collage') + _lab_fig('03-logotipos') + _lab_fig('04-estrategia') + _lab_fig('05-reticula') + _lab_text(
    '<p>El proceso comenzó por entender qué quería construir Lab*502, a quiénes buscaba convocar y qué lugar podía ocupar dentro de su entorno. '
    'A partir de ese trabajo definimos un posicionamiento que conectaba fotografía, experimentación, comunidad y territorio.</p>'
    '<p>Uno de los pasos importantes fue organizar su propuesta comercial en distintas líneas de servicio: fotografía corporativa, editorial e imprenta, '
    'talleres y encuentros, y restauración fotográfica. Esta arquitectura permitió dar mayor claridad a su oferta y construir una marca capaz de '
    'representar todas estas actividades sin perder coherencia.</p>') + '\n      <div class="lab-pair">' + _lab_fig('06-servicios') + _lab_fig('07-isotipo') + '\n      </div>' + f'''
      <div class="lab-split{"" if "08-foto" in _lab_img else " lab-split-solo"}">''' + _lab_fig('08-foto') + _lab_text(
    '<p>La dirección creativa tomó como punto de partida la luz del desierto. Una idea que conectaba la fotografía con el paisaje del norte, '
    'sus colores y su sensibilidad artística. Desde ahí desarrollamos un lenguaje visual experimental, contemporáneo y rupturista, que se alejara '
    'de los códigos tradicionales de los laboratorios fotográficos.</p>') + '''
      </div>''' + _lab_fig('09-reduccion') + _lab_text(
    '<p>El resultado fue un sistema de identidad flexible, construido alrededor del número 502 y un símbolo inspirado en la captura de la luz. '
    'Una identidad que podía desplegarse en distintos formatos, desde sus aplicaciones editoriales y comunicación digital hasta sus espacios físicos '
    'y experiencias.</p>') + _lab_fig('10-arquitectura') + _lab_fig('11-logo-horizontal', 'lab-fig-logo') + _lab_fig('12-historias') + _lab_fig('13-publicaciones', 'lab-fig-plain') + _lab_fig('14-turismo') + _lab_text(
    '<p>Más que construir una identidad visual, el proyecto buscó darle forma a una propuesta cultural: una marca que invitara a explorar, '
    'aprender y vivir el arte desde el norte de Chile.</p>') + _lab_fig('15-sitio-web') + _lab_fig('16-talleres') + '''
    </article>
'''

_lab_desc = 'Caso de estudio: posicionamiento, líneas de servicio y sistema de identidad de LAB*502, un laboratorio fotográfico y editorial en Iquique.'
page('proyectos/lab502.html', 'LAB*502: una marca para acercar las experiencias artísticas análogas al norte de Chile · Luis Vicencio',
     _lab_desc, current='proyectos', ogtype='article', contact=False, html_class='motion inicio caso', extra_css=['css/inicio.css'],
     **case_seo(_lab, _lab_desc), body=_lab_body + case_nav(_lab))
