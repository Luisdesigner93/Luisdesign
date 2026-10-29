import math
# Inicio (index.html): identidad con una línea continua que recorre la página (referencia: dakshgajjar.com).
# Nació como piloto; textos entregados por Luis el 2026-10-27, con correcciones de forma.
# Cada sección tiene su tramo de línea: un SVG que ocupa la sección (viewBox de escritorio y de móvil, estirado sin
# deformar el grosor) y que se dibuja con el scroll (css/inicio.css). Los tramos se unen al centro, en el borde de cada sección.
# La línea es de color destacador (verde amarillo flúor, --pl-line en css/inicio.css).

# Trazo de la firma "luis" (la "i" va sin punto, por diseño) sobre el logo cuadrado (img/marca/logo-luy-cuadrado.png, 560 × 560):
# en el orden del boceto de Luis: la l baja; u, u, i son lazos angostos (sube en diagonal hasta la punta y baja casi vertical);
# la s baja, hace el lazo bajo la línea base y la cola cruza hacia arriba a la derecha (viewBox 55 55 480 420). Grosor: el de la línea, --pl-stroke en css/inicio.css.
_FIRMA = ('M160 78 L152 90 L141 110 L132 130 L123 150 L115 170 L108 190 L102 210 L97 230 L93 250 L89 270 L86 290 L84 310 L82 330 L82 350 L82 372 L84 388 L90 393 L97 388 L108 368 L119 347 L130 326 L140 306 L151 286 L162 265 L173 244 L184 224 L188 214 L184 232 L180 250 L175 270 L172 290 L170 310 L170 330 L169 350 L169 372 L171 388 L177 393 L184 388 L194 368 L205 347 L216 326 L226 306 L236 286 L247 265 L258 244 L268 224 L272 214 L269 232 L265 250 L260 270 L257 290 L255 310 L255 330 L254 350 L254 372 L256 388 L262 393 L269 388 L280 368 L290 347 L300 326 L311 306 L322 286 L332 265 L342 244 L353 224 L357 214 L353 232 L349 250 L344 270 L341 290 L339 310 L339 330 L338 350 L338 372 L340 388 L346 393 L353 388 L363 369 L373 349 L384 330 L394 311 L404 291 L414 272 L425 253 L435 233 L445 214 L449 203 L443 222 L439 240 L435 260 L432 280 L431 300 L430 330 L430 360 L431 385 L433 405 L434 428 L428 445 L414 452 L400 446 L393 432 L397 418 L410 405 L431 390 L456 371 L470 361 L484 350 L499 340 L509 333')



def _suave(d, paso=18):
    """Suaviza un trazado de curvas (solo comandos M y C absolutos) para que sea fluido en todo su largo:
    lo recorre en puntos equidistantes (cada `paso` unidades) y lo vuelve a trazar como B-spline cúbica,
    que no tiene quiebres ni saltos de curvatura (continuidad G2). Las demás formas se dejan tal cual."""
    import re as _re
    if _re.search(r'[^MC0-9.\s-]', d):
        return d
    nums = [float(n) for n in _re.findall(r'-?\d+(?:\.\d+)?', d)]
    pts = [(nums[0], nums[1])]
    curva = []
    for i in range(2, len(nums), 6):
        x0, y0 = pts[-1] if not curva else curva[-1]
        c = nums[i:i + 6]
        p0, p1, p2, p3 = (x0, y0), (c[0], c[1]), (c[2], c[3]), (c[4], c[5])
        for k in range(1, 41):  # muestreo fino de cada segmento Bézier
            t = k / 40; u = 1 - t
            curva.append((u**3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t**3 * p3[0],
                          u**3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t**3 * p3[1]))
    muestra = pts + curva
    # Remuestreo a distancia constante
    eq = [muestra[0]]; resto = 0.0
    for (ax, ay), (bx, by) in zip(muestra, muestra[1:]):
        seg = ((bx - ax) ** 2 + (by - ay) ** 2) ** .5
        while resto + seg >= paso and seg > 0:
            f = (paso - resto) / seg
            ax, ay = ax + (bx - ax) * f, ay + (by - ay) * f
            eq.append((ax, ay)); seg = ((bx - ax) ** 2 + (by - ay) ** 2) ** .5; resto = 0.0
        resto += seg
    eq.append(muestra[-1])
    # B-spline cúbica uniforme con extremos fijos (puntos de control repetidos)
    cp = [eq[0]] * 2 + eq + [eq[-1]] * 2
    f = lambda v: f'{v:.1f}'.rstrip('0').rstrip('.')
    out = [f'M{f(eq[0][0])} {f(eq[0][1])}']
    for i in range(len(cp) - 3):
        p0, p1, p2, p3 = cp[i:i + 4]
        b1 = ((2 * p1[0] + p2[0]) / 3, (2 * p1[1] + p2[1]) / 3)
        b2 = ((p1[0] + 2 * p2[0]) / 3, (p1[1] + 2 * p2[1]) / 3)
        b3 = ((p1[0] + 4 * p2[0] + p3[0]) / 6, (p1[1] + 4 * p2[1] + p3[1]) / 6)
        out.append(f'C{f(b1[0])} {f(b1[1])} {f(b2[0])} {f(b2[1])} {f(b3[0])} {f(b3[1])}')
    return ' '.join(out)


def _a_curvas(d):
    """Convierte un trazado con M, L, H, V, Q y C absolutos a solo M y C (mismas formas), para que js/main.js
    pueda reescalar cualquier tramo a su tamaño real (las coordenadas quedan siempre en pares x y)."""
    import re as _re
    tokens = _re.findall(r'[MLHVQC]|-?\d+(?:\.\d+)?', d)
    out, i, x, y, cmd = [], 0, 0.0, 0.0, None
    f = lambda v: f'{v:.1f}'.rstrip('0').rstrip('.')
    while i < len(tokens):
        if tokens[i].isalpha():
            cmd = tokens[i]; i += 1
        n = lambda k: float(tokens[i + k])
        if cmd == 'M':
            x, y = n(0), n(1); out.append(f'M{f(x)} {f(y)}'); i += 2
        elif cmd in 'LHV':
            nx, ny = (n(0), n(1)) if cmd == 'L' else ((n(0), y) if cmd == 'H' else (x, n(0)))
            i += 2 if cmd == 'L' else 1
            out.append(f'C{f(x + (nx - x) / 3)} {f(y + (ny - y) / 3)} {f(x + 2 * (nx - x) / 3)} {f(y + 2 * (ny - y) / 3)} {f(nx)} {f(ny)}')
            x, y = nx, ny
        elif cmd == 'Q':
            qx, qy, nx, ny = n(0), n(1), n(2), n(3); i += 4
            out.append(f'C{f(x + 2 * (qx - x) / 3)} {f(y + 2 * (qy - y) / 3)} {f(nx + 2 * (qx - nx) / 3)} {f(ny + 2 * (qy - ny) / 3)} {f(nx)} {f(ny)}')
            x, y = nx, ny
        elif cmd == 'C':
            out.append('C' + ' '.join(f(n(k)) for k in range(6))); x, y = n(4), n(5); i += 6
    return ' '.join(out)

def _hilo(desk, mob, cls='', extra='', paso=18):
    """Tramo de línea de una sección: un SVG para escritorio (1440 × 1000) y otro para móvil (375 × 1000), con las curvas suavizadas."""
    def svg(view, paths, media):
        pa = paso if media == 'desk' else min(paso, 10)
        return (f'<svg class="pl-thread pl-thread-{media} {cls}" viewBox="{view}" preserveAspectRatio="none" aria-hidden="true" focusable="false">'
                + ''.join(f'<path d="{_a_curvas(_suave(d, pa))}" pathLength="1" vector-effect="non-scaling-stroke"/>' for d in paths) + extra + '</svg>')
    return svg('0 0 1440 1000', desk, 'desk') + svg('0 0 375 1000', mob, 'mob')


