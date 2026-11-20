# Página de proyectos (proyectos/index.html), enlazada desde «Proyectos» en el menú y el pie.
# Referencia: wunderdogs.co/our-work. Título grande con los filtros por servicio y disciplina debajo,
# y una grilla de tarjetas (imagen, nombre y flecha). Estilos en css/inicio.css (prefijo pj-).

# Casos ocultos en esta página (sus páginas siguen publicadas). Para mostrar uno, quítalo de la lista.
_pj_ocultos = {'bytequest', 'uvenergy', 'auditorweb', 'sustentando', 'botes-salvavidas'}
_pj = [pr for pr in PROJECTS if pr['slug'] not in _pj_ocultos]
_pj_cats = [('marcas', 'Marcas'), ('producto', 'Producto digital')]

# Todas las disciplinas de los casos visibles, de más a menos frecuentes
_pj_conteo = {}
for _pr in _pj:
    for _t in _pr['tags']:
        _pj_conteo[_t] = _pj_conteo.get(_t, 0) + 1
_pj_tags = sorted(_pj_conteo, key=lambda t: (-_pj_conteo[t], t))


def _pj_slug(texto):
    return texto.lower().replace('/', '').replace(' ', '-')


def _pj_btn(grupo, valor, nombre, n):
    return (f'<li><button class="pj-chip" type="button" data-grupo="{grupo}" data-valor="{valor}" aria-pressed="false">'
            f'{nombre}<span class="pj-n">({n})</span></button></li>')


def _pj_over(pr):
    """Capa sobre la imagen (hover, foco o primer toque en móvil): año, «Ver proyecto» y disciplinas.
    Las disciplinas van abajo a la derecha, una sobre otra, de la más angosta (arriba) a la más ancha (abajo);
    la letra es monoespaciada, así que el largo del texto da el ancho.
    aria-hidden: repite datos del caso y el enlace ya se anuncia con el nombre del proyecto."""
    tags = ''.join(f'<span class="pj-over-tag">{t}</span>' for t in sorted(pr['tags'], key=len))
    return (f'<span class="pj-over" aria-hidden="true"><span class="pj-over-year">{pr["year"]}</span>'
            f'<span class="pj-over-bottom"><span class="btn btn-primary pj-over-btn">Ver proyecto<svg class="icon"><use href="{{p}}img/icons.svg#i-arrow"/></svg></span>'
            f'<span class="pj-over-tags">{tags}</span></span></span>')


def _pj_card(pr, i):
    filtros = ' '.join(pr['cats'] + [_pj_slug(t) for t in pr['tags']])
    return f'''
          <li class="pj-item" data-filtros="{filtros}">
            <a class="pj-card" href="{{p}}proyectos/{pr['slug']}.html">
              <figure class="pj-media">{project_art(pr, lazy=i > 2)}{_pj_over(pr)}</figure>
              <span class="pj-name">{pr['title']}<svg class="icon" aria-hidden="true"><use href="{{p}}img/icons.svg#i-arrow"/></svg></span>
            </a>
          </li>'''


_pj_cat_btns = ''.join(_pj_btn('cat', c, nombre, sum(c in pr['cats'] for pr in _pj)) for c, nombre in _pj_cats)
_pj_tag_btns = ''.join(_pj_btn('tag', _pj_slug(t), t, _pj_conteo[t]) for t in _pj_tags)
_pj_cards = ''.join(_pj_card(pr, i) for i, pr in enumerate(_pj))

_pj_body = f'''    <section class="pj-head frame-grid" aria-labelledby="page-title">
      <div class="container">
        <ol class="breadcrumb" aria-label="Ruta"><li><a href="{{home}}">Inicio</a></li><li aria-current="page">Proyectos</li></ol>
        <h1 class="pj-title" id="page-title">Proyectos</h1>
        <div class="pj-filters">
          <div class="pj-group">
            <p class="pj-group-label" id="pj-cat">Servicio</p>
            <ul class="pj-chips" aria-labelledby="pj-cat">{_pj_cat_btns}</ul>
          </div>
          <div class="pj-group">
            <p class="pj-group-label" id="pj-tag">Disciplina</p>
            <ul class="pj-chips" aria-labelledby="pj-tag">{_pj_tag_btns}</ul>
          </div>
        </div>
      </div>
    </section>

    <section class="pj-list" aria-label="Proyectos">
      <div class="container">
        <ul class="pj-grid" role="list">{_pj_cards}
        </ul>
        <p class="pj-empty" hidden>No hay casos con ese filtro.</p>
      </div>
    </section>
    <script src="{{p}}js/proyectos.js" defer></script>
'''

page('proyectos/index.html', 'Proyectos de branding, diseño web y producto digital · Luis Vicencio',
     'Casos de estudio de Luis Vicencio: identidad visual, estrategia de marca, sitios web y productos digitales para pymes y empresas en Chile.',
     body=_pj_body, current='proyectos', contact=False, html_class='motion inicio caso', extra_css=['css/inicio.css'])
