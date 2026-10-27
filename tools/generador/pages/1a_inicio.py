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


# Huellas (contacto): la línea camina. Avanza por un eje y en cada paso dibuja el contorno de una pisada,
# alternando pie izquierdo y derecho. Cada pisada cuelga del eje por el arco interno del pie, así la línea no cruza
# ninguna huella. Medidas para un pie de largo 1 (a: hacia afuera del eje; v: hacia adelante).
_PLANTA_IN = [(-.12, .45), (-.15, .58), (-.16, .7), (-.13, .78)]                       # arco → bola del pie (lado interno)
_PUNTA = [(-.1, .88), (-.03, .95), (.05, .97), (.13, .93), (.19, .84)]                  # punta redondeada
_PLANTA_EX = [(.21, .66), (.19, .52), (.15, .38), (.15, .22), (.11, .06), (0, 0), (-.1, .04), (-.13, .18),
              (-.12, .32), (-.12, .45)]                                                 # lado externo → talón → arco


def _pie():
    """Contorno del pie como lista de puntos (a, v): sube por el lado interno, rodea la punta y baja por el lado
    externo hasta el talón."""
    pts = list(_PLANTA_IN) + _PUNTA
    return pts + _PLANTA_EX


def _huellas(inicio, a, b, fin, pasos, largo, sep, ky):
    """Trazado de `inicio` a `fin` con `pasos` pisadas sobre el eje a→b. `ky` compensa el estiramiento vertical
    del SVG (preserveAspectRatio="none") para que las huellas no se vean deformadas."""
    (ax, ay), (bx, by) = a, b
    dx, dy = bx - ax, (by - ay) / ky
    n = (dx * dx + dy * dy) ** .5
    fx, fy = dx / n, dy / n          # hacia adelante (en espacio sin estirar)
    nx, ny = -fy, fx                 # lateral
    pie = _pie()
    pts = [inicio]
    for i in range(pasos):
        t = (i + .5) / pasos
        cx, cy = ax + dx * t - fx * largo * .5, ay / ky + dy * t - fy * largo * .5   # talón de la pisada
        lado = 1 if i % 2 == 0 else -1
        for pa, pv in pie:
            u = lado * (sep + pa * largo)
            pts.append((cx + fx * pv * largo + nx * u, (cy + fy * pv * largo + ny * u) * ky))
    pts.append(fin)
    f = lambda v: f'{v:.1f}'
    return 'M' + ' L'.join(f'{f(x)} {f(y)}' for x, y in pts)

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
        <h1 class="pl-display pl-hero-title" id="pl-hero-title"><span class="pl-line"><span class="pl-line-in">Diseñ<span class="pl-o">o</span> marcas </span></span><span class="pl-line"><span class="pl-line-in" data-dir="1">que <span class="pl-u">desean<span class="pl-base" aria-hidden="true"></span></span> </span></span><span class="pl-line"><span class="pl-line-in">moverse</span></span></h1>
        <p class="pl-lead">Soy un diseñador de productos digitales construyendo estrategias, identidad y experiencias en torno a tu servicio.</p>
      </div>
      {_hilo([_hero_desk], [_hero_mob], 'pl-thread-front')}
      <span class="pl-head" aria-hidden="true"></span>
      <a class="pl-scroll" href="#ideas" aria-label="Bajar a la siguiente sección"><svg class="icon" aria-hidden="true"><use href="img/icons.svg#i-arrow"/></svg></a>
    </section>
