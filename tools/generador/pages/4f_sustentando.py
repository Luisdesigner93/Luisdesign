# Caso Sustentando (2022 – hoy): identidad y web, comunicación B2B, diseño para sus servicios, rediseño web y stand Inofood 2026.
# Composición editorial igual a Temporis Pro, LAB*502 y Yomecontrolo: título grande, rol y empresa, imágenes a lo ancho,
# pares de imágenes y párrafos centrados (clases lab-* de css/inicio.css; proporción del par en lab-pair-su).
# Quedan sin usarse 02.jpg, 06.jpg (publicación de LinkedIn) y 03.jpg (plantillas por nivel, retirada por Luis), 04.jpg y 05.png, que repiten el blog y las piezas OTEC de las imágenes nuevas.
_su = next(pr for pr in PROJECTS if pr['slug'] == 'sustentando')
_su_img = {im['src'].rsplit('/', 1)[1].rsplit('.', 1)[0]: im for im in _su['images']}


def _su_fig(key, lazy=True, mitad=False):
    # lab-img / lab-img-half le indican a build.py el ancho real para elegir el tamaño WebP adecuado
    im = _su_img.get(key)
    if not im:
        return ''
    return f'\n      <figure class="lab-fig">{img_tag(im, "lab-img-half" if mitad else "lab-img", lazy=lazy)}</figure>'


def _su_par(a, b, cls):
    """Dos imágenes lado a lado con la misma altura (en móvil, una bajo la otra). cls fija la proporción de las columnas."""
    return f'\n      <div class="lab-pair lab-pair-tp lab-pair-su {cls}">' + _su_fig(a, mitad=True) + _su_fig(b, mitad=True) + '\n      </div>'


def _su_text(html):
    return f'\n      <div class="lab-text">{html}</div>'


_su_chips = ''.join(f'<li>{t}</li>' for t in _su['tags'])
_su_body = f'''    <section class="lab-head" aria-labelledby="page-title">
      <div class="lab-wide">
        {case_ruta(_su)}
        <h1 class="lab-title" id="page-title">Sustentando</h1>
        <p class="lab-lead">De un logotipo a una empresa consolidada en su comunicación. Un aliado de diseño que acompaña a una consultora B2B en cada etapa de su crecimiento.</p>
        <div class="lab-meta lab-meta-tp">
          <dl class="lab-facts">
            <div><dt>Rol:</dt><dd>{_su['role']}</dd></div>
            <div><dt>Empresa:</dt><dd>{_su['client']}</dd></div>
            <div><dt>Relación:</dt><dd>{_su['status']}</dd></div>
          </dl>
          <div class="lab-meta-side">
            <ul class="case-chips" aria-label="Disciplinas">{_su_chips}</ul>
          </div>
        </div>
      </div>
    </section>

    <article class="lab-case lab-wide" aria-label="Detalle del caso">''' + _su_fig('07-stand', lazy=False) + _su_fig('10-web-monitor') + _su_text(
    '<p>Todo partió por entender qué necesitaba Sustentando en ese momento, no por lo que podía ofrecerle.</p>'
    '<p>Sustentando es una consultora chilena que acompaña a empresas en calidad e inocuidad. En 2022 su prioridad era presentarse de forma '
    'profesional: un logotipo, presentaciones comerciales y un sitio web. Diseñé una identidad simple y sólida, pensada como base para lo que vendría.</p>'
    ) + _su_par('13-sello', '14-paleta', 'lab-pair-su-a') + _su_fig('01') + _su_text(
    '<p>A medida que la empresa crecía, fuimos sumando capas de trabajo según lo que su equipo necesitaba.</p>'
    '<p>Primero, una estrategia de comunicación B2B para LinkedIn, con plantillas por nivel para que el equipo publicara de forma constante y consistente. '
    'Luego, el diseño de los materiales que acompañan sus propios servicios: presentaciones, brochures y señalética de seguridad y calidad para sus clientes.</p>'
    '<p>Hoy rediseñamos su sitio web y diseñé su stand para Inofood 2026.</p>'
    ) + _su_fig('09-otec') + _su_par('12-llaveros', '15-curso-haccp', 'lab-pair-su-b') + _su_text(
    '<p>La confianza de sus clientes la gana Sustentando con su servicio; mi trabajo es que ese servicio se vea y se perciba con la calidad que tiene.</p>'
    '<p>Para lograrlo me involucro como un integrante más del equipo: detecto sus necesidades y carencias, y las resuelvo con diseño y comunicación. '
    'El resultado es una empresa consolidada comunicacionalmente, con un valor percibido relevante para sus clientes.</p>'
    '<p>En una consultoría B2B, el cliente decide por la percepción que tiene de un proveedor que todavía no conoce. La comunicación en LinkedIn le ha '
    'traído a Sustentando nuevos clientes, y su equipo sigue confiando en mí como alguien que resuelve lo que necesitan en cada etapa.</p>'
    # EDITAR: pedir a Sustentando una frase corta sobre el trabajo (testimonio)
    ) + _su_fig('11-blog-linkedin') + '''
    </article>
'''

_su_desc = 'Caso de estudio: identidad de marca, sitio web, comunicación B2B y diseño gráfico para Sustentando, desde 2022.'
page('proyectos/sustentando.html', 'Sustentando: identidad, sitio web y comunicación B2B para una consultora · Luis Vicencio',
     _su_desc, current='proyectos', ogtype='article', contact=False, html_class='motion inicio caso', extra_css=['css/inicio.css'],
     **case_seo(_su, _su_desc), body=_su_body + case_nav(_su))