# Huellas (contacto): la línea baja caminando. En cada paso dibuja el contorno de una pisada (sin dedos), alternando
# pie derecho e izquierdo, y entre una y otra se mece en una curva amplia, sin tramos rectos. Cada pisada empieza y
# termina en el talón, entrando por su lado externo; así la línea nunca cruza una huella.
# Contorno de un pie de largo 1 (a: hacia afuera del eje; v: hacia adelante), desde el talón por el lado interno.
_PIE = [(0, 0), (-.1, .04), (-.13, .18), (-.12, .32), (-.12, .45), (-.15, .58), (-.16, .7), (-.13, .8),
        (-.1, .88), (-.03, .95), (.05, .97), (.13, .93), (.19, .84), (.21, .66), (.19, .52), (.15, .38),
        (.15, .22), (.11, .06), (0, 0)]


def _huellas(inicio, eje_x, y0, y1, fin, pasos, largo, sep, ky):
    """Trazado de `inicio` a `fin` con `pasos` pisadas que bajan por la vertical `eje_x`, entre `y0` y `y1`.
    `ky` compensa el estiramiento vertical del SVG (preserveAspectRatio="none") para no deformar las huellas.
    Se calcula en un espacio sin estirar (y / ky) y se devuelve en las unidades del viewBox."""
    paso_v = (y1 - y0) / ky / pasos
    pts = []

    def curva(p0, p1, p2, p3, n=24):
        for k in range(1, n + 1):
            t = k / n; u = 1 - t
            pts.append((u**3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t**3 * p3[0],
                        u**3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t**3 * p3[1]))

    talones = []
    for i in range(pasos):
        lado = 1 if i % 2 == 0 else -1          # 1: a la derecha del eje
        talones.append(((eje_x + lado * sep, y0 / ky + paso_v * i), lado))
    ini = (inicio[0], inicio[1] / ky); fn = (fin[0], fin[1] / ky)
    pts.append(ini)
    c = sep * 2.2
    (hx, hy), lado = talones[0]
    curva(ini, (ini[0], ini[1] + paso_v * .6), (hx + lado * c, hy), (hx, hy))   # llega al primer talón por fuera
    for i, ((hx, hy), lado) in enumerate(talones):
        for pa, pv in _PIE[1:]:
            pts.append((hx + lado * pa * largo * 1.3, hy + pv * largo))
        if i + 1 < len(talones):
            (nx, ny), _ = talones[i + 1]
            # sale hacia el eje y se mece hasta entrar al talón siguiente por su lado externo
            curva((hx, hy), (hx - lado * c, hy), (nx - lado * c, ny), (nx, ny))
        else:
            curva((hx, hy), (hx - lado * c, hy), (fn[0], fn[1] - paso_v * .6), fn)
    f = lambda v: f'{v:.1f}'
    return 'M' + ' L'.join(f'{f(x)} {f(y * ky)}' for x, y in pts)

_arrow = '<svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg>'

# 1. HERO (oscuro): la línea entra desde arriba y se entrelaza con el titular. Cada línea del titular aparece desde abajo
#    al cargar y luego se desplaza en horizontal con el scroll (la del medio en sentido contrario), como en la referencia.
# Recorrido según el boceto de Luis: baja con una curva amplia, pasa por dentro de la O de "DISEÑO", sale por arriba y da
# la vuelta, subraya "DESEAN" con una recta limpia, hace un lazo abajo a la derecha y sale hacia la sección siguiente.
# Con JavaScript la línea del hero se construye midiendo la O (.pl-o) y la base de "desean" (.pl-base) (js/main.js, heroPath);
# estos trazados son la versión sin JavaScript.
_hero_desk = ('M130 0 C110 40 70 90 60 142 C50 200 45 260 52 315 C56 350 110 352 140 322 C168 294 152 250 118 258 '
              'C84 266 74 305 70 345 C66 385 44 410 38 445 C30 480 18 540 25 589 C32 620 50 635 80 640 '
              'C200 650 400 645 560 652 C700 658 790 665 812 700 C830 730 810 760 785 765 C750 772 715 765 722 745 '
              'C728 728 780 728 790 760 C798 800 780 860 770 900 C762 940 730 970 720 1000')
# En móvil: el mismo gesto, con el cruce bajo el titular y el rulo antes de la bajada
_hero_mob = ('M90 0 C70 60 40 140 36 220 C32 300 34 340 36 380 C40 430 105 430 118 395 C130 360 100 335 78 350 '
             'C58 362 52 400 48 440 C34 520 26 600 30 660 C34 690 60 700 100 702 C170 705 240 702 290 706 '
             'C320 710 345 722 345 745 C345 765 325 772 305 768 C285 764 287 748 302 745 C320 742 336 758 333 782 '
             'C328 840 345 900 300 935 C260 965 187.5 970 187.5 1000')
INICIO_HERO = f'''
    <!-- INICIO · HERO -->
    <section class="pl-sec pl-dark pl-hero" aria-labelledby="pl-hero-title">
      <!-- Fondo del hero anterior: fotografía en monocromo que se desvanece y cuadrícula -->
      <img class="pl-hero-bg" src="img/marca/hero-fondo.jpg" width="2000" height="1333" alt="" decoding="async" fetchpriority="high">
      {_hilo([_hero_desk], [_hero_mob], 'pl-thread-back')}
      <div class="pl-inner">
        <h1 class="pl-display pl-hero-title" id="pl-hero-title"><span class="pl-line"><span class="pl-line-in">Diseñ<span class="pl-o">o</span> <span class="pl-br-m"></span>marcas </span></span><span class="pl-line"><span class="pl-line-in" data-dir="1">que <span class="pl-u">desean<span class="pl-base" aria-hidden="true"></span></span> </span></span><span class="pl-line"><span class="pl-line-in">moverse</span></span></h1>
        <p class="pl-lead">Soy Luis, diseñador especializado en marcas y productos digitales. Trabajo contigo para entender hacia dónde quieres llevar tu negocio y transformar esa dirección en marcas, experiencias y productos que conecten con las personas.</p>
      </div>
      {_hilo([_hero_desk], [_hero_mob], 'pl-thread-front')}
      <span class="pl-head" aria-hidden="true"></span>
      <a class="pl-scroll" href="#ideas" aria-label="Bajar a la siguiente sección"><svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg></a>
    </section>
'''

# 2. EL MUNDO DE LAS IDEAS (claro): el collage actual; la línea pasa por detrás de los productos
_ideas = HOME_IDEAS
_ini = _ideas.index('          <p>Una idea vale'); _fin = _ideas.index('          <a class="btn btn-outline ideas-cta"')
_ideas = _ideas[:_ini] + '          <p>Por eso, me involucro desde las primeras preguntas hasta la implementación: ayudo a definir qué vale la pena construir, diseño posibles soluciones, valido las decisiones y acompaño el desarrollo para que esa idea se convierta en algo concreto y útil.</p>\n' + _ideas[_fin:]
# Ceja encima del título: la primera frase del texto de Ideas (el resto del texto queda debajo).
# Ceja y título van en un mismo bloque, para que la cuadrícula de .ideas-stage los trate como una sola pieza.
_ideas = _ideas.replace('        <h2 class="ideas-title"', '        <div class="ideas-head">\n        <p class="ideas-eyebrow pl-mono">Conecto lo conceptual con lo práctico.</p>\n        <h2 class="ideas-title"', 1)
_ideas = _ideas.replace('</h2>\n', '</h2>\n        </div>\n', 1)
# Sin la píldora "Ver portafolio" (el portafolio está más abajo en la misma página)
_ini = _ideas.index('        <a class="ideas-pill"'); _fin = _ideas.index('</a>', _ini) + len('</a>\n')
_ideas = _ideas[:_ini] + _ideas[_fin:]
# Sin el botón "Conversemos" de la sección Ideas (el contacto sigue disponible desde el encabezado y más abajo)
_ini = _ideas.index('          <a class="btn btn-outline ideas-cta"'); _fin = _ideas.index('</a>', _ini) + len('</a>\n')
_ideas = _ideas[:_ini] + _ideas[_fin:]
_ideas = _ideas.replace('<section class="panel panel-plain ideas"', '<section class="panel panel-plain ideas pl-sec pl-ideas" id="ideas"', 1)
# La línea baja y se enrolla en espiral en la botella central (pasa por delante, por detrás y otra vez por delante).
# Con JavaScript se construye midiendo el atomizador (js/main.js, ideasPath); esta es la versión sin JavaScript.
_ideas_desk = ['M994 0 C994 160 640 220 620 400 C680 560 860 560 820 720 C780 860 720 900 720 1000']
_ideas_mob = ['M187.5 0 C187.5 140 120 220 150 380 C180 540 260 600 220 760 C200 860 187.5 900 187.5 1000']
_ideas = _ideas.replace('      <div class="ideas-stage">', '      ' + _hilo(_ideas_desk, _ideas_mob) + '\n      <div class="ideas-stage">', 1)
# Fijación: el contenido de la sección queda quieto mientras el scroll abre las palabras y crece el producto (css/inicio.css)
_ideas = _ideas.replace('pl-sec pl-ideas" id="ideas" aria-labelledby="ideas-title">', 'pl-sec pl-ideas" id="ideas" aria-labelledby="ideas-title">\n      <div class="ideas-pin">', 1)
_ideas = _ideas.rstrip()
assert _ideas.endswith('</section>')
_ideas = _ideas[:-len('</section>')] + '      </div>\n    </section>\n'
INICIO_IDEAS = _ideas

