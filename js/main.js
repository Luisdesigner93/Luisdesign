'use strict';

// Header fijo: expone su altura en --header-h para que los elementos sticky se ubiquen debajo.
(function initHeader() {
  const header = document.querySelector('.site-header');
  if (!header) return;
  const setHeight = () => document.documentElement.style.setProperty('--header-h', `${header.offsetHeight}px`);
  setHeight();
  if ('ResizeObserver' in window) new ResizeObserver(setHeight).observe(header);
  else window.addEventListener('resize', setHeight);
})();

// Menú móvil: botón con aria-expanded; se cierra con Escape, al elegir un enlace o al tocar fuera.
(function initMenu() {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.getElementById('main-nav');
  if (!toggle || !nav) return;

  const setOpen = (open) => {
    toggle.setAttribute('aria-expanded', String(open));
    // Páginas en inglés (en/): mismas etiquetas traducidas
    const en = document.documentElement.lang.startsWith('en');
    toggle.setAttribute('aria-label', open ? (en ? 'Close menu' : 'Cerrar menú') : (en ? 'Open menu' : 'Abrir menú'));
    nav.classList.toggle('is-open', open);
    // La página no se desplaza mientras el menú está abierto.
    document.documentElement.classList.toggle('menu-open', open);
    if (!open) nav.querySelectorAll('.has-sub.is-open').forEach((item) => {
      item.classList.remove('is-open');
      item.querySelector('.nav-sub-toggle')?.setAttribute('aria-expanded', 'false');
    });
  };

  toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
  nav.addEventListener('click', (e) => { if (e.target.closest('a')) setOpen(false); });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && nav.classList.contains('is-open')) {
      setOpen(false);
      toggle.focus();
    }
  });
  document.addEventListener('click', (e) => {
    if (nav.classList.contains('is-open') && !nav.contains(e.target) && !toggle.contains(e.target)) setOpen(false);
  });
  // Al pasar a escritorio, el menú vuelve a su estado normal.
  window.matchMedia('(min-width: 53.76em)').addEventListener('change', (e) => { if (e.matches) setOpen(false); });
})();

// Año actual en el pie de página.
document.querySelectorAll('[data-year]').forEach((node) => { node.textContent = String(new Date().getFullYear()); });

// Proyectos: marca en el índice el proyecto visible y su avance de lectura.
(function initShowcase() {
  const items = [...document.querySelectorAll('.showcase-item')];
  if (!items.length) return;
  const links = new Map(items.map((item) => [item, document.querySelector(`.showcase-index a[href="#${item.id}"]`)]));
  const list = document.querySelector('.showcase-index ol');
  let current = null;
  let ticking = false;

  function update() {
    ticking = false;
    const line = window.innerHeight * 0.35; // altura de referencia para decidir el proyecto activo
    let active = null;
    for (const item of items) {
      const r = item.getBoundingClientRect();
      if (r.top <= line && r.bottom > line) { active = item; break; }
    }
    if (active !== current) {
      if (current) links.get(current)?.removeAttribute('aria-current');
      current = active;
      const link = current && links.get(current);
      if (link) {
        link.setAttribute('aria-current', 'true');
        // En móvil el índice es horizontal: mantiene visible el enlace activo sin mover la página.
        if (list && list.scrollWidth > list.clientWidth) {
          list.scrollTo({ left: link.parentElement.offsetLeft - list.clientWidth / 2 + link.parentElement.offsetWidth / 2, behavior: 'smooth' });
        }
      }
    }
    if (current) {
      const r = current.getBoundingClientRect();
      const p = Math.min(1, Math.max(0, (line - r.top) / r.height));
      links.get(current)?.style.setProperty('--p', p.toFixed(3));
    }
  }

  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } };
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  update();
})();

// Paneles laterales (<dialog class="drawer">): se abren con [data-drawer-open] y se cierran con la X, Escape o clic fuera.
(function initDrawers() {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  const root = document.documentElement;

  function close(drawer) {
    if (!drawer.open || drawer.classList.contains('is-closing')) return;
    if (reduceMotion.matches) { drawer.close(); return; }
    drawer.classList.add('is-closing');
    drawer.addEventListener('animationend', () => { drawer.classList.remove('is-closing'); drawer.close(); }, { once: true });
  }

  document.querySelectorAll('dialog.drawer').forEach((drawer) => {
    drawer.addEventListener('close', () => root.classList.remove('has-drawer'));
    // Escape: se usa la animación de salida en lugar del cierre inmediato.
    drawer.addEventListener('cancel', (e) => { e.preventDefault(); close(drawer); });
    // Clic en el fondo (fuera del contenido del panel).
    drawer.addEventListener('click', (e) => { if (e.target === drawer) close(drawer); });
    drawer.querySelectorAll('[data-drawer-close]').forEach((button) => button.addEventListener('click', () => close(drawer)));
  });

  document.querySelectorAll('[data-drawer-open]').forEach((trigger) => {
    const drawer = document.getElementById(trigger.dataset.drawerOpen);
    if (!(drawer instanceof HTMLDialogElement)) return;
    trigger.addEventListener('click', () => {
      drawer.showModal();
      root.classList.add('has-drawer');
      // Siempre abre desde el inicio del contenido, con el foco en el botón de cerrar.
      drawer.querySelectorAll('.drawer-body').forEach((body) => { body.scrollTop = 0; });
      drawer.querySelector('[data-drawer-close]')?.focus({ preventScroll: true });
    });
  });
})();

