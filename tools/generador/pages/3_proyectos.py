# Listado de proyectos con estructura de índice fijo + secciones (referencia: mecha-xyz), con el design system Frost Glass.


def showcase_item(n, pr):
    num = f'{n:02d}'
    # Una sola imagen por proyecto: la primera de su lista.
    if pr['images']:
        fig = f'<figure>{img_tag(pr["images"][0])}</figure>'
    else:
        # EDITAR: reemplazar por la imagen del proyecto
        fig = '<figure><div class="media-ph" role="img" aria-label="Imagen pendiente"><svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-image"/></svg>Imagen pendiente</div></figure>'
    proposal = '<span class="tag tag-value">Propuesta</span>' if pr.get('proposal') else ''
    status = f'<div><dt>Estado</dt><dd>{pr["status"]}</dd></div>' if pr.get('status') else ''
    return f'''
        <article class="showcase-item" id="p-{pr['slug']}" data-cats="{' '.join(pr['cats'])}" aria-labelledby="t-{pr['slug']}">
          <div class="showcase-info">
            <p class="showcase-meta"><span class="numtag">{num}</span>{proposal}<span>{pr['kind']}</span><span>{pr['year']}</span><span>{' · '.join(t for t in pr['tags'] if t != 'Propuesta')}</span></p>
            <h2 class="showcase-title" id="t-{pr['slug']}">{pr['title']}</h2>
            <div class="showcase-body">
              <div class="showcase-text">
                <p>{pr['summary']}</p>
              </div>
            </div>
            <dl class="showcase-facts">
              <div><dt>Rol</dt><dd>{pr['role']}</dd></div>
              <div><dt>Cliente</dt><dd>{pr['client']}</dd></div>
              <div><dt>Año</dt><dd>{pr['year']}</dd></div>{status}
            </dl>
            <a class="link-arrow showcase-link" href="proyectos/{pr['slug']}.html">Ver caso completo<span class="sr-only">: {pr['title']}</span> <svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg></a>
          </div>
          <div class="collage">
            {fig}
          </div>
        </article>
'''


_index = ''.join(f'''
              <li data-cats="{' '.join(pr['cats'])}"><a href="#p-{pr['slug']}"><span class="showcase-num">{i:02d}</span><span class="showcase-name">{pr['title']}</span><span class="showcase-progress" aria-hidden="true"></span></a></li>'''
                 for i, pr in enumerate(PROJECTS, 1))

# Logofolio: misma estructura de mosaicos que la sección "Metodología" de AuditorWeb.
_logos = [('luy design', 'img/marca/logo-luy-cuadrado.png'), ('Bowraps', None)] + [(None, None)] * 7


def _logo_cell(name, src):
    if src:
        return f'''
        <li class="logo-cell"><img src="{src}" width="560" height="560" alt="Logotipo {name}" loading="lazy" decoding="async"><span>{name}</span></li>'''
    # EDITAR: reemplazar por el logo (idealmente SVG o PNG con fondo transparente) y su nombre
    return f'''
        <li class="logo-cell is-pending"><svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-image"/></svg><span>{name + ' · ' if name else ''}Logo pendiente</span></li>'''


# Portada "PORTAFOLIO": palabra gigante detrás del retrato y su contorno por delante (referencia: portada de portafolio editorial).
_word = 'PORTAFOLIO'
_letters = ''.join(f'<span>{c}</span>' for c in _word)
_folio = f'''    <!-- PORTAFOLIO: palabra gigante, retrato al centro y datos en las esquinas -->
    <section class="panel folio-hero" aria-labelledby="folio-title">
      <h2 class="folio-word" id="folio-title"><span class="sr-only">Portafolio</span><span class="folio-letters" aria-hidden="true">{_letters}</span></h2>
      <img class="folio-photo" src="img/marca/luis-vicencio-hombros.png" width="1145" height="1373" alt="Retrato de Luis Vicencio" decoding="async" fetchpriority="high">
      <div class="folio-word folio-word-line" aria-hidden="true"><span class="folio-letters">{_letters}</span></div>
      <p class="folio-role">Branding · UX/UI · Producto</p>
      <a class="folio-corner folio-next" href="#lista-title" aria-label="Ir a la lista de proyectos"><svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg></a>
      <p class="folio-corner folio-name">Luis Vicencio</p>
    </section>

'''