# 3. SISTEMAS (claro): la línea se abre en un óvalo con un punto por disciplina (en móvil, dos columnas).
#    Con JavaScript, el título y cada disciplina aparecen cuando la línea pasa por ellos (js/main.js).
# Disciplinas del óvalo con una descripción breve (EDITAR: textos propuestos por Claude, revisar con Luis)
_disciplinas = [('Branding estratégico', 'Investigo el negocio, su contexto y su público para definir hacia dónde va tu marca y por qué deberían elegirla.'),
                ('Identidad', 'Transformo esa estrategia en un lenguaje visual que hace tu marca reconocible y coherente en cada punto de contacto.'),
                ('UX Research', 'Investigo qué necesitan las personas, cómo se comportan y qué esperan para diseñar experiencias que tengan sentido para ellas.'),
                ('Design Systems', 'Creo componentes y reglas compartidas que mantienen la coherencia del producto y permiten que evolucione junto al equipo de desarrollo.'),
                ('Productos digitales', 'Defino, prototipo y planifico soluciones digitales, desde las primeras ideas hasta su implementación.'),
                ('Desarrollo web', 'Diseño y coordino sitios web que comunican el valor de tu marca, generan oportunidades y ayudan a vender.'),
                ('AI Workflow', 'Diseño flujos de trabajo con IA para desarrollos complejos. La IA ejecuta; yo decido y superviso el resultado.'),
                ('Gestión ágil de producto', 'Organizo el backlog, priorizo requerimientos y planifico entregas para avanzar de forma iterativa junto al equipo.')]
# Las cuatro primeras van a la izquierda del óvalo y las cinco siguientes a la derecha; la primera de cada lado, arriba
_cap_slot = [1, 2, 3, 4, 6, 7, 8, 9]  # posiciones del óvalo en CSS (inicio.css): izquierda 1-4, derecha 6-9
_cap_cls = lambda slot: 'pl-cap-l' if slot <= 4 else 'pl-cap-r'
# Óvalo (centro 720 500, radios 330 × 270) en cuartos de elipse con curvas, para poder reescalarlo en js/main.js.
# El viewBox se ajusta al bloque del óvalo (.pl-stage): y de 0 a 1000. Las y negativas (de -500 a 0) corresponden al
# tramo del título, encima del bloque: la línea entra al centro, se abre por el costado derecho del título y vuelve al óvalo.
# La línea entra desde arriba, rodea el título por la derecha (sin pasar por detrás del texto), vuelve por debajo y entra al aro por arriba
# Ruta ortogonal con esquinas redondeadas: entra desde arriba, rodea el título por la derecha y vuelve por debajo hasta el aro
_caps_desk = ['M1080 -500 L1080.0 -371.0 Q1080 -316 1135.0 -316.0 L1275.0 -316.0 Q1330 -316 1330.0 -261.0 L1330.0 -43.0 Q1330 12 1275.0 12.0 L151.5 12.0 Q115 12 115.0 48.5 L115.0 48.5 Q115 85 151.5 85.0 L665.0 85.0 Q720 85 720.0 140.0 L720 200 C885.7 200 1020 338.6 1020 500 C1020 661.4 885.7 800 720 800 V1000', 'M720 200 C554.3 200 420 338.6 420 500 C420 661.4 554.3 800 720 800']
# En móvil, una sola línea recta por el centro exacto (50 % de 375); los puntos caen sobre ella y los textos quedan a cada lado
_caps_mob = ['M304 -500 C304 -200 187.5 -200 187.5 0 V1000']
INICIO_SISTEMAS = f'''
    <!-- INICIO · SISTEMAS -->
    <section class="pl-sec pl-light pl-caps" aria-labelledby="pl-caps-title">
      {_hilo(_caps_desk, _caps_mob)}
      <div class="pl-inner">
        <h2 class="pl-title pl-caps-title" id="pl-caps-title"><mark class="pl-mark">Diseño el camino</mark> <span class="pl-br-m"></span>para cerrar la <span class="pl-br-m"></span>brecha entre tu <span class="pl-br-m"></span>negocio y <span class="pl-br-m"></span>tu público.</h2>
      </div>
      <div class="pl-stage">
      <ul class="pl-caps-list" role="list">''' + ''.join(f'''
        <li class="pl-cap pl-cap-{_cap_slot[i - 1]} {_cap_cls(_cap_slot[i - 1])}"><span class="pl-dot" aria-hidden="true"></span><span class="pl-cap-txt"><strong class="pl-cap-name">{d}</strong><span class="pl-cap-desc">{x}</span></span></li>''' for i, (d, x) in enumerate(_disciplinas, 1)) + '''
      </ul>
      </div>
    </section>
'''

# 4. PORTAFOLIO (claro): proyectos como cubos isométricos repartidos alrededor del título (el mismo diseño de tools/generador/pages/1e_portafolio_alternativa.py).
#    La línea flúor sigue un recorrido ortogonal con esquinas redondeadas que rodea el título y los cubos.
def _redondeada(pts, radio=55):
    """Polilínea con esquinas redondeadas (Q): en cada giro corta el radio sin pasar de la mitad de cada tramo."""
    out = [f'M{pts[0][0]} {pts[0][1]}']
    for i in range(1, len(pts) - 1):
        (px, py), (cx, cy), (nx, ny) = pts[i - 1], pts[i], pts[i + 1]
        l1 = math.hypot(cx - px, cy - py); l2 = math.hypot(nx - cx, ny - cy)
        r = min(radio, l1 / 2, l2 / 2)
        out.append(f'L{cx + (px - cx) * r / l1:.1f} {cy + (py - cy) * r / l1:.1f} Q{cx} {cy} {cx + (nx - cx) * r / l2:.1f} {cy + (ny - cy) * r / l2:.1f}')
    out.append(f'L{pts[-1][0]} {pts[-1][1]}')
    return ' '.join(out)

# Recorrido (unidades 1440 × 1000, desde el borde superior de la sección): entra al centro, rodea el título y los cubos, y sale al centro
_ruta_portafolio = [(720, 0), (719, 233), (211, 432), (353, 503), (975, 288), (1245, 456), (527, 787), (720, 870), (1190, 870), (1190, 1000)]
_ruta_desk = _redondeada(_ruta_portafolio, 55)
# En móvil: recorrido isométrico (tramos a 30° como las caras de los cubos, en zigzag entre las dos columnas)
# y vuelta al centro; las esquinas se redondean. Entra y sale por el centro, como las secciones vecinas.
_ruta_mob = _redondeada([(187.5, 0), (187.5, 130), (67.5, 199), (67.5, 330), (307.5, 468), (307.5, 600), (187.5, 669), (187.5, 1000)], 14)