// Inicio v2: el título fijo de Proyectos se difumina a medida que las tarjetas pasan por encima.
(function initWorkFade() {
  const head = document.querySelector('.v2-work-head');
  const section = head && head.closest('.v2-work');
  if (!section) return;
  let ticking = false;
  function update() {
    ticking = false;
    const r = section.getBoundingClientRect();
    // Empieza cuando el título ya quedó fijo y las tarjetas comienzan a subir; termina tras ~60% de la altura de la ventana.
    const p = Math.min(1, Math.max(0, (window.innerHeight * 0.1 - r.top) / (window.innerHeight * 0.6)));
    head.style.setProperty('--fade', p.toFixed(3));
  }
  const onScroll = () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } };
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  update();
})();

// Servicios en móvil: la tarjeta que está a la vista en la fila deslizable queda activa (nítida y en color).
(function initServiceCards() {
  const row = document.querySelector('.svc-row');
  if (!row || !('IntersectionObserver' in window)) return;
  const cards = row.querySelectorAll('.svc-card');
  const mobile = window.matchMedia('(max-width: 53.75em)');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => entry.target.classList.toggle('is-active', entry.intersectionRatio >= 0.6));
  }, { root: row, threshold: [0, 0.6, 1] });
  function sync() {
    if (mobile.matches) {
      row.classList.add('has-active');
      cards.forEach((card) => observer.observe(card));
    } else {
      observer.disconnect();
      row.classList.remove('has-active');
      cards.forEach((card) => card.classList.remove('is-active'));
    }
  }
  mobile.addEventListener('change', sync);
  sync();
})();