_logofolio = '''
    <!-- LOGOFOLIO -->
    <section class="panel logofolio" id="logofolio" aria-labelledby="logofolio-title">
      <div class="tile-bg" aria-hidden="true"></div>
      <div class="section-head center">
        <span class="tag tag-eyebrow">Logofolio</span>
        <h2 class="heading" id="logofolio-title">Marcas que empiezan <strong>por un símbolo</strong>.</h2>
        <p class="lead">Una selección de logotipos diseñados para marcas de distintos rubros.</p>
      </div>
      <ul class="logo-grid" role="list" aria-label="Logotipos">''' + ''.join(_logo_cell(n, s) for n, s in _logos) + '''
      </ul>
    </section>
    <section class="panel panel-plain section logofolio-extra" aria-label="Fichas de Logofolio">
      <div class="container">
        <!-- EDITAR: 3 o 4 imágenes de Bowraps en alta desde Behance (behance.net/gallery/142375157/Bowraps-Identidad-de-Marca) -->
        <article class="card logo-feature" id="bowraps" aria-labelledby="bowraps-title">
          <div class="media-ph" role="img" aria-label="Imagen pendiente: identidad de Bowraps"><svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-image"/></svg>Imagen pendiente</div>
          <div class="logo-feature-text">
            <p class="eyebrow-text">2022 · Naming e identidad visual</p>
            <h3 class="card-title" id="bowraps-title">Bowraps</h3>
            <p>Naming e identidad visual para una marca de wraps y bowls frescos, hoy en funcionamiento en Viña del Mar. Propuse un nombre que une sus dos productos y un símbolo que los integra en una sola forma. Fue uno de mis primeros proyectos liderando a otro diseñador. Diseño gráfico en colaboración con Claudio Almeyda Godoy.</p>
          </div>
        </article>
      </div>
    </section>
'''

page('proyectos.html', 'Proyectos · Luis Vicencio',
     'Casos de estudio de branding, packaging, UX/UI y producto digital de Luis Vicencio.',
     current='proyectos', html_class='showcase-page',
     cta_title='¿Tu proyecto es <strong>el siguiente</strong>?',
     body=_folio + '''    <section class="hero-shell" aria-labelledby="lista-title">
      <div class="shell-body frame-grid page-hero">
        <div class="container">
          <ol class="breadcrumb" aria-label="Ruta"><li><a href="./">Inicio</a></li><li aria-current="page">Proyectos</li></ol>
          <span class="tag tag-eyebrow">Proyectos</span>
          <h1 class="display" id="lista-title">Marcas y productos que pasaron <strong>de la idea a la realidad</strong>.</h1>
          <p class="lead">Branding, packaging, experiencias digitales y productos de software. Recorre cada proyecto o entra al caso completo para ver el proceso y los resultados.</p>
          <nav class="filter-tabs" aria-label="Filtrar proyectos por categoría">
            <a href="proyectos.html" data-cat="todos">Todos</a>
            <a href="proyectos.html?cat=marcas" data-cat="marcas">Marcas</a>
            <a href="proyectos.html?cat=producto" data-cat="producto">Producto digital</a>
            <a href="proyectos.html?cat=logofolio" data-cat="logofolio">Logofolio</a>
          </nav>
        </div>
      </div>
    </section>

    <div class="showcase">
      <aside class="showcase-aside" aria-label="Índice de proyectos">
        <div class="showcase-aside-inner">
          <nav class="showcase-index" aria-label="Proyectos">
            <p class="showcase-all"><svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-layers"/></svg>Proyectos</p>
            <ol>''' + _index + '''
            </ol>
          </nav>
        </div>
      </aside>

      <div class="showcase-main">
''' + ''.join(showcase_item(i, pr) for i, pr in enumerate(PROJECTS, 1)) + '''      </div>
    </div>
''' + _logofolio)
