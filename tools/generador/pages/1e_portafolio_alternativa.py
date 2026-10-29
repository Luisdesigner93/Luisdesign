# Alternativa de portafolio (no enlazada desde el sitio; para comparar con la sección actual de la home).
# Composición de prueba: cubos 3D isométricos (proyección sin perspectiva, vista desde arriba hacia una esquina),
# ordenados en cuadrícula sobre fondo blanco. No usa imágenes de proyectos. Estilos en css/portafolio-alt.css (generado aquí).

def _alt_enlace(nombre, enlace):
    cubo = '<span class="alt-cubo" aria-hidden="true"><span class="alt-cara alt-tapa"></span><span class="alt-cara alt-izq"></span><span class="alt-cara alt-der"></span></span>'
    etiqueta = f'<span class="alt-tag">{nombre}</span>'
    if enlace:
        return f'<a class="alt-link" href="{enlace}" aria-label="{nombre}: ver el proyecto completo">{cubo}{etiqueta}<span class="alt-hint">Haz clic para ver el proyecto completo</span></a>'
    return f'<span class="alt-link alt-link-off">{cubo}{etiqueta}</span>'


_alt_proyectos = [
    ('Fuchi Chao', 'proyectos/fuchi-chao.html'),
    ('Khronos', 'proyectos/khronos.html'),
    ('Sustentando', 'proyectos/sustentando.html'),
    ('Uvenergy', 'proyectos/uvenergy.html'),
    ('Yomecontrolo', 'proyectos/yomecontrolo.html'),
    ('Botes Salvavidas', 'proyectos/botes-salvavidas.html'),
    ('Bowraps', None),  # sin página propia todavía
    ('Proyecto 8', None),
]

_alt_items = ''.join(
    f'''
          <li class="alt-item alt-d{i}">{_alt_enlace(nombre, enlace)}</li>'''
    for i, (nombre, enlace) in enumerate(_alt_proyectos)
)

# Posiciones repartidas alrededor del título, como en la referencia (x %, y % del escenario) y escala de cada cubo
_alt_pos = [(10, 16, 1.0), (33, 8, 0.9), (54, 30, 1.1), (76, 12, 1.0), (12, 56, 1.2), (38, 58, 0.9), (64, 58, 1.0), (86, 40, 0.9)]
_alt_diag = ''.join(
    f'.alt-d{i} {{ left: {x}%; top: {y}%; --k: {k}; }}\n' for i, (x, y, k) in enumerate(_alt_pos)
)

_alt_css = '''/* Alternativa de portafolio (generada por tools/generador/pages/1e_portafolio_alternativa.py).
   Cubos isométricos: rotación de 35,264° en X y 45° en Y, sin perspectiva (proyección ortogonal), vista desde arriba hacia una esquina. */
.alt-folio { position: relative; min-height: 100svh; background: #ffffff; overflow: hidden; overflow: clip; padding: clamp(4rem, 9vw, 7rem) 0; }
.alt-bg { position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); margin: 0; font-family: "Plus Jakarta Sans", sans-serif; font-weight: 800; font-size: clamp(90px, 22vw, 340px); letter-spacing: -0.05em; line-height: 1; color: rgba(11, 18, 32, .05); white-space: nowrap; pointer-events: none; user-select: none; }
.alt-stage { position: relative; z-index: 1; list-style: none; margin: 0 auto; padding: 0; width: min(1184px, calc(100% - 2rem)); height: min(900px, 115svh); }
.alt-item { position: absolute; display: flex; flex-direction: column; align-items: center; gap: 22px; }
/* Cubo: tres caras visibles, cada una en su propio plano (--s = arista) */
.alt-cubo { --s: calc(clamp(80px, 9vw, 120px) * var(--k, 1)); position: relative; display: block; width: var(--s); height: var(--s); transform-style: preserve-3d; transform: rotateX(-35.264deg) rotateY(45deg); }
.alt-cara { position: absolute; left: 0; top: 0; width: var(--s); height: var(--s); }
.alt-tapa { background: #f4f6fa; transform: rotateX(90deg) translateZ(calc(var(--s) / 2)); }
.alt-izq { background: #d6dce6; transform: translateZ(calc(var(--s) / 2)); }
.alt-der { background: #b9c2d0; transform: rotateY(90deg) translateZ(calc(var(--s) / 2)); }
.alt-link { display: flex; flex-direction: column; align-items: center; gap: 22px; color: inherit; text-decoration: none; }
.alt-link .alt-cubo { transition: transform .45s cubic-bezier(.2, .8, .2, 1); }
.alt-link:hover .alt-cubo, .alt-link:focus-visible .alt-cubo { transform: translateY(-14px) rotateX(-35.264deg) rotateY(45deg); }
.alt-link:hover .alt-tapa, .alt-link:focus-visible .alt-tapa { background: #ffffff; }
.alt-link:hover .alt-tag, .alt-link:focus-visible .alt-tag { border-color: #0b1220; }
.alt-link:focus-visible { outline: 2px solid #0b1220; outline-offset: 8px; border-radius: 12px; }
.alt-hint { position: absolute; top: 100%; left: 50%; margin-top: 10px; transform: translate(-50%, 6px); opacity: 0; transition: opacity .3s ease, transform .3s ease; font-family: var(--mono, monospace); font-size: 12px; color: #0b1220; white-space: nowrap; pointer-events: none; }
.alt-link { position: relative; }
.alt-link:hover .alt-hint, .alt-link:focus-visible .alt-hint { opacity: 1; transform: translate(-50%, 0); }
.alt-link-off { cursor: default; }
.alt-tag { display: inline-block; padding: 6px 14px; border-radius: 999px; border: 1px solid rgba(11, 18, 32, .3); background: #ffffff; font-family: var(--mono, monospace); font-size: 12px; letter-spacing: .03em; color: #0b1220; white-space: nowrap; }
@media (max-width: 40em) {
  .alt-stage { height: auto; display: grid; grid-template-columns: repeat(2, 1fr); gap: 2.5rem 1rem; justify-items: center; }
  .alt-item { position: relative; left: auto !important; top: auto !important; }
  .alt-bg { font-size: 22vw; top: 12%; }
  .alt-hint { display: none; }
}
'''

open('css/portafolio-alt.css', 'w', encoding='utf-8').write(_alt_css + _alt_diag)

_alt_body = f'''
    <section class="alt-folio" aria-labelledby="alt-title">
      <p class="alt-bg" aria-hidden="true">PORTAFOLIO</p>
      <h2 class="sr-only" id="alt-title">Portafolio</h2>
      <ul class="alt-stage" role="list">{_alt_items}
      </ul>
    </section>
'''

page('alternativa-portafolio.html', 'Alternativa de portafolio · Luis Vicencio',
     'Propuesta de portafolio con cubos isométricos sobre fondo blanco. Página de comparación, no enlazada desde el sitio.',
     body=_alt_body, current=None, contact=False, noindex=True,
     html_class='motion', extra_css=['css/portafolio-alt.css'])