'''

# 2. EL MUNDO DE LAS IDEAS (claro): el collage actual; la línea pasa por detrás de los productos
_ideas = HOME_IDEAS
_ini = _ideas.index('          <p>Una idea vale'); _fin = _ideas.index('          <a class="btn btn-outline ideas-cta"')
_ideas = _ideas[:_ini] + '          <p>Se trata de conectar tu marca con sus usuarios y su entorno para definir tendencias.</p>\n' + _ideas[_fin:]
# Sin la píldora "Ver portafolio" (el portafolio está más abajo en la misma página)
_ini = _ideas.index('        <a class="ideas-pill"'); _fin = _ideas.index('</a>', _ini) + len('</a>\n')
_ideas = _ideas[:_ini] + _ideas[_fin:]
_ideas = _ideas.replace('<section class="panel panel-plain ideas"', '<section class="panel panel-plain ideas pl-sec pl-ideas" id="ideas"', 1)
# La línea baja y se enrolla en espiral en la botella central (pasa por delante, por detrás y otra vez por delante).
# Con JavaScript se construye midiendo el atomizador (js/main.js, ideasPath); esta es la versión sin JavaScript.
_ideas_desk = ['M994 0 C994 160 640 220 620 400 C680 560 860 560 820 720 C780 860 720 900 720 1000']
_ideas_mob = ['M187.5 0 C187.5 140 120 220 150 380 C180 540 260 600 220 760 C200 860 187.5 900 187.5 1000']
_ideas = _ideas.replace('      <div class="ideas-stage">', '      ' + _hilo(_ideas_desk, _ideas_mob) + '\n      <div class="ideas-stage">', 1)
# Capa delantera (sobre los productos), recortada por js/main.js a los cruces por delante de la botella
_ideas = _ideas.replace('      <div class="container ideas-foot">', '      ' + _hilo(_ideas_desk, _ideas_mob, 'pl-thread-front') + '\n      <div class="container ideas-foot">', 1)
INICIO_IDEAS = _ideas

# 3. SISTEMAS (claro): la línea se abre en un óvalo con un punto por disciplina (en móvil, dos columnas).
#    Con JavaScript, el título y cada disciplina aparecen cuando la línea pasa por ellos (js/main.js).
# Disciplinas del óvalo con una descripción breve (EDITAR: textos propuestos por Claude, revisar con Luis)
_disciplinas = [('Branding', 'Estrategia y propósito que ordenan cómo se presenta tu marca.'),
                ('Identidad', 'Logotipo, color, tipografía y aplicaciones que hacen reconocible tu marca.'),
                ('UX Research', 'Entrevistas y pruebas con usuarios para decidir con evidencia.'),
                ('Productos digitales', 'Sitios, apps y plataformas diseñados y prototipados, listos para construir.'),
                ('AI workflow', 'Flujos de trabajo con IA para prototipar y producir más rápido.'),
                ('Colaboración', 'Trabajo integrado con tu equipo, desarrolladores y otros creadores.')]
# Óvalo (centro 720 500, radios 440 × 330) en cuartos de elipse con curvas, para poder reescalarlo en js/main.js
_caps_desk = ['M720 0 V170 C963 170 1160 318 1160 500 C1160 682 963 830 720 830 V1000', 'M720 170 C477 170 280 318 280 500 C280 682 477 830 720 830']
# En móvil, dos paralelas juntas al centro; las disciplinas quedan por fuera de ellas
_caps_mob = ['M187.5 0 V330 C187.5 360 210 355 210 385 V880 C210 910 187.5 905 187.5 935 V1000',
             'M187.5 330 C187.5 360 165 355 165 385 V880 C165 910 187.5 905 187.5 935']
INICIO_SISTEMAS = f'''
    <!-- INICIO · SISTEMAS -->
    <section class="pl-sec pl-light pl-caps" aria-labelledby="pl-caps-title">
      {_hilo(_caps_desk, _caps_mob)}
      <h2 class="pl-title pl-caps-title" id="pl-caps-title">Diseño sistemas que identifican y reducen la brecha que separa a tu negocio de tu público.</h2>
      <ul class="pl-caps-list" role="list">''' + ''.join(f'''
        <li class="pl-cap pl-cap-{i}"><span class="pl-dot" aria-hidden="true"></span><strong class="pl-cap-name">{d}</strong><span class="pl-cap-desc">{x}</span></li>''' for i, (d, x) in enumerate(_disciplinas, 1)) + '''
      </ul>
    </section>
'''

# 4. PORTAFOLIO (claro): el carrusel actual; la línea baja por el costado y vuelve al centro
INICIO_PORTAFOLIO = f'''
    <!-- INICIO · PORTAFOLIO -->
    <section class="pl-sec pl-light more pl-folio" id="proyectos" aria-labelledby="pl-folio-title">
      {_hilo(['M720 0 C720 90 1290 60 1290 220 C1290 420 980 560 980 760 C980 900 720 880 720 1000'],
             ['M187.5 0 C187.5 60 345 60 345 160 V820 C345 920 187.5 900 187.5 1000'])}
      <h2 class="pl-display pl-folio-title" id="pl-folio-title">Portafolio</h2>
      <div class="more-stage">
        <div class="more-nav" hidden>
          <button class="more-prev" type="button" aria-label="Proyecto anterior">{_arrow}</button>
          <button class="more-next" type="button" aria-label="Proyecto siguiente">{_arrow}</button>
        </div>
        <ul class="more-arc" aria-label="Proyectos">{_more_arc}
        </ul>
      </div>
      <div class="pl-inner pl-center"><a class="btn btn-primary" href="proyectos.html">Ver todos los proyectos {_arrow}</a></div>
    </section>