# Cubos isométricos (x %, y %, escala) y proyectos enlazados
_pf_cubos = [
    ('Fuchi Chao', 'proyectos/fuchi-chao.html', 14.8, 26.8, 1.0),
    ('Khronos', 'proyectos/khronos.html', 33.8, 17.7, 0.9),
    ('Sustentando', 'proyectos/sustentando.html', 51.0, 38.2, 1.1),
    ('Uvenergy', 'proyectos/uvenergy.html', 67.4, 21.0, 1.0),
    ('Yomecontrolo', 'proyectos/yomecontrolo.html', 25.9, 40.8, 1.2),
    ('Botes Salvavidas', 'proyectos/botes-salvavidas.html', 38.7, 57.0, 0.9),
    ('Bowraps', None, 68.1, 58.7, 1.0),
    ('Proyecto 8', None, 86.0, 41.0, 0.9),
]
_pf_cubo_html = '<span class="alt-cubo" aria-hidden="true"><span class="alt-cara alt-tapa"></span><span class="alt-cara alt-izq"></span><span class="alt-cara alt-der"></span></span>'
# Mockups definitivos (img/portafolio): se reparten en orden entre las posiciones
_pf_mockups = [('mockup-cerveza', 800, 667), ('mockup-telefono', 700, 738), ('mockup-laptop', 800, 534), ('mockup-pin', 800, 534)]
# Isométricos de producto (Khronos y Fuchi Chao), ya reducidos al tamaño que se muestra en pantalla
_pf_fotos = {'Khronos': ('mockup-khronos', 384, 576), 'Fuchi Chao': ('mockup-fuchi', 384, 576), 'Botes Salvavidas': ('mockup-botes', 480, 320), 'Yomecontrolo': ('mockup-yomecontrolo', 384, 576)}
_pf_items = ''
for i, (nombre, enlace, x, y, k) in enumerate(_pf_cubos):
    archivo, ancho, alto = _pf_fotos.get(nombre) or _pf_mockups[i % len(_pf_mockups)]
    mockup = f'<span class="alt-mock"><img src="img/portafolio/{archivo}.webp" width="{ancho}" height="{alto}" alt="" loading="lazy" decoding="async"></span>'
    if enlace:
        contenido = f'<a class="alt-link" href="{enlace}" aria-label="{nombre}: ver el proyecto completo">{mockup}<span class="alt-tag">{nombre}</span><span class="alt-hint">Haz clic para ver el proyecto completo</span></a>'
    else:
        contenido = f'<span class="alt-link alt-link-off">{mockup}<span class="alt-tag">{nombre}</span></span>'
    _pf_items += f'\n          <li class="alt-item alt-pf{i}">{contenido}</li>'
_pf_pos = ''.join(f'.alt-pf{i} {{ left: {x}%; top: {y}%; --k: {k}; }}\n' for i, (_n, _e, x, y, k) in enumerate(_pf_cubos))
_pf_mock_css = (
    '.alt-mock { display: block; transition: transform .45s cubic-bezier(.2, .8, .2, 1); }\n'
    '.alt-mock img { display: block; width: auto; height: calc(clamp(150px, 17vw, 230px) * var(--k, 1)); max-width: none; }\n'
    '.alt-link:hover .alt-mock, .alt-link:focus-visible .alt-mock { transform: translateY(-14px); }\n'
    # El texto de fondo "PORTAFOLIO" mide ~6.1 veces su tamaño: se ajusta para que no supere el ancho de la pantalla (con margen de 16px)
    '.alt-folio .alt-bg { font-size: clamp(56px, calc((100vw - 2rem) / 6.1), 300px); }\n'
    # Cada elemento se centra en su posición (sobre las diagonales); en móvil vuelve a la cuadrícula
    '.alt-folio .alt-item { transform: translate(-50%, -50%); }\n'
    '@media (max-width: 40em) { .alt-folio .alt-item { transform: none; } }\n'
)
open('css/portafolio-home.css', 'w', encoding='utf-8').write(_pf_pos + _pf_mock_css)

INICIO_PORTAFOLIO = f"""
    <!-- INICIO · PORTAFOLIO (cubos isométricos enlazados a sus proyectos) -->
    <section class="pl-sec pl-light alt-folio" id="proyectos" aria-labelledby="pl-folio-title">
      {_hilo([_a_curvas(_ruta_desk)], [_a_curvas(_ruta_mob)])}
      <p class="alt-bg" aria-hidden="true">PORTAFOLIO</p>
      <h2 class="sr-only" id="pl-folio-title">Portafolio</h2>
      <ul class="alt-stage" role="list">{_pf_items}
      </ul>
    </section>
"""


# Poste de señalética (Marca y producto): la línea entra desde arriba, recorre el contorno de cada cartel
# (caja 190 × 73 con 10 de margen, separación 36, centro en x = 1190) y sale hacia abajo.
# Poste de señalética: la línea entra desde arriba, recorre el contorno de cada flecha (cuerpo de 420 × 130 con punta de 44,
# separación de 22, x0 = 940) y sale hacia abajo.
_SIG_X0, _SIG_X1, _SIG_TIP, _SIG_H, _SIG_GAP, _SIG_TOP, _SIG_D = 940, 1360, 44, 130, 50, 283, 10
_SIG_XP = (_SIG_X0 + _SIG_X1 - _SIG_TIP) / 2  # centro del cuerpo: por aquí baja el poste
_sig_tops = [_SIG_TOP + i * (_SIG_H + _SIG_GAP) for i in range(3)]
def _sig_loop(top):
    """Contorno de una flecha (con margen _SIG_D) desde el centro superior del cuerpo, dando la vuelta hasta volver ahí."""
    t, b = top - _SIG_D, top + _SIG_H + _SIG_D
    mid = top + _SIG_H / 2
    x0 = _SIG_X0 - _SIG_D
    return [(_SIG_X1 - _SIG_TIP + _SIG_D * 0.6, t), (_SIG_X1 + _SIG_D * 1.6, mid), (_SIG_X1 - _SIG_TIP + _SIG_D * 0.6, b),
            (x0, b), (x0, t), (_SIG_XP, t)]
# Según el boceto: cada flecha se recorre por su contorno (entra arriba, punta, base y lado izquierdo) y desde
# arriba-izquierda baja por dentro hasta la siguiente. El primer tramo entra por el centro; los demás, por x = _SIG_XQ.
_SIG_XQ = 1057
def _sig_loop(top, entrada_x):
    t, b, mid = top - _SIG_D, top + _SIG_H + _SIG_D, top + _SIG_H / 2
    x0 = _SIG_X0 - _SIG_D
    return [(entrada_x, t), (_SIG_X1 - _SIG_TIP + _SIG_D * 0.6, t), (_SIG_X1 + _SIG_D * 1.6, mid),
            (_SIG_X1 - _SIG_TIP + _SIG_D * 0.6, b), (x0, b), (x0, t), (_SIG_XQ, t), (_SIG_XQ, b)]
_sig_puntos = [(720, 0), (720, 160), (_SIG_XQ, 160)]
_sig_puntos += _sig_loop(_sig_tops[0], _SIG_XQ)
_sig_puntos += _sig_loop(_sig_tops[1], _SIG_XQ)
_sig_puntos += _sig_loop(_sig_tops[2], _SIG_XQ)
# La salida vuelve al centro (x=720) para entrar al portafolio, que arranca ahí
_sig_puntos += [(_SIG_XQ, 950), (720, 950), (720, 1000)]
_sig_desk = _a_curvas(_redondeada(_sig_puntos, 20))

# Versión móvil (375 × 1000): las flechas van arriba, sobre el título, con la misma lógica (entrada, contorno, bajada)
# Flechas (móvil) alineadas con los iconos y textos: cada flecha envuelve su icono (izq.) y su texto (der.),
# con el centro en la misma altura que el texto; la línea baja por el hueco entre icono y texto (x = _M_XQ)
_M_X0, _M_X1, _M_TIP, _M_H, _M_GAP, _M_TOP, _M_D, _M_XQ = 50, 280, 22, 52, 65, 46, 5, 110
_m_tops = [_M_TOP + i * (_M_H + _M_GAP) for i in range(3)]
def _m_loop(top, ex):
    t, b, mid = top - _M_D, top + _M_H + _M_D, top + _M_H / 2
    x0 = _M_X0 - _M_D
    return [(ex, t), (_M_X1 - _M_TIP + _M_D * 0.6, t), (_M_X1 + _M_D * 1.6, mid),
            (_M_X1 - _M_TIP + _M_D * 0.6, b), (x0, b), (x0, t), (_M_XQ, t), (_M_XQ, b)]
# Tras la última flecha, la línea baja, rodea el texto por la derecha (por fuera, nunca por detrás) y vuelve al centro bajo la firma
_M_RX, _M_GIRO, _M_FIN = 358, 440, 930
# Entra por el centro (187.5), igual que la sección anterior, y baja hasta el poste de las flechas
_m_puntos = [(187.5, 0), (_M_XQ, 0)] + _m_loop(_m_tops[0], _M_XQ) + _m_loop(_m_tops[1], _M_XQ) + _m_loop(_m_tops[2], _M_XQ) + [(_M_XQ, _M_GIRO), (_M_RX, _M_GIRO), (_M_RX, _M_FIN), (_M_XQ, _M_FIN), (187.5, _M_FIN), (187.5, 1000)]
_sig_mob = _a_curvas(_redondeada(_m_puntos, 12))


