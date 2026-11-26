# Caso Cerveza Khronos (2023): propuesta de rebranding, concepto, identidad y packaging.
# Contenido basado en el brandbook publicado en Behance (behance.net/gallery/231002797/Cerveza-Khronos).
# Composición editorial igual a Temporis Pro, Sustentando y Yomecontrolo: título grande, ficha, imágenes a lo ancho,
# pares de imágenes y párrafos centrados (clases lab-* de css/inicio.css; proporción del par Stout en lab-pair-kh).
_kh = next(pr for pr in PROJECTS if pr['slug'] == 'khronos')
_kh_img = {im['src'].rsplit('/', 1)[1].rsplit('.', 1)[0]: im for im in _kh['images']}


def _kh_fig(key, lazy=True, mitad=False):
    # lab-img / lab-img-half le indican a build.py el ancho real para elegir el tamaño WebP adecuado
    im = _kh_img.get(key)
    if not im:
        return ''
    return f'\n      <figure class="lab-fig">{img_tag(im, "lab-img-half" if mitad else "lab-img", lazy=lazy)}</figure>'


def _kh_par(a, b, cls):
    """Dos imágenes lado a lado con la misma altura (en móvil, una bajo la otra). cls fija la proporción de las columnas."""
    return f'\n      <div class="lab-pair lab-pair-tp {cls}">' + _kh_fig(a, mitad=True) + _kh_fig(b, mitad=True) + '\n      </div>'


def _kh_text(html):
    return f'\n      <div class="lab-text">{html}</div>'


_kh_chips = ''.join(f'<li>{t}</li>' for t in _kh['tags'])
_kh_body = f'''    <section class="lab-head" aria-labelledby="page-title">
      <div class="lab-wide">
        {case_ruta(_kh)}
        <h1 class="lab-title" id="page-title">Cerveza Khronos</h1>
        <p class="lab-lead">Un nombre que encontró su sentido. Buscamos el significado de <em>khronos</em>, tiempo, y lo convertimos en el concepto que guía la marca: tómate el tiempo.</p>
        <div class="lab-meta lab-meta-tp">
          <dl class="lab-facts">
            <div><dt>Rol:</dt><dd>{_kh['role']}</dd></div>
            <div><dt>Empresa:</dt><dd>{_kh['client']}</dd></div>
            <div><dt>Estado:</dt><dd>{_kh['status']}</dd></div>
          </dl>
          <div class="lab-meta-side">
            <ul class="case-chips" aria-label="Disciplinas">{_kh_chips}</ul>
          </div>
        </div>
      </div>
    </section>

    <article class="lab-case lab-wide" aria-label="Detalle del caso">''' + _kh_fig('05', lazy=False) + _kh_text(
    '<p>Khronos nació en 2013 recorriendo ferias y bierfest, antes incluso de producir su propia cerveza. Desde 2015 elabora sus variedades '
    'y las ha mejorado con constancia hasta estandarizar su calidad.</p>'
    '<p>La cervecería ya tenía nombre y una marca en uso, pero el nombre no tenía un significado detrás ni una idea que orientara cómo comunicar. '
    'En ferias y góndolas llenas de etiquetas artesanales parecidas, eso la dejaba sin un argumento propio.</p>'
    '<p>El desafío del rebranding fue darle sentido al nombre y convertirlo en un concepto capaz de direccionar todas las decisiones de la marca.</p>'
    ) + _kh_fig('01') + _kh_text(
    # EDITAR: ajustar la última frase si el camino se eligió por otra razón
    '<p>Antes de definir la identidad, presenté tres caminos visuales distintos para que la cervecería eligiera cómo quería verse. Como la marca '
    'no tenía un concepto detrás, el sentido del nombre fue lo que ayudó a decidir: el camino elegido fue el que mejor contaba el tiempo.</p>'
    '<p>Un reloj de arena que también se lee como la O del nombre: el tiempo queda dentro de la marca.</p>'
    ) + _kh_par('10-simbolo', '11-ilustracion', 'lab-pair-kh-simbolo') + _kh_par('06-logo-vertical', '07-sello', 'lab-pair-tp-c') + _kh_fig('09-tipografia') + _kh_text(
    '<p>La identidad usa el concepto del tiempo para hablar de momentos inolvidables, compartidos y sin apuro. El tagline «Tómate el tiempo» lo '
    'convierte en una invitación directa que se repite en cada pieza: tómate el tiempo de explorar, de disfrutar, de una más.</p>'
    '<p>El logotipo integra el símbolo y tiene versiones para fondos claros, oscuros y de color. Las etiquetas usan un color por variedad '
    '(American Pale Ale, IPA, Golden Ale, Stout, Barley Wine y Berries Pale Ale) con una misma estructura de información, y el sistema se '
    'extiende a las aplicaciones para ferias: stand, stickers y piezas para concursos en redes sociales.</p>'
    ) + _kh_par('02', '04', 'lab-pair-tp-c') + _kh_par('03', '08-etiqueta-stout', 'lab-pair-kh') + '''
    </article>
'''

_kh_desc = 'Caso de estudio: rebranding de Cerveza Khronos, una cervecería artesanal de Chile. Concepto de marca, identidad visual y packaging.'
page('proyectos/khronos.html', 'Cerveza Khronos: propuesta de rebranding, concepto y packaging · Luis Vicencio',
     _kh_desc, current='proyectos', ogtype='article', contact=False, html_class='motion inicio caso', extra_css=['css/inicio.css'],
     **case_seo(_kh, _kh_desc), body=_kh_body + case_nav(_kh))
