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
  function fitSvg(svg, w, h, mapY, dx = 0) {
    if (!svg.dataset.view) svg.dataset.view = svg.getAttribute('viewBox');
    const [, , vw, vh] = svg.dataset.view.split(' ').map(Number);
    const my = mapY || ((y) => (y * h) / vh);
    svg.setAttribute('viewBox', `0 0 ${w} ${h}`);
    svg.querySelectorAll('path').forEach((path) => {
      if (!path.dataset.d) path.dataset.d = path.getAttribute('d');
      let i = 0;
      path.setAttribute('d', path.dataset.d.replace(/-?\d+(?:\.\d+)?/g, (n) => (i++ % 2 === 0 ? (n * w) / vw + dx : my(+n)).toFixed(1)));
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
  // Espiral alrededor de la botella central: un resorte de dos vueltas, visto con una leve inclinación para que cada vuelta
  // sea una elipse ordenada. Por detrás de la botella va todo el trazado (la botella lo tapa); por delante, solo los tramos
  // de frente (seno > 0), que se muestran con una máscara sobre el mismo trazado (así la animación sigue en sincronía).
  function bezier(p0, p1, p2, p3, n) {
    const puntos = [];
    for (let k = 0; k <= n; k += 1) {
      const t = k / n; const u = 1 - t;
      puntos.push([u * u * u * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t * t * t * p3[0],
        u * u * u * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t * t * t * p3[1]]);
    }
    return puntos;
  }

  function ideasPath(seg) {
    const { sec, back, front } = seg.spiral;
    const bottle = sec.querySelector('.ideas-item-spray');
    if (!bottle) return;
    const box = (sec.querySelector('.ideas-pin') || sec).getBoundingClientRect();
    const w = box.width; const h = box.height;
    // La espiral se calcula solo cuando cambia el tamaño de la pantalla; con la botella a tamaño final, para que su largo no cambie
    const clave = `${Math.round(w)}x${Math.round(h)}`;
    if (seg.clave === clave) return;
    seg.clave = clave;
    const guardado = bottle.style.animationDelay;
    bottle.style.animationDelay = '-1000ms';
    const r = bottle.getBoundingClientRect();
    bottle.style.animationDelay = guardado;
    const mob = window.matchMedia('(max-width: 40em)').matches;
    // Entra exactamente donde termina la línea del hero (misma coordenada en pantalla), para que no haya quiebre
    let xs = w * (mob ? EXIT.mob : EXIT.desk);
    if (heroSeg) {
      const hp = heroSeg.path; const fin = hp.getPointAtLength(hp.getTotalLength()); const m = hp.getScreenCTM();
      if (m) { const xPantalla = m.a * fin.x + m.c * fin.y + m.e; if (xPantalla > box.left && xPantalla < box.right) xs = xPantalla - box.left; }
    }
    const xr = w * (mob ? 0.82 : 0.75); // la salida baja por la derecha (lejos del texto) y vuelve al centro al final
    const bt = r.top - box.top + r.height * 0.36; const bb = r.bottom - box.top - r.height * 0.04; const bh = bb - bt;
    const cx = r.left - box.left + r.width / 2; const bw = r.width * 0.78;
    const R = r.width * 0.95; // radio horizontal del resorte: cada vuelta sobresale a ambos lados de la botella
    const y1 = bt + bh * 0.1; const y2 = bb - bh * 0.02; // altura de la primera y de la última vuelta
    const e = bh * 0.05; // inclinación de la vista: cada vuelta se ve como una elipse
    const VUELTAS = 3;
    const th0 = Math.PI; const th1 = th0 + 2 * Math.PI * VUELTAS;
    const punto = (th) => {
      const f = (th - th0) / (th1 - th0);
      return [cx + R * Math.cos(th), y1 + (y2 - y1) * f + e * Math.sin(th)];
    };
    const P0 = punto(th0); const P1 = punto(th1);
    const entrada = bezier([xs, 0], [xs, y1 * 0.5], [P0[0], P0[1] - bh * 0.12], P0, 30);
    // Desde la última vuelta, la salida va directo a la derecha y baja por ese lado, sin volver al centro
    const salida = bezier(P1, [(P1[0] + xr) / 2, P1[1]], [xr, P1[1]], [xr, P1[1] + (h - P1[1]) * 0.3], 30)
      .concat(bezier([xr, P1[1] + (h - P1[1]) * 0.3], [xr, P1[1] + (h - P1[1]) * 0.65], [xr, h * 0.9], [xr, h], 30).slice(1));
    const N = 80 * VUELTAS;
    const resorte = [];
    for (let i = 0; i <= N; i += 1) {
      const th = th0 + ((th1 - th0) * i) / N;
      resorte.push({ p: punto(th), frente: Math.sin(th) > 0 });
    }
    // Muestreo denso (decenas de puntos por vuelta): el trazo es fluido sin suavizado adicional
    const aTrazo = (puntos) => 'M' + puntos.map((q) => `${q[0].toFixed(1)} ${q[1].toFixed(1)}`).join(' L ');
    const completo = aTrazo([...entrada, ...resorte.map((x) => x.p), ...salida.slice(1)]);
    // Fracción del trazo que corresponde a la entrada (desde el hero): se dibuja al llegar a la sección
    const largo = (pts) => pts.reduce((acc, q, i) => (i ? acc + Math.hypot(q[0] - pts[i - 1][0], q[1] - pts[i - 1][1]) : 0), 0);
    seg.entrada = largo(entrada) / Math.max(1, largo([...entrada, ...resorte.map((x) => x.p), ...salida.slice(1)]));
    [back, front].forEach((svg) => {
      if (!svg) return;
      svg.setAttribute('viewBox', `0 0 ${w} ${h}`);
      svg.querySelectorAll('path').forEach((path) => path.setAttribute('d', completo));
    });
    seg.t = table(seg.path);

    // Tramos de frente: se agrupan las muestras consecutivas de seno positivo (con un punto de margen a cada lado)
    if (front) {
      const tramos = [];
      let actual = null;
      resorte.forEach((x, i) => {
        if (x.frente) {
          if (!actual) { actual = []; if (i > 0) actual.push(resorte[i - 1].p); }
          actual.push(x.p);
        } else if (actual) {
          actual.push(x.p); tramos.push(actual); actual = null;
        }
      });
      if (actual) tramos.push(actual);
      const svgNS = 'http://www.w3.org/2000/svg';
      if (!front._mascara) {
        const defs = document.createElementNS(svgNS, 'defs');
        const mascara = document.createElementNS(svgNS, 'mask');
        mascara.setAttribute('id', 'ideas-frente');
        mascara.setAttribute('maskUnits', 'userSpaceOnUse');
        mascara.setAttribute('x', '0'); mascara.setAttribute('y', '0');
        defs.append(mascara);
        front.prepend(defs);
        front.querySelectorAll('path').forEach((path) => path.setAttribute('mask', 'url(#ideas-frente)'));
        front._mascara = mascara;
        front.style.clipPath = 'none';
      }
      front._mascara.setAttribute('width', w);
      front._mascara.setAttribute('height', h);
      front._mascara.replaceChildren(...tramos.map((puntos) => {
        const trazo = document.createElementNS(svgNS, 'path');
        trazo.setAttribute('d', aTrazo(puntos));
        trazo.setAttribute('fill', 'none');
        trazo.setAttribute('stroke', '#fff');
        trazo.setAttribute('stroke-width', '14');
        trazo.setAttribute('stroke-linecap', 'round');
        trazo.setAttribute('vector-effect', 'non-scaling-stroke');
        return trazo;
      }));
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
    let finAnteriorX = null; // x en pantalla del punto final del trazo de la sección anterior
    document.querySelectorAll('.pl-sec:not(.pl-hero)').forEach((sec) => {
      const box = (sec.querySelector('.ideas-pin') || sec).getBoundingClientRect();
      const svgs = visible(sec);
      // Con .pl-stage, el dibujo (y entre 0 y 1000 del viewBox) se ajusta a ese bloque; las y negativas (de -500 a 0)
      // ocupan lo que hay encima de él (el título) y y = 1000 queda en el borde inferior de la sección
      const stage = sec.querySelector('.pl-stage');
      let mapY;
      if (stage) {
        const r = stage.getBoundingClientRect(); const top = r.top - box.top;
        mapY = (y) => (y < 0 ? Math.max(0, top * (1 + y / 500)) : y >= 1000 ? box.height : top + (y / 1000) * r.height);
      }
      svgs.forEach((svg) => fitSvg(svg, box.width, box.height, mapY));
      if (!svgs.length) return;
      // Continuidad: la entrada de la sección se alinea con el punto final de la sección anterior (en pantalla)
      const trazoBack = (svgs.find((svg) => !svg.classList.contains('pl-thread-front')) || svgs[0]).querySelector('path');
      const mBack = trazoBack.getScreenCTM();
      if (mBack && finAnteriorX !== null) {
        const ini = trazoBack.getPointAtLength(0);
        const delta = finAnteriorX - (mBack.a * ini.x + mBack.c * ini.y + mBack.e);
        if (Math.abs(delta) > 0.5 && Math.abs(delta) < 20) svgs.forEach((svg) => fitSvg(svg, box.width, box.height, mapY, delta));
      }
      const trazoFin = (svgs.find((svg) => !svg.classList.contains('pl-thread-front')) || svgs[0]).querySelector('path');
      const fin = trazoFin.getPointAtLength(trazoFin.getTotalLength()); const mFin = trazoFin.getScreenCTM();
      if (mFin) finAnteriorX = mFin.a * fin.x + mFin.c * fin.y + mFin.e;
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
      // Marca práctica (Marca y producto): cada cartel y su icono aparecen cuando la línea pasa por su flecha
      sec.querySelectorAll('.pl-cartel, .pl-icono').forEach((el) => items.push([el, el.getBoundingClientRect()]));
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
      // En móvil la sección es más alta que la pantalla: termina antes (a un cuarto de alto) para que la línea no se sienta lenta
      const movil = window.matchMedia('(max-width: 40em)').matches;
      const endTop = movil ? window.innerHeight * 0.25 : Math.max(0, (window.innerHeight - r.height) / 2); // termina con la sección centrada
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

  // Fijación de la sección de ideas: 0 cuando la sección llega arriba, 1 cuando termina (y la página puede seguir bajando)
  function ideasP() {
    const sec = document.getElementById('ideas');
    if (!sec) return 0;
    const recorrido = Math.max(1, sec.offsetHeight - window.innerHeight);
    return Math.min(1, Math.max(0, -sec.getBoundingClientRect().top / recorrido));
  }
  // Espiral: la entrada se dibuja al llegar a la sección; durante la fijación, el resto del trazo avanza con ella
  function ideasProgress(seg) {
    const f = seg.entrada || 0;
    const fijacion = ideasP();
    return fijacion > 0 ? f + (1 - f) * fijacion : Math.min(progressOf(seg), f);
  }
  // Rango de cada línea y de cada producto dentro de la fijación (0 a 1)
  // Cada línea se abre al mismo ritmo que el producto que está en su hueco (teléfono, cerveza y espray): el producto empuja el texto
  const IDEAS_LINEAS = [[0.25, 0.6], [0.4, 0.75], [0.55, 0.9]];
  const IDEAS_ITEMS = { 'ideas-item-phone': [0.25, 0.6], 'ideas-item-beer': [0.4, 0.75], 'ideas-item-spray': [0.55, 0.9] };
  // Ajusta el retraso negativo de cada animación (duración 1 s) para que avance con el progreso
  function scrubIdeas() {
    const sec = document.getElementById('ideas');
    if (!sec) return;
    const p = ideasP();
    const ajustar = (el, [a, b]) => {
      const q = Math.min(1, Math.max(0, (p - a) / (b - a)));
      el.style.animationDelay = `${-q * 1000}ms`;
    };
    sec.querySelectorAll('.ideas-line').forEach((linea, i) => {
      if (!IDEAS_LINEAS[i]) return;
      linea.querySelectorAll(':scope > span:first-child, :scope > span:last-child, .ideas-w1, .ideas-w2')
        .forEach((el) => ajustar(el, IDEAS_LINEAS[i]));
    });
    Object.entries(IDEAS_ITEMS).forEach(([clase, rango]) => {
      const el = sec.querySelector(`.${clase}`);
      if (el) ajustar(el, rango);
    });
  }

  function draw() {
    scrubIdeas();
    const heroSvgs = visible(hero);
    if (autoDone && heroSeg) heroP = Math.max(heroStop, progressOf(heroSeg));
    heroSvgs.forEach((svg) => svg.querySelectorAll('path').forEach((path) => { path.style.strokeDashoffset = String(1 - heroP); }));
    let front = heroSvgs[0] ? { path: heroSvgs[0].querySelector('path'), p: heroP } : null;
    chain.forEach((seg) => {
      if (seg.spiral) ideasPath(seg);
      const p = heroP < 1 ? 0 : (seg.spiral ? ideasProgress(seg) : progressOf(seg)); // las secciones esperan a que el hero esté completo
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

// Inicio: las líneas de los titulares animados (hero y contacto) se desplazan en horizontal con el scroll, siguiéndolo
// con suavidad (la primera y la tercera hacia la izquierda; la marcada con data-dir="1", hacia la derecha).
// El del hero se mueve desde el inicio de la página; los demás desde que entran en pantalla, y aparecen línea a línea.
(function initHomeTitle() {
  const titles = [...document.querySelectorAll('.pl-hero-title, .pl-anim-title')];
  if (!titles.length || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const SPEED = 0.07; // px de desplazamiento por px de scroll
  const groups = titles.map((el) => ({ el, hero: el.classList.contains('pl-hero-title'), lines: [...el.querySelectorAll('.pl-line-in')], current: 0 }));
  // Entrada línea a línea al aparecer en pantalla (el hero ya entra al cargar, por CSS)
  const later = groups.filter((g) => !g.hero).map((g) => g.el);
  if (later.length && 'IntersectionObserver' in window) {
    later.forEach((el) => el.classList.add('pl-reveal'));
    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); } });
    }, { threshold: 0.35 });
    later.forEach((el) => io.observe(el));
  }
  let running = false;
  function frame() {
    let moving = false;
    groups.forEach((g) => {
      const scrolled = g.hero ? window.scrollY : window.innerHeight - g.el.getBoundingClientRect().top;
      const target = Math.max(0, Math.min(scrolled, window.innerHeight * 1.5)) * SPEED;
      g.current += (target - g.current) * 0.12;
      if (Math.abs(target - g.current) < 0.05) g.current = target;
      else moving = true;
      g.lines.forEach((line) => { line.style.transform = `translate3d(${(line.dataset.dir === '1' ? 1 : -1) * g.current}px, 0, 0)`; });
    });
    window.dispatchEvent(new Event('pl:title-move'));
    running = moving;
    if (running) requestAnimationFrame(frame);
  }
  window.addEventListener('scroll', () => { if (!running) { running = true; requestAnimationFrame(frame); } }, { passive: true });
})();

// Inicio: Conversemos (encabezado y tarjeta de ideas) abre un popup con el formulario. El envío va a contacto/guardar.php,
// que valida y guarda el mensaje en el servidor. Sin JavaScript, el enlace lleva a #contacto.
(function initContactForm() {
  const dialog = document.getElementById('pl-conversemos');
  const form = document.getElementById('pl-form');
  if (!dialog || !form || !dialog.showModal) return;
  const note = document.getElementById('pl-form-note');
  const submit = form.querySelector('button[type="submit"]');
  // Con el popup abierto se usa el cursor del sistema (el anillo queda detrás del popup)
  const abrir = () => {
    document.documentElement.classList.remove('has-cursor');
    dialog.showModal();
    form.querySelector('input').focus();
  };
  dialog.addEventListener('close', () => document.documentElement.classList.add('has-cursor'));
  document.querySelectorAll('.header-actions a[href$="#contacto"], .ideas-cta').forEach((link) => {
    link.addEventListener('click', (event) => { event.preventDefault(); abrir(); });
  });
  dialog.querySelector('[data-close]').addEventListener('click', () => dialog.close());
  // Cierra al hacer clic fuera del popup (no al hacer clic en su contenido ni en su barra de desplazamiento)
  dialog.addEventListener('click', (event) => {
    const r = dialog.getBoundingClientRect();
    const fuera = event.clientX < r.left || event.clientX > r.right || event.clientY < r.top || event.clientY > r.bottom;
    if (fuera) dialog.close();
  });
  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    submit.disabled = true;
    note.textContent = 'Enviando…';
    try {
      const respuesta = await fetch('contacto/guardar.php', { method: 'POST', body: new FormData(form), credentials: 'omit' });
      const datos = await respuesta.json();
      note.textContent = datos.mensaje;
      if (datos.ok) form.reset();
    } catch (error) {
      note.textContent = 'No pude enviar tu mensaje. Escríbeme a contacto@luisdesign.cl.';
    } finally {
      submit.disabled = false;
    }
  });
})();

// Inicio: los títulos de sección se mueven como el del hero. Cada palabra se separa en su propio elemento; las palabras
// se agrupan por línea y cada línea entra desde abajo y se desplaza en horizontal con el scroll (una a la izquierda y la
// siguiente a la derecha). Solo en la home (html.inicio); el hero y el titular de contacto tienen su propio código.
(function initSectionTitles() {
  if (!document.documentElement.classList.contains('inicio') || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const titulos = [...document.querySelectorAll('main h2[id]')]
    .filter((h) => !h.classList.contains('pl-anim-title') && !h.classList.contains('ideas-title') && !h.closest('dialog'));
  if (!titulos.length) return;
  const SPEED = 0.035; // menos desplazamiento que el hero: los títulos de sección son más anchos
  const MAX = 48; // px, máximo desplazamiento de cada línea

  // Separa el texto en palabras, conservando los elementos (p. ej. <mark> o <strong>)
  function separar(el) {
    const recorrido = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
    const nodos = [];
    while (recorrido.nextNode()) nodos.push(recorrido.currentNode);
    nodos.forEach((nodo) => {
      if (!nodo.nodeValue.trim()) return;
      const enMarca = !!nodo.parentElement.closest('mark');
      const fragmento = document.createDocumentFragment();
      nodo.nodeValue.split(/(\s+)/).forEach((parte) => {
        if (!parte) return;
        if (/^\s+$/.test(parte)) { fragmento.append(parte); return; }
        const palabra = document.createElement('span');
        palabra.className = enMarca ? 'pl-w pl-w-mark' : 'pl-w';
        palabra.textContent = parte;
        fragmento.append(palabra);
      });
      nodo.replaceWith(fragmento);
    });
    el.querySelectorAll('mark.pl-mark').forEach((marca) => marca.classList.add('pl-mark-split'));
    el.classList.add('pl-split');
    return [...el.querySelectorAll('.pl-w')];
  }

  // Agrupa las palabras por línea: dirección alterna (izquierda, derecha...) y entrada escalonada por línea
  function agrupar(palabras) {
    let linea = -1;
    let ultimoTop = null;
    palabras.forEach((palabra) => {
      const top = Math.round(palabra.getBoundingClientRect().top);
      if (ultimoTop === null || Math.abs(top - ultimoTop) > 4) { linea += 1; ultimoTop = top; }
      palabra.style.setProperty('--dir', linea % 2 === 0 ? -1 : 1);
      palabra.style.setProperty('--line', linea);
    });
  }

  const estados = titulos.map((el) => ({ el, palabras: separar(el), actual: 0 }));
  const regrupar = () => estados.forEach((e) => agrupar(e.palabras));
  regrupar();
  document.fonts?.ready.then(regrupar);
  let espera = null;
  window.addEventListener('resize', () => { clearTimeout(espera); espera = setTimeout(regrupar, 150); });

  // Entrada: cada título aparece al entrar en pantalla
  if ('IntersectionObserver' in window) {
    const observador = new IntersectionObserver((entradas) => {
      entradas.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('is-in'); observador.unobserve(e.target); } });
    }, { threshold: 0.35 });
    estados.forEach((e) => observador.observe(e.el));
  } else {
    estados.forEach((e) => e.el.classList.add('is-in'));
  }

  // Desplazamiento: el mismo movimiento que el titular del hero (SPEED), suavizado; se detiene al llegar a su destino
  let corriendo = false;
  function frame() {
    let movimiento = false;
    estados.forEach((e) => {
      const r = e.el.getBoundingClientRect();
      const avance = Math.max(0, Math.min(window.innerHeight - r.top, window.innerHeight * 1.5));
      const destino = Math.min(avance * SPEED, MAX);
      e.actual += (destino - e.actual) * 0.12;
      if (Math.abs(destino - e.actual) < 0.05) e.actual = destino; else movimiento = true;
      e.el.style.setProperty('--shift', `${e.actual.toFixed(2)}px`);
    });
    corriendo = movimiento;
    if (corriendo) requestAnimationFrame(frame);
  }
  window.addEventListener('scroll', () => { if (!corriendo) { corriendo = true; requestAnimationFrame(frame); } }, { passive: true });
  frame();
})();

// Inicio: las líneas del título de ideas aparecen en secuencia al entrar en pantalla (antes de que el scroll las abra)
(function initIdeasReveal() {
  const titulo = document.getElementById('ideas-title');
  if (!titulo || !document.documentElement.classList.contains('inicio') || !('IntersectionObserver' in window)) return;
  titulo.querySelectorAll('.ideas-line').forEach((linea, i) => linea.style.setProperty('--i', i));
  const observador = new IntersectionObserver((entradas) => {
    if (entradas.some((e) => e.isIntersecting)) { titulo.classList.add('is-on'); observador.disconnect(); }
  }, { threshold: 0.25 });
  observador.observe(titulo);
})();