# 5. MARCA Y PRODUCTO (oscuro): la línea entra con una curva, forma una flecha hacia la derecha, un zigzag con esquinas
#    redondeadas y una flecha hacia la izquierda, y sale hacia abajo (boceto de Luis). Las puntas de las flechas son en ángulo.
_flechas = ('M720 0 C722 80 745 140 821 144 L1174 144 Q1214 144 1214 104 L1214 38 L1398 256 L1228 460 L1228 412 '
            'Q1228 372 1190 372 L1170 372 Q1132 372 1132 410 L1132 588 Q1132 626 1094 626 L1057 626 Q1019 626 1019 588 '
            'L1019 517 L828 744 L1007 957 L1007 877 Q1007 839 1045 839 L1152 839 Q1190 839 1190 877 L1190 1000')
INICIO_PRODUCTO = f'''
    <!-- INICIO · MARCA Y PRODUCTO -->
    <section class="pl-sec pl-dark pl-producto" data-thread="fit" aria-labelledby="pl-producto-title">
      {_hilo([_sig_desk], [_sig_mob])}
      <!-- Poste de señalética: tres carteles sobre el trazo que recorre su contorno -->
      <div class="pl-signs" aria-hidden="true"><span class="pl-icono pl-icono-1"><svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-pen"/></svg></span><span class="pl-icono pl-icono-2"><svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-code"/></svg></span><span class="pl-icono pl-icono-3"><svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-layers"/></svg></span><span class="pl-cartel pl-cartel-1">Branding</span><span class="pl-cartel pl-cartel-2">Websites</span><span class="pl-cartel pl-cartel-3">Producto</span></div>
      <div class="pl-inner">
        <h2 class="pl-title" id="pl-producto-title">Construyamos en la misma dirección.</h2>
        <p class="pl-lead">Combino diseño centrado en las personas con metodologías ágiles para definir problemas, ordenar prioridades y coordinar entregas junto a equipos multidisciplinarios. Me interesa conectar lo que el negocio necesita, lo que las personas esperan y lo que los equipos pueden construir. <span class="pl-lead-extra">Porque una buena idea necesita más que diseño: necesita dirección, colaboración y decisiones fundamentadas.</span></p>
        <!-- Firma de la sección -->
        <p class="pl-signature"><strong>Luis Vicencio</strong><span class="pl-mono">Brand &amp; Product Designer.</span></p>
      </div>
    </section>
'''

# 6. LUIS VICENCIO: sección retirada del inicio (el nombre va como firma de "Marca y producto"); se conserva por si se recupera
INICIO_FIRMA = f'''
    <!-- INICIO · FIRMA -->
    <section class="pl-sec pl-light pl-sign" aria-labelledby="pl-sign-title">
      {_hilo(['M1190 0 C1190 90 650 100 561 184', 'M972 504 C1060 560 1120 700 1040 860 C980 960 720 920 720 1000'],
             ['M187.5 0 C187.5 80 130 120 120 209', 'M295 456 C350 520 360 700 300 860 C260 940 187.5 930 187.5 1000'])}
      <svg class="pl-firma pl-firma-grande" viewBox="55 55 480 420" aria-hidden="true" focusable="false"><path d="{_FIRMA}" pathLength="1" vector-effect="non-scaling-stroke"/></svg>
      <div class="pl-inner pl-center">
        <h2 class="pl-title" id="pl-sign-title">Luis Vicencio</h2>
        <p class="pl-mono">Diseñador digital.</p>
      </div>
    </section>
'''

# 7. CONTACTO (claro): la línea llega desde arriba, sin pisadas, hasta el titular
INICIO_CONTACTO = f'''
    <!-- INICIO · CONTACTO -->
    <section class="pl-sec pl-light pl-contact frame-grid" id="contacto" aria-labelledby="pl-contact-title">
      <div class="contact-pin">
      {_hilo(['M1189.4 0.0 C1189.4 97.2 353.7 83.3 353.7 222.2 C368.5 305.6 486.4 319.4 471.6 388.9 C456.9 444.4 383.2 444.4 390.6 500.0 C400.9 555.6 530.6 544.4 678.0 538.9 C825.4 533.3 943.3 555.6 1075.9 527.8 C1179.1 527.8 1238.1 444.4 1186.5 420.8 C1134.9 395.8 1105.4 486.1 1127.5 538.9 C1134.9 722.2 766.4 972.2 619.0 830.6'], ['M187.5 0 V852'], paso=8)}
      <div class="pl-inner pl-center">
        <h2 class="pl-display pl-anim-title" id="pl-contact-title"><span class="pl-line"><span class="pl-line-in">Tu próximo proyecto </span></span><span class="pl-line"><span class="pl-line-in" data-dir="1">empieza acá.</span></span></h2>
        <p class="pl-lead pl-contact-lead">Cada proyecto parte de una necesidad distinta. Podemos trabajar en tu marca, tu presencia web o un producto digital, según lo que tengas entre manos y lo que necesites resolver.</p>

        <a class="btn btn-primary" href="#contacto" data-abrir-contacto>Hablemos {_arrow}</a>
        
      </div>
      </div>
      <dialog class="pl-dialog" id="pl-conversemos" aria-labelledby="pl-dialog-title">
        <div class="pl-dialog-grid">
          <div class="pl-dialog-lead">
            <h2 class="pl-dialog-title" id="pl-dialog-title"><mark class="pl-mark">Hablemos</mark> de tu proyecto!</h2>
            <p class="pl-dialog-lead-text">Cuéntame en qué etapa está tu marca o tu producto y te respondo con una propuesta de alcance, plazos y presupuesto.</p>
          </div>
          <div class="pl-dialog-body">
            <div class="pl-dialog-head">
              <button class="pl-dialog-close" type="button" data-close aria-label="Cerrar">&times;</button>
            </div>
            <form class="pl-form" id="pl-form" method="dialog" aria-describedby="pl-form-note">
              <div class="pl-field"><input id="pl-name" name="nombre" type="text" autocomplete="name" required maxlength="100" placeholder=" " autofocus><label for="pl-name">Nombre</label></div>
              <div class="pl-field"><input id="pl-mail" name="correo" type="email" autocomplete="email" required maxlength="150" placeholder=" "><label for="pl-mail">Correo</label></div>
              <div class="pl-field"><textarea id="pl-msg" name="mensaje" required maxlength="2000" rows="4" placeholder=" "></textarea><label for="pl-msg">Mensaje</label></div>
              <div class="pl-hp" aria-hidden="true"><label for="pl-web">No completes este campo</label><input id="pl-web" name="web" type="text" tabindex="-1" autocomplete="off"></div>
              <label class="pl-check"><input type="checkbox" name="consentimiento" value="1" required><span>Acepto que guarden mi nombre, correo y mensaje para responderme. Lo explico en la <a href="privacidad.html">política de privacidad</a>.</span></label>
              <button class="btn btn-primary" type="submit">Enviar</button>
              <p class="pl-form-note" id="pl-form-note" role="status"></p>
            </form>
          </div>
        </div>
      </dialog>
    </section>
'''

# 8. BLOG (claro): una noticia principal y tres complementarias en carrusel. Cada tema es una página propia
# (noticias/, tools/generador/pages/1d_noticias.py); las bajadas son las mismas de cada página.
_noticia_principal = ('noticias/cuando-trabajar-tu-marca.html', 'Marca', '¿Cuándo es momento de trabajar tu marca?',
                      'Cuando nace tu negocio, cuando crece, cuando te comparan por precio, cuando cambia el rumbo o cuando la gente no sabe bien qué haces.')