'''

# 5. MARCA Y PRODUCTO (oscuro): la línea entra con una curva, forma una flecha hacia la derecha, un zigzag con esquinas
#    redondeadas y una flecha hacia la izquierda, y sale hacia abajo (boceto de Luis). Las puntas de las flechas son en ángulo.
_flechas = ('M720 0 C722 80 745 140 821 144 L1174 144 Q1214 144 1214 104 L1214 38 L1398 256 L1228 460 L1228 412 '
            'Q1228 372 1190 372 L1170 372 Q1132 372 1132 410 L1132 588 Q1132 626 1094 626 L1057 626 Q1019 626 1019 588 '
            'L1019 517 L828 744 L1007 957 L1007 877 Q1007 839 1045 839 L1152 839 Q1190 839 1190 877 L1190 1000')
INICIO_PRODUCTO = f'''
    <!-- INICIO · MARCA Y PRODUCTO -->
    <section class="pl-sec pl-dark pl-producto" data-thread="fit" aria-labelledby="pl-producto-title">
      {_hilo([_flechas],
             ['M187.5 0 V60 Q187.5 90 217.5 90 H325 Q355 90 355 120 V880 Q355 910 325 910 H217.5 Q187.5 910 187.5 940 V1000'])}
      <div class="pl-inner">
        <h2 class="pl-title" id="pl-producto-title">Marca y producto en la misma dirección</h2>
        <p class="pl-lead">Product Owner y estratega de marca para pymes y startups. Me sumo a tu equipo para que lo que construyes tenga un norte claro, prioridades ordenadas y entregas que cumplan lo esperado.</p>
        <!-- Firma de la sección -->
        <p class="pl-signature"><strong>Luis Vicencio</strong><span class="pl-mono">Diseñador digital.</span></p>
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

# 7. CONTACTO (claro): la línea llega caminando, dejando huellas, hasta el titular
INICIO_CONTACTO = f'''
    <!-- INICIO · CONTACTO -->
    <section class="pl-sec pl-light pl-contact" id="contacto" aria-labelledby="pl-contact-title">
      {_hilo([_a_curvas(_huellas((1190, 0), (1220, 50), (770, 320), (720, 420), 3, 175, 52, 1.12))],
             [_a_curvas(_huellas((187.5, 0), (187.5, 10), (187.5, 340), (187.5, 380), 3, 95, 30, 1.5))], paso=5)}
      <div class="pl-inner pl-center">
        <h2 class="pl-display" id="pl-contact-title">¿Quieres que tu marca se mueva dejando huella?</h2>
        <a class="btn btn-primary" href="{WA_MARCAS}" rel="noopener noreferrer" target="_blank">Hablemos<span class="sr-only"> (WhatsApp, se abre en una pestaña nueva)</span> {_arrow}</a>
      </div>
    </section>
'''

# 8. BLOG (claro): EDITAR: artículos pendientes
INICIO_BLOG = '''
    <!-- INICIO · BLOG -->
    <section class="pl-sec pl-light pl-blog" id="blog" aria-labelledby="pl-blog-title">
      <div class="pl-inner">
        <h2 class="pl-title" id="pl-blog-title">Blog</h2>
        <p class="pl-lead">Información que puede ser de utilidad para tu negocio o para que me conozcas.</p>
        <!-- EDITAR: reemplazar por los artículos reales (título, bajada, fecha y enlace) -->
        <ul class="pl-blog-list" role="list">''' + ''.join('''
          <li class="card pl-post"><p class="pl-mono">Próximamente</p><p class="pl-post-title">Artículo pendiente</p></li>''' for _ in range(3)) + '''
        </ul>
      </div>
    </section>
'''

page('index.html', 'Luis Vicencio · Diseño de marcas, productos digitales y estrategia',
     'Diseño marcas que desean moverse: estrategia, identidad y experiencias para tu servicio. Branding, UX Research y productos digitales para pymes y startups en Chile.',
     contact=False, canonical='', html_class='home motion v2 inicio', extra_css=['css/home-v2.css', 'css/inicio.css'],
     og_image='img/og/inicio.jpg', og_alt='Línea de productos Fuchi Chao: detergente, eliminador de olores y jabón anti olores',
     jsonld=[person_ld(),
             {'@context': 'https://schema.org', '@type': 'ProfessionalService', '@id': SITE + '#servicio', 'name': 'Luis Vicencio · Diseño de marcas y productos digitales',
              'url': SITE, 'description': 'Estrategia, identidad y experiencias para marcas, servicios y productos digitales: branding, UX Research, productos digitales y Product Owner.',
              'image': SITE + 'img/og/inicio.jpg', 'telephone': TELEFONO, 'email': 'mailto:' + EMAIL, 'sameAs': PERFILES,
              'founder': {'@id': PERSON_ID}, 'areaServed': {'@type': 'Country', 'name': 'Chile'},
              'address': {'@type': 'PostalAddress', 'addressCountry': 'CL'}},
             faq_ld(_preguntas)],
     body=INICIO_HERO + INICIO_IDEAS + INICIO_SISTEMAS + INICIO_PORTAFOLIO + INICIO_PRODUCTO
     + INICIO_CONTACTO + INICIO_BLOG + HOME_PREGUNTAS)
