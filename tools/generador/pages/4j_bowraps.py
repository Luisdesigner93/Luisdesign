# Caso Bowraps (2022): naming e identidad visual de una marca de wraps y bowls frescos, en colaboración con Claudio Almeyda Godoy.
# Composición editorial igual a LAB*502 y Fuchi Chao, con las clases lab-* de css/inicio.css (variantes lab-bw-*).
# Texto basado en tools/narrativa/01-narrativa-y-casos.md ("Caso nuevo: Bowraps"). Pendiente de revisión de Luis.
_bw = next(pr for pr in PROJECTS if pr['slug'] == 'bowraps')
_bw_img = {im['src'].rsplit('/', 1)[1].rsplit('.', 1)[0]: im for im in _bw['images']}


def _bw_fig(key, cls='', lazy=True, mitad=False):
    return f'\n      <figure class="lab-fig{(" " + cls) if cls else ""}">{img_tag(_bw_img[key], "lab-img-half" if mitad else "lab-img", lazy=lazy)}</figure>'


def _bw_par(a, b, cls, lazy=True):
    """Dos imágenes a la misma altura (en móvil, una bajo la otra). cls fija la proporción de las columnas."""
    return f'\n      <div class="lab-pair lab-pair-tp {cls}">' + _bw_fig(a, lazy=lazy, mitad=True) + _bw_fig(b, lazy=lazy, mitad=True) + '\n      </div>'


def _bw_text(html):
    return f'\n      <div class="lab-text">{html}</div>'


_bw_chips = ''.join(f'<li>{t}</li>' for t in _bw['tags'])
_bw_body = f'''    <section class="lab-head" aria-labelledby="page-title">
      <div class="lab-wide">
        {case_ruta(_bw)}
        <h1 class="lab-title" id="page-title">{_bw['title']}</h1>
        <p class="lab-lead">{_bw['summary']}</p>
        <div class="lab-meta">
          <ul class="case-chips" aria-label="Disciplinas">{_bw_chips}</ul>
          <p class="lab-year"><span class="sr-only">Año: </span>{_bw['year']}</p>
        </div>
      </div>
    </section>

    <article class="lab-case lab-wide" aria-label="Detalle del caso">''' + _bw_fig('01', lazy=False) + _bw_fig('02') + _bw_fig('04') + _bw_fig('06') + _bw_par('07', '08', 'lab-bw-c') + _bw_fig('09') + _bw_fig('10') + _bw_par('13', '05', 'lab-bw-a') + _bw_par('11', '12', 'lab-bw-d') + _bw_text(
    '<p>La marca está en uso y sigue en funcionamiento en Viña del Mar.</p>'
    '<p>El proyecto fue en colaboración con el diseñador gráfico Claudio Almeyda Godoy. Fue uno de mis primeros procesos liderando a otro diseñador.</p>'
    ) + '''
    </article>
'''

_bw_desc = 'Caso de estudio: naming, logotipo, identidad visual y aplicaciones de Bowraps, una marca de wraps y bowls frescos de la región de Valparaíso.'
page('proyectos/bowraps.html', 'Bowraps: naming e identidad visual para una marca de wraps y bowls · Luis Vicencio',
     _bw_desc, current='proyectos', ogtype='article', contact=False, html_class='motion inicio caso', extra_css=['css/inicio.css'],
     **case_seo(_bw, _bw_desc), body=_bw_body + case_nav(_bw))