_noticias_complementarias = [
    ('noticias/un-buen-equipo-no-basta.html', 'Producto digital', 'Un buen equipo técnico no basta si nadie ordena el camino',
     'Son señales que se repiten en productos digitales: el cliente pide una cosa, el equipo entrega otra y nadie tiene claro qué construir primero.'),
    ('noticias/tres-roles-de-producto.html', 'Servicios', 'Diseñar va más allá de diseñar: negocio, marcas y productos digitales',
     'En todos esos casos, el diseño puede aportar mucho más que una solución visual.'),
    ('noticias/metodo-scrum.html', 'Método', 'Scrum, con los pies en el negocio',
     'Desde el inicio acordamos prioridades, responsables y entregables, y reviso las señales de alerta en cada sprint para corregir el rumbo a tiempo.'),
    ('noticias/ley-21719-prepara-tu-web.html', 'Normativa', 'Ley 21.719 prepara tu web ante multas',
     'La Ley 21.719 está prevista para entrar en vigor a fines de 2026. Revisa formularios, cookies y avisos de privacidad de tu web antes de esa fecha.'),
]


# Imagen de las tarjetas complementarias que ya la tienen (misma imagen que la portada de la noticia)
_IMAGEN_COMPLEMENTARIA = {
    'noticias/metodo-scrum.html': ('img/noticias/metodo-scrum.webp',
                                   'Persona subiendo una escalera de bloques de concreto junto a paneles de vidrio y un arco verde lima con una flecha.'),
    'noticias/tres-roles-de-producto.html': ('img/noticias/tres-roles-de-producto.webp',
                                   'Mano sosteniendo un lápiz frente a paneles de vidrio translúcido y uno verde lima.'),
    'noticias/ley-21719-prepara-tu-web.html': ('img/noticias/ley-21719-prepara-tu-web.webp',
                                   'Balanza de justicia, un computador y un documento sobre bloques de concreto, junto a paneles de vidrio y un panel verde lima.'),
    'noticias/un-buen-equipo-no-basta.html': ('img/noticias/un-buen-equipo-no-basta.webp',
                                   'Cuatro personas reunidas alrededor de un computador sobre bloques de concreto, entre paneles de vidrio y un panel verde lima.'),
}


def _tarjeta_complementaria(href, etiqueta, titulo, bajada):
    imagen = _IMAGEN_COMPLEMENTARIA.get(href)
    img = f'<img class="pl-tarjeta-img" src="{{p}}{imagen[0]}" width="1672" height="941" alt="{imagen[1]}" loading="lazy">' if imagen else ''
    return f'''
          <li class="card"><div class="pl-tarjeta-foto">{img}<p class="pl-mono pl-chip">{etiqueta}</p></div><div class="pl-tarjeta-texto"><h3 class="pl-post-title"><a href="{href}">{titulo}</a></h3><p class="pl-post-lead">{bajada}</p></div></li>'''


_href, _etiqueta, _titulo, _bajada = _noticia_principal
INICIO_BLOG = f'''
    <!-- INICIO · BLOG (ARTÍCULOS) -->
    <section class="pl-sec pl-light pl-blog" id="blog" aria-labelledby="pl-blog-title">
      <div class="pl-inner">
        <p class="pl-mono pl-blog-ceja">Blog</p>
        <h2 class="pl-title" id="pl-blog-title"><span class="pl-resalte">Lecturas</span> que pueden ser de utilidad <span class="pl-resalte">para tu negocio</span></h2>
        <article class="card pl-blog-principal">
          <figure class="pl-blog-foto"><img src="{{p}}img/noticias/cuando-trabajar-tu-marca.webp" width="1536" height="1024" alt="Silueta de perfil de una persona entre paneles de vidrio translúcido y esmerilado, con un panel verde lima detrás." loading="lazy"></figure>
          <div class="pl-blog-texto">
            <p class="pl-mono pl-chip">{_etiqueta}</p>
            <h3 class="pl-blog-titulo"><a href="{_href}">{_titulo}</a></h3>
            <p class="pl-post-lead">{_bajada}</p>
            <div class="pl-blog-pie"><span>Por Luis Vicencio</span><a class="link-arrow" href="{_href}">Leer el artículo</a></div>
          </div>
        </article>
        <div class="pl-carrusel" data-carrusel>
          <div class="pl-carrusel-barra">
            <p class="pl-mono">Más artículos</p>
            <div class="pl-carrusel-botones">
              <button class="btn btn-secondary" type="button" data-paso="-1" aria-label="Artículo anterior">&larr;</button>
              <button class="btn btn-secondary" type="button" data-paso="1" aria-label="Artículo siguiente">&rarr;</button>
            </div>
          </div>
          <ul class="pl-carrusel-pista" role="list">''' + ''.join(_tarjeta_complementaria(*n) for n in _noticias_complementarias) + '''
          </ul>
        </div>
      </div>
    </section>
'''

page('index.html', 'Luis Vicencio · Diseño de marcas, productos digitales y estrategia',
     'Diseño marcas que desean moverse: estrategia, identidad y experiencias para tu servicio. Branding, UX Research y productos digitales para pymes y startups en Chile.',
     contact=False, canonical='', html_class='home motion v2 inicio', extra_css=['css/home-v2.css', 'css/inicio.css', 'css/portafolio-alt.css', 'css/portafolio-home.css'],
     og_image='img/og/inicio.jpg', og_alt='Línea de productos Fuchi Chao: detergente, eliminador de olores y jabón anti olores',
     jsonld=[person_ld(),
             {'@context': 'https://schema.org', '@type': 'ProfessionalService', '@id': SITE + '#servicio', 'name': 'Luis Vicencio · Diseño de marcas y productos digitales',
              'url': SITE, 'description': 'Estrategia, identidad y experiencias para marcas, servicios y productos digitales: branding, UX Research, productos digitales y Product Owner.',
              'image': SITE + 'img/og/inicio.jpg', 'telephone': TELEFONO, 'email': 'mailto:' + EMAIL, 'sameAs': PERFILES,
              'founder': {'@id': PERSON_ID}, 'areaServed': {'@type': 'Country', 'name': 'Chile'},
              'address': {'@type': 'PostalAddress', 'addressCountry': 'CL'}},
             faq_ld(_preguntas)],
     body=INICIO_HERO + INICIO_IDEAS + INICIO_SISTEMAS + INICIO_PRODUCTO + INICIO_PORTAFOLIO
     + INICIO_CONTACTO + INICIO_BLOG + HOME_PREGUNTAS,
     alternates={'es-CL': '', 'en': 'en/', 'x-default': ''})


# ---------- Versión en inglés del inicio (en/index.html) ----------
import re
# Los bloques con clases que usa js/main.js (título del hero, espiral de ideas, título de Sistemas) se reemplazan completos,
# conservando sus clases. El resto se traduce por texto exacto. Traducción en revisión: pendiente de revisión de Luis.
_EN_BLOQUES = [
    (r'<h1 class="pl-display pl-hero-title".*?</h1>',
     '<h1 class="pl-display pl-hero-title" id="pl-hero-title"><span class="pl-line"><span class="pl-line-in">De<span class="pl-o">s</span>ign <span class="pl-br-m"></span>brands </span></span>'
     '<span class="pl-line"><span class="pl-line-in" data-dir="1">that <span class="pl-u">want<span class="pl-base" aria-hidden="true"></span></span> </span></span>'
     '<span class="pl-line"><span class="pl-line-in">to move</span></span></h1>'),
    (r'<h2 class="ideas-title" id="ideas-title">.*?</h2>',
     '<h2 class="ideas-title" id="ideas-title"><span class="ideas-line"><span>The world</span><span class="ideas-gap" aria-hidden="true"></span>'
     '<span><span class="ideas-w1">of</span><span class="ideas-split"></span><span class="ideas-w2">ideas</span></span></span>'
     '<span class="ideas-line"><span><span class="ideas-w1">in</span><span class="ideas-split"></span><span class="ideas-w2">our</span></span>'
     '<span class="ideas-gap" aria-hidden="true"></span><span>products</span></span>'
     '<span class="ideas-line"><span>for everyday</span><span class="ideas-gap" aria-hidden="true"></span><span>life</span></span></h2>'),
    (r'<h2 class="pl-title pl-caps-title" id="pl-caps-title">.*?</h2>',
     '<h2 class="pl-title pl-caps-title" id="pl-caps-title"><mark class="pl-mark">I design the path</mark> <span class="pl-br-m"></span>to close the <span class="pl-br-m"></span>gap between your <span class="pl-br-m"></span>business and <span class="pl-br-m"></span>your audience.</h2>'),
    (r'<h2 class="pl-display pl-anim-title" id="pl-contact-title">.*?</h2>',
     '<h2 class="pl-display pl-anim-title" id="pl-contact-title"><span class="pl-line"><span class="pl-line-in">Your next project </span></span>'
     '<span class="pl-line"><span class="pl-line-in" data-dir="1">starts here.</span></span></h2>'),
    ('Cada proyecto parte de una necesidad distinta. Podemos trabajar en tu marca, tu presencia web o un producto digital, según lo que tengas entre manos y lo que necesites resolver.', 'Every project starts from a different need. We can work on your brand, your web presence or a digital product, depending on what you have in hand and what you need to solve.'),
]