// Carrusel "Más proyectos": al hacer scroll las tarjetas avanzan por el arco y las que salen por un lado vuelven por el otro.
// Las flechas de las esquinas superiores lo mueven una posición hacia atrás o hacia adelante.
(function initMoreArc() {
  const arc = document.querySelector('.more-arc');
  if (!arc || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const cards = [...arc.children];
  const n = cards.length;
  const center = (n - 1) / 2;
  const SLOTS = 4; // cuántas posiciones avanza el carrusel mientras la sección cruza la pantalla
  const GAP = 8; // separación visible entre tarjetas, en px
  const TURN = 22 * Math.PI / 180; // giro por posición (igual que --arc-turn en CSS)
  const DEPTH = 650; // distancia de la perspectiva (igual que perspective en CSS)
  // Geometría de la tarjeta en la posición t (t >= 0, a la derecha del centro): medio ancho proyectado sin perspectiva (a)
  // y factor de perspectiva de su borde interior (cL) y exterior (cR), que queda más cerca y se ve más grande.
  function geom(t, h) {
    const w = h * 0.78 * (0.82 + 0.07 * t * t);
    const phi = -TURN * t;
    const half = w / 2;
    return { a: half * Math.cos(phi), cL: DEPTH / (DEPTH - half * Math.sin(phi)), cR: DEPTH / (DEPTH + half * Math.sin(phi)) };
  }
  // Centro de la tarjeta en k: cada tarjeta se ubica a 8 px (en pantalla) del borde exterior de la anterior hacia el centro.
  function offsetFor(k, h) {
    const t = Math.abs(k);
    const base = t % 1;           // parte fraccionaria: entre el centro y la primera posición se interpola
    const steps = Math.round(t - base);
    const next = (x, tPrev) => {   // centro de la tarjeta en tPrev + 1, a 8 px de la tarjeta en tPrev
      const gp = geom(tPrev, h);
      const gc = geom(tPrev + 1, h);
      return ((x + gp.a) * gp.cR + GAP) / gc.cL + gc.a;
    };
    let x = base * next(0, 0);
    for (let i = 0; i < steps; i += 1) x = next(x, base + i);
    return Math.sign(k) * x;
  }
  const wrap = (k) => { const w = ((k % n) + n) % n; return w >= n / 2 ? w - n : w; };
  let scrollShift = 0;
  let extra = 0;        // desplazamiento sumado con las flechas (en posiciones)
  let extraTarget = 0;
  arc.classList.add('is-live');

  function render() {
    const h = arc.clientHeight / 1.6; // --arc-h en px
    cards.forEach((card, i) => {
      const k = wrap(i - center - scrollShift - extra);
      card.style.setProperty('--k', k.toFixed(3));
      card.style.setProperty('--x', `${offsetFor(k, h).toFixed(1)}px`);
    });
  }
  function readScroll() {
    const r = arc.getBoundingClientRect();
    const p = Math.min(1, Math.max(0, (window.innerHeight - r.top) / (window.innerHeight + r.height)));
    scrollShift = p * SLOTS;
  }
  // Movimiento suave hacia la posición elegida con las flechas
  let animating = false;
  function tick() {
    extra += (extraTarget - extra) * 0.14;
    const done = Math.abs(extraTarget - extra) < 0.002;
    if (done) extra = extraTarget;
    render();
    if (done) animating = false; else requestAnimationFrame(tick);
  }
  function move(step) {
    extraTarget += step;
    if (!animating) { animating = true; requestAnimationFrame(tick); }
  }
  const nav = arc.parentElement.querySelector('.more-nav');
  if (nav) {
    nav.hidden = false;
    nav.querySelector('.more-prev').addEventListener('click', () => move(-1));
    nav.querySelector('.more-next').addEventListener('click', () => move(1));
  }

  let ticking = false;
  const onScroll = () => {
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(() => { ticking = false; readScroll(); render(); });
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  readScroll();
  render();
})();

// Desplegable de Proyectos en la cabecera: el botón lo abre o cierra; Escape o un clic fuera lo cierran.
(function initNavSub() {
  document.querySelectorAll('.has-sub').forEach((item) => {
    const toggle = item.querySelector('.nav-sub-toggle');
    if (!toggle) return;
    const setOpen = (open) => { item.classList.toggle('is-open', open); toggle.setAttribute('aria-expanded', String(open)); };
    toggle.addEventListener('click', () => setOpen(!item.classList.contains('is-open')));
    item.addEventListener('keydown', (e) => { if (e.key === 'Escape' && item.classList.contains('is-open')) { setOpen(false); toggle.focus(); } });
    document.addEventListener('click', (e) => { if (!item.contains(e.target)) setOpen(false); });
  });
})();

// Proyectos: filtro por categoría (?cat=marcas | producto | logofolio). Sin JavaScript se ven todos.
(function initProjectFilter() {
  const tabs = document.querySelector('.filter-tabs');
  if (!tabs) return;
  const valid = ['marcas', 'producto', 'logofolio'];
  const param = new URLSearchParams(window.location.search).get('cat');
  const cat = valid.includes(param) ? param : 'todos';

  tabs.querySelectorAll('a[data-cat]').forEach((a) => {
    if (a.dataset.cat === cat) a.setAttribute('aria-current', 'page');
    else a.removeAttribute('aria-current');
  });

  const showcase = document.querySelector('.showcase');
  const logofolio = document.getElementById('logofolio');
  if (showcase) showcase.hidden = cat === 'logofolio';
  document.querySelectorAll('#logofolio, .logofolio-extra').forEach((node) => { node.hidden = cat === 'marcas' || cat === 'producto'; });

  if (cat === 'marcas' || cat === 'producto') {
    document.querySelectorAll('.showcase-item[data-cats], .showcase-index li[data-cats]').forEach((node) => {
      node.hidden = !node.dataset.cats.split(' ').includes(cat);
    });
  }
  // Numeración correlativa de los proyectos visibles (en el índice y en cada proyecto).
  let n = 0;
  document.querySelectorAll('.showcase-item').forEach((item) => {
    if (item.hidden) return;
    n += 1;
    const num = String(n).padStart(2, '0');
    const tag = item.querySelector('.numtag');
    if (tag) tag.textContent = num;
    const idx = document.querySelector(`.showcase-index a[href="#${item.id}"] .showcase-num`);
    if (idx) idx.textContent = num;
  });
  if (cat === 'logofolio' && logofolio) logofolio.scrollIntoView({ block: 'start' });
})();

// Logofolio: genera los mosaicos de vidrio y ubica cada logo en su celda (misma técnica que AuditorWeb).
(function initLogofolio() {
  const section = document.getElementById('logofolio');
  const layer = section && section.querySelector('.tile-bg');
  if (!layer) return;
  const cells = [...section.querySelectorAll('.logo-cell')];

  function build() {
    const cs = getComputedStyle(section);
    const cols = parseInt(cs.getPropertyValue('--cols'), 10) || 3;
    const rows = Math.ceil(cells.length / cols);
    const key = `${cols}x${rows}`;
    if (layer.dataset.key === key) return;
    layer.dataset.key = key;
    section.style.setProperty('--rows', String(rows));
    const tiles = [];
    for (let r = 1; r <= rows + 2; r += 1) {
      for (let c = 1; c <= cols + 2; c += 1) {
        const tile = document.createElement('span');
        tile.style.gridArea = `${r} / ${c}`;
        tiles.push(tile);
      }
    }
    layer.replaceChildren(...tiles);
    cells.forEach((cell, i) => { cell.style.gridArea = `${2 + Math.floor(i / cols)} / ${2 + (i % cols)}`; });
    section.classList.add('is-tiled');
  }

  build();
  window.addEventListener('resize', build);
})();

// Pantalla de carga: se retira cuando terminó la firma (≈2,6 s desde la navegación) y la página cargó.
(function initLoader() {
  const root = document.documentElement;
  if (!root.classList.contains('is-loading')) return;
  const MIN_MS = 2600;
  let finished = false;
  const finish = () => {
    if (finished) return;
    finished = true;
    root.classList.add('is-loaded');
    try { sessionStorage.setItem('intro', '1'); } catch { /* sin almacenamiento */ }
    setTimeout(() => root.classList.remove('is-loading', 'is-loaded'), 700);
  };
  const whenReady = () => setTimeout(finish, Math.max(0, MIN_MS - performance.now()));
  if (document.readyState === 'complete') whenReady();
  else window.addEventListener('load', whenReady, { once: true });
  setTimeout(finish, 6000); // respaldo si la carga se demora
})();

// Inicio: una sola línea recorre la página. En el hero se dibuja sola al entrar (después de la pantalla de carga);
// desde ahí avanza con el scroll hasta una línea de lectura (60 % del alto de la ventana) y una punta redondeada marca
// siempre el extremo dibujado, pasando de una sección a la siguiente sin saltos.
// Sin JavaScript o con "reducir movimiento", cada tramo usa su animación CSS (o se ve completo) y no hay punta.
(function initHomeThread() {
  const hero = document.querySelector('.pl-hero');
  if (!hero || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const root = document.documentElement;
  const head = hero.querySelector('.pl-head');
  if (head) document.body.append(head); // fija en la ventana, sobre todas las secciones
  const DURATION = 2600; // ms que tarda en dibujarse la línea del hero
  const SCAN = 0.6; // línea de lectura, como fracción del alto de la ventana
  let heroP = 0;
  let heroSeg = null; // tramo del hero (para seguir con el scroll)
  let heroStop = 1; // fracción hasta donde se dibuja sola al cargar
  let autoDone = false;
  let chain = []; // tramos de las secciones siguientes, en orden

  const visible = (scope) => [...scope.querySelectorAll('.pl-thread')].filter((svg) => svg.getBoundingClientRect().width > 0);

  // Las líneas vienen estiradas (viewBox fijo). Se reescalan al tamaño real de su sección para que el avance del trazo
  // y la posición de la punta se midan en la misma escala. mapY permite mover alturas (el subrayado del hero).
  function fitSvg(svg, w, h, mapY) {
    if (!svg.dataset.view) svg.dataset.view = svg.getAttribute('viewBox');
    const [, , vw, vh] = svg.dataset.view.split(' ').map(Number);
    const my = mapY || ((y) => (y * h) / vh);
    svg.setAttribute('viewBox', `0 0 ${w} ${h}`);
    svg.querySelectorAll('path').forEach((path) => {
      if (!path.dataset.d) path.dataset.d = path.getAttribute('d');
      let i = 0;
      path.setAttribute('d', path.dataset.d.replace(/-?\d+(?:\.\d+)?/g, (n) => (i++ % 2 === 0 ? (n * w) / vw : my(+n)).toFixed(1)));
    });
  }

  // Línea del hero construida sobre el titular (boceto de Luis): baja con una curva amplia, pasa por dentro de la O de
  // "DISEÑO", sale por arriba y da la vuelta, subraya "DESEAN" con una recta limpia bajo su línea base, hace un lazo
  // abajo a la derecha y sale por abajo hacia la sección siguiente. Se suaviza (smooth) y se recalcula si el titular se mueve.
  // Al cargar se dibuja sola hasta unos 10vh antes del final del hero; el resto lo completa el scroll.
  const EXIT = { desk: 0.69, mob: 0.5 }; // salida por abajo, como fracción del ancho (donde empieza la línea siguiente)
  const STEP = 18; // px entre puntos al suavizar (como _suave en el generador)

  // Suaviza y simplifica un trazado: lo recorre en puntos equidistantes y lo vuelve a trazar como B-spline cúbica
  // (sin quiebres ni saltos de curvatura). Usa `probe` (un <path>) para medir.
  function smooth(d, probe) {
    probe.setAttribute('d', d);
    const L = probe.getTotalLength();
    const n = Math.max(2, Math.round(L / STEP));
    const pts = [];
    for (let i = 0; i <= n; i += 1) { const p = probe.getPointAtLength((L * i) / n); pts.push([p.x, p.y]); }
    const cp = [pts[0], pts[0], ...pts, pts[n], pts[n]];
    const f = (v) => v.toFixed(1);
    let out = `M${f(pts[0][0])} ${f(pts[0][1])}`;
    for (let i = 0; i < cp.length - 3; i += 1) {
      const [, p1, p2, p3] = cp.slice(i, i + 4);
      out += ` C${f((2 * p1[0] + p2[0]) / 3)} ${f((2 * p1[1] + p2[1]) / 3)} ${f((p1[0] + 2 * p2[0]) / 3)} ${f((p1[1] + 2 * p2[1]) / 3)} ${f((p1[0] + 4 * p2[0] + p3[0]) / 6)} ${f((p1[1] + 4 * p2[1] + p3[1]) / 6)}`;
    }
    return out;
  }
  function heroPath() {
    const box = hero.getBoundingClientRect();
    const w = box.width; const h = box.height;
    const oEl = hero.querySelector('.pl-o'); const uEl = hero.querySelector('.pl-u'); const bEl = hero.querySelector('.pl-base');
    if (!oEl || !uEl || !bEl) return;
    const or = oEl.getBoundingClientRect(); const ur = uEl.getBoundingClientRect(); const br = bEl.getBoundingClientRect();
    const fs = parseFloat(getComputedStyle(uEl).fontSize);
    const o = or.height * 0.62; // alto de la O (la caja incluye espacio sobre y bajo las mayúsculas)
    const ox = or.left + or.width / 2 - box.left;
    const oy = br.top - box.top - (ur.bottom - or.bottom) - o * 0.5; // centro de la O: su línea base menos media letra
    const uy = br.top - box.top + fs * 0.1; // subrayado, justo bajo la línea base de "desean"
    const dl = ur.left - box.left; const dr = ur.right - box.left;
    const mob = window.matchMedia('(max-width: 40em)').matches;
    const xe = w * (mob ? EXIT.mob : EXIT.desk);
    const x0 = Math.max(16, ox - 2.6 * o);
    // El lazo inferior se corre a la izquierda si no cabe en la pantalla
    const shift = Math.min(0, w - 14 - (dr + 1.44 * fs));
    const L = (x, y) => `${(x).toFixed(1)} ${(y).toFixed(1)}`;
    const R = (k) => dr + k * fs + shift;
    const d = [
      `M${L(x0, 0)}`,
      `C${L(x0 + 0.05 * o, oy * 0.45)} ${L(ox - 1.8 * o, oy - 0.9 * o)} ${L(ox - 0.9 * o, oy - 0.45 * o)}`,
      `C${L(ox - 0.45 * o, oy - 0.2 * o)} ${L(ox - 0.15 * o, oy)} ${L(ox + 0.1 * o, oy - 0.05 * o)}`,
      `C${L(ox + 0.6 * o, oy - 0.1 * o)} ${L(ox + 0.85 * o, oy - 0.7 * o)} ${L(ox + 0.7 * o, oy - 1.05 * o)}`,
      `C${L(ox + 0.55 * o, oy - 1.35 * o)} ${L(ox + 0.1 * o, oy - 1.45 * o)} ${L(ox - 0.25 * o, oy - 1.3 * o)}`,
      `C${L(ox - 0.9 * o, oy - 1.05 * o)} ${L(ox - 2.0 * o, oy - 0.4 * o)} ${L(ox - 2.25 * o, oy + 0.45 * o)}`,
      `C${L(ox - 2.45 * o, uy - 0.2 * fs)} ${L(dl - 0.9 * fs, uy)} ${L(dl - 0.35 * fs, uy)}`,
      // Subrayado recto de "desean"
      `C${L(dl + 0.2 * fs, uy)} ${L(dr + 0.1 * fs, uy)} ${L(Math.max(dr + 0.15 * fs, R(0.67)), uy)}`,
      // Bajada y lazo inferior derecho
      `C${L(R(1.0), uy)} ${L(R(1.28), uy + 0.45 * fs)} ${L(R(1.22), uy + 0.85 * fs)}`,
      `C${L(R(1.16), uy + 1.2 * fs)} ${L(R(0.85), uy + 1.25 * fs)} ${L(R(0.6), uy + 1.2 * fs)}`,
      `C${L(R(0.25), uy + 1.14 * fs)} ${L(R(0.0), uy + 0.95 * fs)} ${L(R(0.08), uy + 0.78 * fs)}`,
      `C${L(R(0.18), uy + 0.6 * fs)} ${L(R(0.7), uy + 0.62 * fs)} ${L(R(1.0), uy + 0.9 * fs)}`,
      `C${L(R(1.25), uy + 1.12 * fs)} ${L(R(1.42), uy + 1.4 * fs)} ${L(R(1.44), uy + 1.7 * fs)}`,
      `C${L(R(1.46), uy + 1.7 * fs + (h - uy - 1.7 * fs) * 0.45)} ${L(xe, h - (h - uy - 1.7 * fs) * 0.4)} ${L(xe, h)}`,
    ].join(' ');
    const probe = hero.querySelector('.pl-thread path');
    const ds = probe ? smooth(d, probe) : d;
    // Capa delantera: solo el tramo que entra a la O por su borde superior izquierdo (ahí la línea pasa por encima)
    const clip = `inset(${(oy - 0.75 * o).toFixed(1)}px ${(w - ox).toFixed(1)}px ${(h - (oy + 0.15 * o)).toFixed(1)}px ${(or.left - box.left - 0.35 * o).toFixed(1)}px)`;
    hero.querySelectorAll('.pl-thread').forEach((svg) => {
      svg.setAttribute('viewBox', `0 0 ${w} ${h}`);
      svg.querySelectorAll('path').forEach((path) => path.setAttribute('d', ds));
      if (svg.classList.contains('pl-thread-front')) svg.style.clipPath = clip;
    });
  }

  // El mundo de las ideas: la línea baja y se enrolla en espiral en la botella central (boceto de Luis): cruza por delante,
  // da la vuelta por la derecha, vuelve por detrás y cruza otra vez por delante en diagonal antes de salir hacia abajo.
  // Se mide el atomizador en cada cuadro (crece con el scroll); la capa delantera se recorta a los dos cruces por delante.
  function ideasPath(seg) {
    const { sec, back, front } = seg.spiral;
    const bottle = sec.querySelector('.ideas-item-spray');
    if (!bottle) return;
    const box = sec.getBoundingClientRect(); const r = bottle.getBoundingClientRect();
    const w = box.width; const h = box.height;
    const mob = window.matchMedia('(max-width: 40em)').matches;
    const xs = w * (mob ? EXIT.mob : EXIT.desk); // entra donde terminó la línea del hero
    const xe = w * 0.5; // sale al centro, donde empieza la línea de Sistemas
    // Cuerpo de la botella (sin el gatillo)
    const bt = r.top - box.top + r.height * 0.36; const bb = r.bottom - box.top - r.height * 0.04; const bh = bb - bt;
    const cx = r.left - box.left + r.width / 2; const bw = r.width * 0.78;
    const L0 = cx - bw / 2; const R0 = cx + bw / 2; const m = bw * 0.22; const k = bh * 0.1;
    const y1 = bt + bh * 0.12; const y2 = bt + bh * 0.4; const s = bh * 0.1;
    const y3 = bt + bh * 0.6; const y4 = bt + bh * 0.86;
    const P = (x, y) => `${x.toFixed(1)} ${y.toFixed(1)}`;
    const d = [
      `M${P(xs, 0)}`,
      `C${P(xs, y1 * 0.4)} ${P(L0 - m * 2.2, y1 - bh * 0.5)} ${P(L0 - m, y1)}`, // baja por detrás hasta el lado izquierdo
      `C${P(L0 + bw * 0.3, y1 + s * 0.6 + k)} ${P(R0 - bw * 0.3, y1 + s * 0.6 + k)} ${P(R0 + m, y1 + s)}`, // cruce por delante
      `C${P(R0 + m * 2, y1 + s + bh * 0.08)} ${P(R0 + m * 2, y2 - bh * 0.06)} ${P(R0 + m, y2)}`, // vuelta por la derecha
      `C${P(R0 - bw * 0.3, y2 - k)} ${P(L0 + bw * 0.3, y2 + s - k)} ${P(L0 - m, y2 + s)}`, // cruce por detrás
      `C${P(L0 - m * 2, y2 + s + bh * 0.05)} ${P(L0 - m * 1.6, y3 - bh * 0.06)} ${P(L0 - m * 0.6, y3)}`, // vuelta por la izquierda
      `C${P(L0 + bw * 0.3, y3 + k)} ${P(R0 - bw * 0.3, y4 - k * 0.5)} ${P(R0 + m, y4)}`, // cruce por delante en diagonal
      `C${P(R0 + m * 2.2, y4 + bh * 0.12)} ${P(xe, h - (h - bb) * 0.45)} ${P(xe, h)}`, // sale hacia abajo
    ].join(' ');
    const ds = smooth(d, seg.path);
    [back, front].forEach((svg) => {
      if (!svg) return;
      svg.setAttribute('viewBox', `0 0 ${w} ${h}`);
      svg.querySelectorAll('path').forEach((path) => path.setAttribute('d', ds));
    });
    seg.t = table(seg.path);
    // Capa delantera: todo menos la silueta de la botella central (cuello y cuerpo); dentro de ella solo
    // se ven el primer cruce y el cruce en diagonal. Las demás piezas del collage quedan por detrás de la línea.
    if (front) {
      const f = (v) => v.toFixed(1);
      const top = r.top - box.top; const nx0 = cx - r.width * 0.25; const nx1 = cx + r.width * 0.25;
      const silueta = `M${f(nx0)} ${f(top)} H${f(nx1)} V${f(bt)} H${f(R0)} V${f(bb)} H${f(L0)} V${f(bt)} H${f(nx0)} Z`;
      const franja = (y0, y1b) => `M${f(L0 + 1)} ${f(y0)} H${f(R0 - 1)} V${f(y1b)} H${f(L0 + 1)} Z`;
      front.style.clipPath = `path(evenodd, 'M0 0 H${f(w)} V${f(h)} H0 Z ${silueta} ${franja(y1 - k, y1 + s + k * 1.2)} ${franja(y3 - k * 0.5, Math.min(bb - 1, y4 + k * 1.2))}')`;
    }
  }

  // Tabla de cada tramo: largo recorrido y altura máxima alcanzada hasta ese punto (para dibujar hasta la línea de lectura)
  function table(path) {
    const L = path.getTotalLength();
    const n = Math.max(60, Math.min(500, Math.round(L / 6)));
    const lens = []; const maxY = []; const pts = [];
    let top = -Infinity;
    for (let i = 0; i <= n; i += 1) {
      const pt = path.getPointAtLength((L * i) / n);
      top = Math.max(top, pt.y);
      lens.push((L * i) / n); maxY.push(top); pts.push(pt);
    }
    return { L, lens, maxY, pts };
  }

  function build() {
    heroPath();
    heroStopAt();
    chain = [];
    document.querySelectorAll('.pl-sec:not(.pl-hero)').forEach((sec) => {
      const box = sec.getBoundingClientRect();
      const svgs = visible(sec);
      svgs.forEach((svg) => fitSvg(svg, box.width, box.height));
      if (!svgs.length) return;
      const back = svgs.find((svg) => !svg.classList.contains('pl-thread-front')) || svgs[0];
      const front = svgs.find((svg) => svg.classList.contains('pl-thread-front'));
      const paths = [...back.querySelectorAll('path')];
      const firma = sec.querySelector('.pl-firma path');
      // En la firma, la línea entra, escribe "luis" y sale; en Sistemas, el segundo tramo es la otra mitad del óvalo
      const ordered = firma ? [paths[0], firma, ...paths.slice(1)] : paths;
      // data-thread="fit": la línea se completa cuando la sección queda centrada (para ver su dibujo entero, p. ej. las flechas)
      const fit = sec.dataset.thread === 'fit' ? sec : null;
      const segs = ordered.map((path, i) => ({ path, fit, main: !(sec.classList.contains('pl-caps') && i === 1), t: table(path), marks: [],
        twin: front ? front.querySelectorAll('path')[i] : null, spiral: sec.classList.contains('pl-ideas') ? { sec, back, front } : null }));
      chain.push(...segs);
      // Elementos que aparecen cuando la línea pasa por ellos (Sistemas: disciplinas por su punto; el título, al entrar al óvalo)
      const items = [...sec.querySelectorAll('.pl-cap .pl-dot')].map((dot) => [dot.closest('.pl-cap'), dot.getBoundingClientRect()]);
      const title = sec.querySelector('.pl-caps-title');
      if (title) { const r = title.getBoundingClientRect(); items.push([title, { left: r.left + r.width / 2, top: r.top, width: 0, height: 0 }]); }
      items.forEach(([el, r]) => {
        let best = null;
        segs.forEach((seg) => {
          const m = seg.path.getScreenCTM();
          if (!m) return;
          const inv = m.inverse();
          const x = r.left + r.width / 2; const y = r.top + r.height / 2;
          const ux = inv.a * x + inv.c * y + inv.e; const uy = inv.b * x + inv.d * y + inv.f;
          seg.t.pts.forEach((pt, k) => {
            const dd = (pt.x - ux) ** 2 + (pt.y - uy) ** 2;
            if (!best || dd < best.dd) best = { dd, seg, at: seg.t.lens[k] / seg.t.L };
          });
        });
        if (best) best.seg.marks.push({ el, at: best.at });
      });
    });
  }

  function progressOf(seg) {
    if (seg.fit) {
      const r = seg.fit.getBoundingClientRect();
      const startTop = window.innerHeight * SCAN; // empieza cuando la sección llega a la línea de lectura
      const endTop = Math.max(0, (window.innerHeight - r.height) / 2); // termina con la sección centrada
      return Math.min(1, Math.max(0, (startTop - r.top) / Math.max(1, startTop - endTop)));
    }
    const m = seg.path.getScreenCTM();
    if (!m || !m.d) return 0;
    const y = (window.innerHeight * SCAN - m.f) / m.d; // línea de lectura en coordenadas del tramo
    const { lens, maxY, L } = seg.t;
    if (y <= maxY[0]) return 0;
    if (y >= maxY[maxY.length - 1]) return 1;
    let lo = 0; let hi = maxY.length - 1;
    while (hi - lo > 1) { const mid = (lo + hi) >> 1; if (maxY[mid] <= y) lo = mid; else hi = mid; }
    return lens[lo] / L;
  }

  function place(path, p) {
    if (!head || !path) return;
    const pt = path.getPointAtLength(path.getTotalLength() * p);
    const m = path.getScreenCTM();
    head.style.setProperty('--x', `${pt.x * m.a + pt.y * m.c + m.e}px`);
    head.style.setProperty('--y', `${pt.x * m.b + pt.y * m.d + m.f}px`);
  }

  // Dónde se detiene el dibujo automático: unos 10vh antes del borde inferior del hero
  function heroStopAt() {
    const path = visible(hero)[0] && visible(hero)[0].querySelector('path');
    if (!path) return;
    heroSeg = { path, t: table(path) };
    const limit = hero.getBoundingClientRect().height - window.innerHeight * 0.1;
    const { lens, maxY, L } = heroSeg.t;
    let k = 0;
    while (k < maxY.length - 1 && maxY[k + 1] <= limit) k += 1;
    heroStop = lens[k] / L;
  }

  function draw() {
    const heroSvgs = visible(hero);
    if (autoDone && heroSeg) heroP = Math.max(heroStop, progressOf(heroSeg));
    heroSvgs.forEach((svg) => svg.querySelectorAll('path').forEach((path) => { path.style.strokeDashoffset = String(1 - heroP); }));
    let front = heroSvgs[0] ? { path: heroSvgs[0].querySelector('path'), p: heroP } : null;
    chain.forEach((seg) => {
      if (seg.spiral) ideasPath(seg);
      const p = heroP < 1 ? 0 : progressOf(seg); // las secciones esperan a que el hero esté completo
      seg.path.style.strokeDashoffset = String(1 - p);
      if (seg.twin) seg.twin.style.strokeDashoffset = String(1 - p);
      seg.marks.forEach((mk) => mk.el.classList.toggle('is-on', p >= mk.at - 0.01));
      if (seg.main && p > 0) front = { path: seg.path, p };
    });
    if (front) place(front.path, front.p);
  }

  // Dibujo automático del hero con aceleración suave; espera a que se retire la pantalla de carga
  const ease = (t) => (t < 0.5 ? 4 * t * t * t : 1 - (-2 * t + 2) ** 3 / 2);
  let start = null;
  function tick(now) {
    if (root.classList.contains('is-loading')) { requestAnimationFrame(tick); return; }
    if (start === null) start = now;
    const t = Math.min(1, (now - start) / DURATION);
    heroPath();
    heroStopAt();
    heroP = ease(t) * heroStop;
    if (t >= 1) autoDone = true;
    draw();
    if (t < 1) requestAnimationFrame(tick);
  }

  let pending = false;
  const request = () => { if (!pending) { pending = true; requestAnimationFrame(() => { pending = false; draw(); }); } };

  root.classList.add('thread-js');
  hero.classList.add('is-live');
  build();
  draw();
  requestAnimationFrame(tick);
  window.addEventListener('scroll', request, { passive: true });
  window.addEventListener('resize', () => { build(); request(); });
  window.addEventListener('load', () => { build(); request(); }); // las imágenes cambian el alto de las secciones
  window.addEventListener('pl:title-move', () => { heroPath(); heroStopAt(); request(); }); // el titular se desplaza con el scroll
})();

// Inicio: el cursor es un círculo del color destacado que sigue al puntero y crece sobre enlaces y botones.
// Solo con mouse o trackpad; en pantallas táctiles se mantiene el comportamiento normal.
(function initHomeCursor() {
  if (!document.querySelector('.pl-hero') || !window.matchMedia('(hover: hover) and (pointer: fine)').matches) return;
  const dot = document.createElement('span');
  dot.className = 'pl-cursor';
  dot.setAttribute('aria-hidden', 'true');
  document.body.append(dot);
  document.documentElement.classList.add('has-cursor');
  const still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let x = -100; let y = -100; let cx = x; let cy = y; let running = false;
  function frame() {
    cx += (x - cx) * (still ? 1 : 0.28);
    cy += (y - cy) * (still ? 1 : 0.28);
    dot.style.transform = `translate3d(${cx}px, ${cy}px, 0)`;
    running = Math.abs(x - cx) > 0.1 || Math.abs(y - cy) > 0.1;
    if (running) requestAnimationFrame(frame);
  }
  window.addEventListener('mousemove', (e) => {
    x = e.clientX; y = e.clientY;
    if (!dot.classList.contains('is-visible')) { cx = x; cy = y; dot.classList.add('is-visible'); }
    dot.classList.toggle('is-hover', !!e.target.closest('a, button, summary, [role="button"], label'));
    if (!running) { running = true; requestAnimationFrame(frame); }
  }, { passive: true });
  document.addEventListener('mouseleave', () => dot.classList.remove('is-visible'));
})();

// Inicio: las líneas del titular se desplazan en horizontal con el scroll, siguiéndolo con suavidad
// (la primera y la tercera hacia la izquierda; la marcada con data-dir="1", hacia la derecha).
(function initHomeTitle() {
  const lines = [...document.querySelectorAll('.pl-hero-title .pl-line-in')];
  if (!lines.length || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const SPEED = 0.07; // px de desplazamiento por px de scroll
  let current = 0;
  let running = false;
  function frame() {
    const target = Math.min(window.scrollY, window.innerHeight * 1.5) * SPEED;
    current += (target - current) * 0.12;
    if (Math.abs(target - current) < 0.05) current = target;
    lines.forEach((line) => { line.style.transform = `translate3d(${(line.dataset.dir === '1' ? 1 : -1) * current}px, 0, 0)`; });
    window.dispatchEvent(new Event('pl:title-move'));
    running = current !== target;
    if (running) requestAnimationFrame(frame);
  }
  window.addEventListener('scroll', () => { if (!running) { running = true; requestAnimationFrame(frame); } }, { passive: true });
})();