_EN_TEXTOS = [
    # Hero, ideas y sistemas
    ('Soy Luis, diseñador especializado en marcas y productos digitales. Trabajo contigo para entender hacia dónde quieres llevar tu negocio y transformar esa dirección en marcas, experiencias y productos que conecten con las personas.',
     "Hi, I'm Luis, a designer specialized in brands and digital products. I work with you to understand where you want to take your business and turn that direction into brands, experiences and products that connect with people."),
    ('Conecto lo conceptual con lo práctico.', 'I connect the conceptual with the practical.'),
    ('Por eso, me involucro desde las primeras preguntas hasta la implementación: ayudo a definir qué vale la pena construir, diseño posibles soluciones, valido las decisiones y acompaño el desarrollo para que esa idea se convierta en algo concreto y útil.',
     "That's why I get involved from the first questions through implementation: I help define what is worth building, design possible solutions, validate decisions and support development so the idea becomes something concrete and useful."),
    ('Conversemos</a>', 'Let’s talk</a>'), ('>Conversemos <svg', '>Let’s talk <svg'),
    # Disciplinas
    ('Investigo el negocio, su contexto y su público para definir hacia dónde va tu marca y por qué deberían elegirla.', 'I research the business, its context and its audience to define where your brand is going and why they should choose it.'),
    ('Transformo esa estrategia en un lenguaje visual que hace tu marca reconocible y coherente en cada punto de contacto.', 'I turn that strategy into a visual language that makes your brand recognizable and consistent at every touchpoint.'),
    ('Investigo qué necesitan las personas, cómo se comportan y qué esperan para diseñar experiencias que tengan sentido para ellas.', 'I research what people need, how they behave and what they expect, to design experiences that make sense to them.'),
    ('Creo componentes y reglas compartidas que mantienen la coherencia del producto y permiten que evolucione junto al equipo de desarrollo.', 'I create shared components and rules that keep the product coherent and let it evolve alongside the development team.'),
    ('Defino, prototipo y planifico soluciones digitales, desde las primeras ideas hasta su implementación.', 'I define, prototype and plan digital solutions, from the first ideas to their implementation.'),
    ('Diseño y coordino sitios web que comunican el valor de tu marca, generan oportunidades y ayudan a vender.', 'I design and coordinate websites that communicate your brand\'s value, generate opportunities and help sell.'),
    ('Diseño flujos de trabajo con IA para desarrollos complejos. La IA ejecuta; yo decido y superviso el resultado.', 'I design AI workflows for complex developments. AI executes; I decide and supervise the result.'),
    ('Organizo el backlog, priorizo requerimientos y planifico entregas para avanzar de forma iterativa junto al equipo.', 'I organize the backlog, prioritize requirements and plan deliveries to move forward iteratively alongside the team.'),
    ('>Identidad</strong>', '>Identity</strong>'), ('>Branding estratégico</strong>', '>Strategic branding</strong>'),
    ('>Prototipado</strong>', '>Prototyping</strong>'), ('>Productos digitales</strong>', '>Digital products</strong>'),
    ('>Desarrollo web</strong>', '>Web development</strong>'), ('>Gestión ágil de producto</strong>', '>Agile product management</strong>'),
    ('>Design Systems</strong>', '>Design Systems</strong>'),
    # Portafolio
    ('>Portafolio</h2>', '>Portfolio</h2>'), ('Imagen pendiente', 'Image pending'), ('aria-label="Ver proyecto: ', 'aria-label="View project: '),
    ('>Estrategia</span>', '>Strategy</span>'), ('>Identidad</span>', '>Identity</span>'), ('>Comunicación B2B</span>', '>B2B communication</span>'),
    ('>Comunicación</span>', '>Communication</span>'), ('>Redes</span>', '>Social media</span>'), ('>Propuesta</span>', '>Proposal</span>'),
    ('De una tienda de insumos a un laboratorio fotográfico con propósito, que ganó un fondo cultural con su estrategia.',
     'From a supplies shop to a purposeful photo lab that won a cultural grant with its strategy.'),
    ('Cuatro años como aliado: de un logotipo a una consultora que consigue clientes por LinkedIn.',
     'Four years as a partner: from a logo to a consultancy that wins clients through LinkedIn.'),
    ('Una pyme de energía renovable que nació con marca en 2023 y la hizo crecer en 2025.',
     'A renewable energy SME that launched its brand in 2023 and grew it in 2025.'),
    ('Una comunicación que pone al centro su labor de rescate.', 'Communication that puts their rescue work at the center.'),
    ('Propuesta de rebranding: un nombre que encontró su sentido en "Tómate el tiempo".',
     'Rebranding proposal: a name that found its meaning in "Tómate el tiempo".'),
    ('Propuesta de rebranding: un nombre que encontró su sentido en &quot;Tómate el tiempo&quot;.',
     'Rebranding proposal: a name that found its meaning in "Tómate el tiempo".'),
    ('>Cerveza Khronos</h3>', '>Khronos beer</h3>'),
    # Marca y producto
    ('Construyamos en la misma dirección.', "Let's build in the same direction."),
    ('Combino diseño centrado en las personas con metodologías ágiles para definir problemas, ordenar prioridades y coordinar entregas junto a equipos multidisciplinarios. Me interesa conectar lo que el negocio necesita, lo que las personas esperan y lo que los equipos pueden construir. <span class="pl-lead-extra">Porque una buena idea necesita más que diseño: necesita dirección, colaboración y decisiones fundamentadas.</span>',
     'I combine people-centered design with agile methods to define problems, order priorities and coordinate deliveries alongside multidisciplinary teams. I am interested in connecting what the business needs, what people expect and what teams can build. <span class="pl-lead-extra">Because a good idea needs more than design: it needs direction, collaboration and well-founded decisions.</span>'),
    ('alt="Silueta de perfil de una persona entre paneles de vidrio translúcido y esmerilado, con un panel verde lima detrás."',
     'alt="Profile silhouette of a person between translucent and frosted glass panels, with a lime green panel behind."'),
    ('alt="Persona subiendo una escalera de bloques de concreto junto a paneles de vidrio y un arco verde lima con una flecha."',
     'alt="A person climbing a staircase of concrete blocks beside glass panels and a lime green arc with an arrow."'),
    ('alt="Cuatro personas reunidas alrededor de un computador sobre bloques de concreto, entre paneles de vidrio y un panel verde lima."',
     'alt="Four people gathered around a laptop on concrete blocks, between glass panels and a lime green panel."'),
    ('La Ley 21.719 está prevista para entrar en vigor a fines de 2026. Revisa formularios, cookies y avisos de privacidad de tu web antes de esa fecha.',
     'Law 21.719 is expected to take effect at the end of 2026. Review forms, cookies and privacy notices on your website before that date.'),
    ('>Normativa</p>', '>Regulation</p>'),
    ('>Ley 21.719 prepara tu web ante multas</a>', '>Law 21.719 prepares your website for fines</a>'),
    ('alt="Balanza de justicia, un computador y un documento sobre bloques de concreto, junto a paneles de vidrio y un panel verde lima."',
     'alt="A justice scale, a laptop and a document on concrete blocks, beside glass panels and a lime green panel."'),
    ('alt="Mano sosteniendo un lápiz frente a paneles de vidrio translúcido y uno verde lima."',
     'alt="A hand holding a pencil in front of translucent glass panels and a lime green one."'),
    ('>Diseñador digital.<', '>Digital designer.<'),
    # Contacto y diálogo
    ('Hablemos (WhatsApp, se abre en una pestaña nueva)', 'Let’s talk (WhatsApp, opens in a new tab)'),
    ('(WhatsApp, se abre en una pestaña nueva)', '(WhatsApp, opens in a new tab)'),
    ('(se abre en una pestaña nueva)', '(opens in a new tab)'),
    ('data-abrir-contacto>Hablemos ', 'data-abrir-contacto>Let’s talk '),
    ('<mark class="pl-mark">Hablemos</mark> de tu proyecto!</h2>', '<mark class="pl-mark">Let’s talk</mark> about your project!</h2>'),
    ('Cuéntame en qué etapa está tu marca o tu producto y te respondo con una propuesta de alcance, plazos y presupuesto.', 'Tell me what stage your brand or product is at, and I will reply with a proposal for scope, timelines and budget.'),
    ('>Nombre</label>', '>Name</label>'), ('>Correo</label>', '>Email</label>'), ('>Mensaje</label>', '>Message</label>'),
    ('No completes este campo', 'Leave this field empty'),
    ('Acepto que guarden mi nombre, correo y mensaje para responderme. Lo explico en la <a href="privacidad.html">política de privacidad</a>.',
     'I agree that my name, email and message are stored so I can reply. See the <a href="privacidad.html">privacy policy</a>.'),
    ('>Enviar</button>', '>Send</button>'),
    ('aria-label="Cerrar"', 'aria-label="Close"'),
    # Blog
    ('<span class="pl-resalte">Lecturas</span> que pueden ser de utilidad <span class="pl-resalte">para tu negocio</span></h2>',
     '<span class="pl-resalte">Reading</span> that may be useful <span class="pl-resalte">for your business</span></h2>'),
    ('>Marca</p>', '>Brand</p>'), ('>Producto digital</p>', '>Digital product</p>'),
    ('>Leer el artículo</a>', '>Read the article</a>'), ('>Más artículos</p>', '>More articles</p>'),
    ('<span>Por Luis Vicencio</span>', '<span>By Luis Vicencio</span>'),
    ('aria-label="Artículo anterior"', 'aria-label="Previous article"'), ('aria-label="Artículo siguiente"', 'aria-label="Next article"'),
    ('Cuando nace tu negocio, cuando crece, cuando te comparan por precio, cuando cambia el rumbo o cuando la gente no sabe bien qué haces.',
     'When your business is born, when it grows, when you are compared on price, when your direction changes, or when people do not quite know what you do.'),
    ('Son señales que se repiten en productos digitales: el cliente pide una cosa, el equipo entrega otra y nadie tiene claro qué construir primero.',
     'These are signs that repeat in digital products: the client asks for one thing, the team delivers another, and no one is clear on what to build first.'),
    ('En todos esos casos, el diseño puede aportar mucho más que una solución visual.',
     'In all those cases, design can offer much more than a visual solution.'),
    ('Desde el inicio acordamos prioridades, responsables y entregables, y reviso las señales de alerta en cada sprint para corregir el rumbo a tiempo.',
     'From the start we agree on priorities, owners and deliverables, and I review warning signs in every sprint to correct course in time.'),
    ('>Servicios</p>', '>Services</p>'), ('>Método</p>', '>Method</p>'), ('>Casos</p>', '>Cases</p>'), ('>Modalidad</p>', '>Format</p>'),
    ('>¿Cuándo es momento de trabajar tu marca?</a>', '>When is it time to work on your brand?</a>'),
    ('>Un buen equipo técnico no basta si nadie ordena el camino</a>', '>A good tech team is not enough if no one sets the course</a>'),
    ('>Diseñar va más allá de diseñar: negocio, marcas y productos digitales</a>', '>Design goes beyond design: business, brands and digital products</a>'),
    ('>Scrum, con los pies en el negocio</a>', '>Scrum, grounded in the business</a>'),
    ('>Productos con IA para organizaciones exigentes</a>', '>AI products for demanding organizations</a>'),
    ('>Cómo trabajamos juntos</a>', '>How we work together</a>'),
    # Preguntas frecuentes
    ('Preguntas <strong>frecuentes</strong>.', 'Frequently asked <strong>questions</strong>.'),
]

_EN_PREGUNTAS = [
    ('¿Cuándo es momento de trabajar mi marca?', 'When is it time to work on my brand?',
     'When your business is born, when it grows, when you are compared only on price, when your direction changes or when people do not quite know what you do. If you see yourself in any of these, it is a good time.'),
    ('¿Puedo partir solo con la identidad visual?', 'Can I start with visual identity only?',
     'Yes. Many brands start with identity and add strategy as the business grows, like Fuchi Chao.'),
    ('¿Qué es un Brand Compass?', 'What is a Brand Compass?',
     'A tool to define your brand’s purpose, differentiator, personality and promise. It is the north that guides everything else.'),
    ('¿Cuánto cuesta?', 'How much does it cost?',
     'It depends on level and scope. After a first conversation I send you a proposal with scope, timelines and a fixed value.'),
    ('¿Cuánto demora?', 'How long does it take?',
     'A visual identity or a corporate site usually takes four to eight weeks, depending on content and review rounds. A strategic branding project takes longer, depending on its scope; we define it in the proposal.'),
    ('¿Trabajas con otros creadores?', 'Do you work with other creators?',
     'Yes. When the project calls for it, I bring in photographers, filmmakers or designers and coordinate the work.'),
    ('¿Qué hace un Product Owner externo?', 'What does an external Product Owner do?',
     'They represent your business in front of the tech team: they define what gets built and in what order, and check that every delivery meets expectations, without you having to hire someone full time.'),
    ('¿Trabajas con mi equipo de desarrollo?', 'Do you work with my development team?',
     'Yes. I integrate with your team or your client’s team, as I did when coordinating an AI cell inside a Bytequest client’s team.'),
    ('¿Programas?', 'Do you code?',
     'I design and build functional prototypes with AI-assisted development to validate ideas fast. Production development is done by your team.'),
    ('¿Tienes experiencia con IA?', 'Do you have experience with AI?',
     'Yes: I have led products with multi-agent assistants, automatic call analysis, AI summaries and automations. I also work with spec-driven development: I write clear specifications so your team and AI tools build exactly what was agreed.'),
    ('¿Firmas acuerdos de confidencialidad?', 'Do you sign confidentiality agreements?',
     'Yes. That is why some cases are shown without the client’s name.'),
]


def _en_home(html):
    for patron, nuevo in _EN_BLOQUES:
        html, n = re.subn(patron, nuevo, html, count=1, flags=re.S)
        assert n == 1, patron[:40]
    for es, en in _EN_TEXTOS:
        html = html.replace(es, en)
    for es, en, resp in _EN_PREGUNTAS:
        assert html.count(f'<summary>{es}</summary>') == 1, es
        html = html.replace(f'<summary>{es}</summary>', f'<summary>{en}</summary>')
        assert html.count(f'<p>{_ES_RESP[es]}</p>') == 1, es
        html = html.replace(f'<p>{_ES_RESP[es]}</p>', f'<p>{resp}</p>')
    # La versión en inglés vive en en/: sus rutas a recursos y a páginas de la raíz suben un nivel (noticias/ queda en en/)
    html = re.sub(r'(?<=["\s,])(img/|privacidad\.html|sobre-mi\.html|css/|js/|proyectos/)', r'../\1', html)
    return html


_ES_RESP = {q: a for q, a in _preguntas}
_EN_BODY = _en_home(INICIO_HERO + INICIO_IDEAS + INICIO_SISTEMAS + INICIO_PRODUCTO + INICIO_PORTAFOLIO
                    + INICIO_CONTACTO + INICIO_BLOG + HOME_PREGUNTAS)
page('en/index.html', 'Luis Vicencio · Brand and digital product strategy',
     'Brands that want to move: strategy, identity and experiences for your business. Branding, UX Research and digital products for SMEs and startups in Chile.',
     contact=False, canonical='en/', html_class='home motion v2 inicio', extra_css=['css/home-v2.css', 'css/inicio.css', 'css/portafolio-alt.css', 'css/portafolio-home.css'],
     og_image='img/og/inicio.jpg', og_alt='Fuchi Chao product line: detergent, odor eliminator and anti-odor soap',
     jsonld=[person_ld(), faq_ld([(en, resp) for _es, en, resp in _EN_PREGUNTAS])],
     body=_EN_BODY, lang='en', alternates={'es-CL': '', 'en': 'en/', 'x-default': ''})
