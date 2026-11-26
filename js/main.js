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

// Pantalla de carga: en la primera visita se retira cuando terminó la firma (≈2,6 s) y la página cargó;
// al llegar desde otra página, apenas la página está lista.
(function initLoader() {
  const root = document.documentElement;
  if (!root.classList.contains('is-loading')) return;
  const transicion = root.classList.contains('is-transition');
  const MIN_MS = transicion ? 0 : 2600;
  let finished = false;
  const finish = () => {
    if (finished) return;
    finished = true;
    root.classList.add('is-loaded');
    try { sessionStorage.setItem('intro', '1'); } catch { /* sin almacenamiento */ }
    document.dispatchEvent(new Event('loader:fin'));
    setTimeout(() => root.classList.remove('is-loading', 'is-loaded', 'is-transition'), transicion ? 400 : 700);
  };
  const whenReady = () => setTimeout(finish, Math.max(0, MIN_MS - performance.now()));
  if (document.readyState === 'complete') whenReady();
  else window.addEventListener('load', whenReady, { once: true });
  setTimeout(finish, 6000); // respaldo si la carga se demora
})();

// Transición entre páginas: al seguir un enlace interno se dibuja el logo y luego se navega.
(function initPageTransition() {
  const root = document.documentElement;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const SALIDA_MS = 850;
  const ruta = (url) => url.pathname.replace(/(index)?(\.html)?$/, '').replace(/\/$/, '');
  document.addEventListener('click', (event) => {
    if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    const link = event.target.closest && event.target.closest('a[href]');
    if (!link || link.hasAttribute('download') || (link.target && link.target !== '_self')) return;
    const url = new URL(link.href, location.href);
    if (url.origin !== location.origin) return;
    if (/\.[a-z0-9]+$/i.test(url.pathname) && !/\.html$/i.test(url.pathname)) return; // archivos, no páginas
    if (ruta(url) === ruta(location) && url.search === location.search) return; // ancla en la misma página
    if (root.classList.contains('is-loading')) return;
    event.preventDefault();
    const modal = link.closest('dialog');
    if (modal && modal.open) modal.close(); // un popup quedaría sobre la pantalla de carga
    const previa = document.createElement('link');
    previa.rel = 'prefetch';
    previa.href = url.href;
    document.head.append(previa);
    try { sessionStorage.setItem('transicion', String(Date.now())); } catch { /* sin almacenamiento */ }
    root.classList.add('is-loading', 'is-leaving');
    setTimeout(() => { location.href = url.href; }, SALIDA_MS);
  });
  // Al volver con el botón Atrás el navegador puede restaurar la página tal como quedó
  window.addEventListener('pageshow', (event) => {
    if (event.persisted) root.classList.remove('is-loading', 'is-leaving', 'is-loaded', 'is-transition');
  });
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

  // Servicios del inicio: la línea rodea el título, cruza los números en orden y, si hay más filas, vuelve por el espacio
  // entre tarjetas para seguir de izquierda a derecha. Se calcula con la posición real de cada número.
  function rutaServicios(sec, svgs, box) {
    const stage = sec.querySelector('.pl-stage-servicios');
    const nums = stage ? [...stage.querySelectorAll('.lb-servicio-num')] : [];
    if (!nums.length) return;
    const grid = stage.querySelector('.lb-servicios-grid').getBoundingClientRect();
    const zona = stage.getBoundingClientRect();
    const margen = Math.max(6, (box.right - grid.right) / 2);
    const xI = Math.max(6, (grid.left - box.left) / 2);
    const xD = box.width - margen;
    const filas = [];
    nums.forEach((n) => {
      const r = n.getBoundingClientRect();
      const y = r.top + r.height / 2 - box.top;
      const carta = n.closest('.lb-servicio').getBoundingClientRect();
      const fila = filas.find((f) => Math.abs(f.y - y) < 4);
      if (fila) fila.fin = carta.bottom - box.top; else filas.push({ y, ini: carta.top - box.top, fin: carta.bottom - box.top });
    });
    filas.sort((a, b) => a.y - b.y);
    svgs.forEach((svg) => {
      const path = svg.querySelector('path');
      const ini = path.getPointAtLength(0);
      const fin = path.getPointAtLength(path.getTotalLength());
      const yTitulo = parseFloat(getComputedStyle(sec).paddingTop) / 2;
      const yUnion = (zona.top + (grid.top - zona.top) / 2) - box.top;
      const ySalida = box.height - Math.min(36, (zona.bottom - stage.querySelector('.pl-servicios-cta').getBoundingClientRect().bottom) / 2);
      const pts = [[ini.x, 0], [ini.x, yTitulo], [xD, yTitulo], [xD, yUnion], [xI, yUnion]];
      filas.forEach((f, i) => {
        pts.push([xI, f.y], [xD, f.y]);
        if (i < filas.length - 1) { const entre = (f.fin + filas[i + 1].ini) / 2; pts.push([xD, entre], [xI, entre]); } // por el espacio entre filas
      });
      pts.push([xD, ySalida], [fin.x, ySalida], [fin.x, box.height]);
      const radio = box.width < 640 ? 7 : 16;
      let d = `M${pts[0][0].toFixed(1)} ${pts[0][1].toFixed(1)}`;
      for (let i = 1; i < pts.length - 1; i += 1) {
        const [px, py] = pts[i - 1]; const [cx, cy] = pts[i]; const [nx, ny] = pts[i + 1];
        const l1 = Math.hypot(cx - px, cy - py); const l2 = Math.hypot(nx - cx, ny - cy);
        if (!l1 || !l2) continue;
        const r = Math.min(radio, l1 / 2, l2 / 2);
        d += ` L${(cx + ((px - cx) * r) / l1).toFixed(1)} ${(cy + ((py - cy) * r) / l1).toFixed(1)} Q${cx.toFixed(1)} ${cy.toFixed(1)} ${(cx + ((nx - cx) * r) / l2).toFixed(1)} ${(cy + ((ny - cy) * r) / l2).toFixed(1)}`;
      }
      const u = pts[pts.length - 1];
      path.setAttribute('d', `${d} L${u[0].toFixed(1)} ${u[1].toFixed(1)}`);
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
  // sea una elipse ordenada. Va todo en una sola capa, por detrás de la botella (la botella lo tapa).
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
    const { sec, back } = seg.spiral;
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
    let xr = w * (mob ? 0.82 : 0.75); // la salida baja por la derecha (lejos del texto) y vuelve al centro al final
    // Sale exactamente donde empieza la línea de la sección siguiente: las dos secciones pueden tener anchos distintos
    const siguiente = sec.nextElementSibling && visible(sec.nextElementSibling).find((svg) => !svg.classList.contains('pl-thread-front'));
    const trazoSig = siguiente && siguiente.querySelector('path');
    const mSig = trazoSig && trazoSig.getScreenCTM();
    if (mSig) {
      const ini = trazoSig.getPointAtLength(0);
      const xPantalla = mSig.a * ini.x + mSig.c * ini.y + mSig.e;
      if (xPantalla > box.left && xPantalla < box.right) xr = xPantalla - box.left;
    }
    const bt = r.top - box.top + r.height * 0.36; const bb = r.bottom - box.top - r.height * 0.04; const bh = bb - bt;
    const cx = r.left - box.left + r.width / 2; const bw = r.width * 0.78;
    const R = r.width * 0.95; // radio horizontal del resorte: cada vuelta sobresale a ambos lados de la botella
    const y1 = bt + bh * 0.1; const y2 = bb - bh * 0.02; // altura de la primera y de la última vuelta
    const e = bh * 0.05; // inclinación de la vista: cada vuelta se ve como una elipse
    const VUELTAS = 2; // dos vueltas alrededor de la botella: el espiral se lee más limpio
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
      resorte.push({ p: punto(th) });
    }
    // Muestreo denso (decenas de puntos por vuelta): el trazo es fluido sin suavizado adicional
    const aTrazo = (puntos) => 'M' + puntos.map((q) => `${q[0].toFixed(1)} ${q[1].toFixed(1)}`).join(' L ');
    const completo = aTrazo([...entrada, ...resorte.map((x) => x.p), ...salida.slice(1)]);
    // Fracción del trazo que corresponde a la entrada (desde el hero): se dibuja al llegar a la sección
    const largo = (pts) => pts.reduce((acc, q, i) => (i ? acc + Math.hypot(q[0] - pts[i - 1][0], q[1] - pts[i - 1][1]) : 0), 0);
    seg.entrada = largo(entrada) / Math.max(1, largo([...entrada, ...resorte.map((x) => x.p), ...salida.slice(1)]));
    back.setAttribute('viewBox', `0 0 ${w} ${h}`);
    back.querySelectorAll('path').forEach((path) => path.setAttribute('d', completo));
    seg.t = table(seg.path);
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
      const pinContacto = sec.querySelector('.contact-pin');
      const fijo = pinContacto && getComputedStyle(pinContacto).position === 'sticky' ? pinContacto : null;
      const box = (sec.querySelector('.ideas-pin') || fijo || sec).getBoundingClientRect();
      const svgs = visible(sec);
      // Con .pl-stage, el dibujo (y entre 0 y 1000 del viewBox) se ajusta a ese bloque; las y negativas (de -500 a 0)
      // ocupan lo que hay encima de él (el título) y y = 1000 queda en el borde inferior de la sección
      const stage = sec.querySelector('.pl-stage, .alt-stage');
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
      rutaServicios(sec, svgs, box);
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
        twin: front ? front.querySelectorAll('path')[i] : null, spiral: sec.classList.contains('pl-ideas') ? { sec, back } : null, contacto: sec.id === 'contacto' }));
      chain.push(...segs);
      // Elementos que aparecen cuando la línea pasa por ellos (Sistemas: disciplinas por su punto; el título, al entrar al óvalo)
      const items = [...sec.querySelectorAll('.pl-cap .pl-dot')].map((dot) => [dot.closest('.pl-cap'), dot.getBoundingClientRect()]);
      // Marca práctica (Marca y producto): cada cartel y su icono aparecen cuando la línea pasa por su flecha
      sec.querySelectorAll('.pl-cartel, .pl-icono, .pl-stage-servicios .lb-servicio-num').forEach((el) => items.push([el, el.getBoundingClientRect()]));
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
      const endTop = movil ? 0 : Math.max(0, (window.innerHeight - r.height) / 2); // termina con la sección centrada (en móvil, al llegar arriba: avance más largo y suave)
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

  // Contacto (escritorio): el bloque se fija en pantalla y la línea avanza con el scroll hasta completarse.
  // Devuelve null cuando el bloque no está fijado (móvil), para usar el avance normal.
  function contactoP() {
    const sec = document.getElementById('contacto');
    const pin = sec && sec.querySelector('.contact-pin');
    if (!pin || getComputedStyle(pin).position !== 'sticky') return null;
    const recorrido = Math.max(1, sec.offsetHeight - pin.offsetHeight);
    const inicio = Math.max(0, (window.innerHeight - pin.offsetHeight) / 2); // posición en que el bloque queda fijo
    return Math.min(1, Math.max(0, (inicio - sec.getBoundingClientRect().top) / recorrido));
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
      const pc = seg.contacto ? contactoP() : null;
      const p = heroP < 1 ? 0 : (seg.spiral ? ideasProgress(seg) : pc !== null ? pc : progressOf(seg)); // las secciones esperan a que el hero esté completo
      seg.path.style.strokeDashoffset = String(1 - p);
      if (seg.twin) seg.twin.style.strokeDashoffset = String(1 - p);
      seg.marks.forEach((mk) => mk.el.classList.toggle('is-on', p >= mk.at - 0.01));
      if (seg.main && p > 0) front = { path: seg.path, p };
    });
    // Contacto: el borde del llamado a la acción se ilumina cuando la línea termina su recorrido en él
    const cta = document.querySelector('#contacto .btn');
    if (cta) cta.classList.toggle('is-luz', (contactoP() ?? 0) >= 0.99);
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
  // Si una sección cambia de alto después de cargar (fuentes, textos que se ajustan, Safari), se recalcula la línea
  // para que siga alineada con los carteles y los textos
  if ('ResizeObserver' in window) {
    let pendiente = null;
    const recalcular = new ResizeObserver(() => { cancelAnimationFrame(pendiente); pendiente = requestAnimationFrame(() => { build(); request(); }); });
    document.querySelectorAll('.pl-sec').forEach((sec) => recalcular.observe(sec));
  }
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
  // Títulos de artículo (.noticia-h1): se dividen en líneas según cómo se ven en pantalla y se mueven como el del hero,
  // alternando el sentido (línea 1 a la izquierda, 2 a la derecha, 3 a la izquierda…). Se vuelven a dividir al cambiar el ancho.
  const movibles = [...document.querySelectorAll('.noticia-h1')];
  function dividir(el) {
    const texto = el.dataset.texto || el.textContent.trim();
    el.dataset.texto = texto;
    el.textContent = '';
    const palabras = texto.split(/\s+/).map((p) => { const s = document.createElement('span'); s.textContent = p + ' '; el.appendChild(s); return s; });
    const lineas = [];
    palabras.forEach((s) => {
      const ultima = lineas[lineas.length - 1];
      if (!ultima || Math.abs(ultima.top - s.offsetTop) > 2) lineas.push({ top: s.offsetTop, palabras: [] });
      lineas[lineas.length - 1].palabras.push(s.textContent);
    });
    el.textContent = '';
    lineas.forEach((l, i) => {
      const linea = document.createElement('span'); linea.className = 'pl-line';
      const dentro = document.createElement('span'); dentro.className = 'pl-line-in';
      if (i % 2 === 1) dentro.dataset.dir = '1';
      dentro.textContent = l.palabras.join(''); // con el espacio final, para que el texto siga leyéndose con espacios
      linea.appendChild(dentro); el.appendChild(linea);
    });
  }
  movibles.forEach(dividir);
  const titles = [...document.querySelectorAll('.pl-hero-title, .pl-anim-title, .noticia-h1')];
  if (!titles.length || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const SPEED = 0.07; // px de desplazamiento por px de scroll
  // Los títulos de artículo se mueven desde el inicio de la página, como el del hero
  const groups = titles.map((el) => ({ el, hero: el.classList.contains('pl-hero-title') || el.classList.contains('noticia-h1'), lines: [...el.querySelectorAll('.pl-line-in')], current: 0 }));
  const redividir = () => groups.filter((g) => g.el.classList.contains('noticia-h1')).forEach((g) => { dividir(g.el); g.lines = [...g.el.querySelectorAll('.pl-line-in')]; g.current = 0; });
  // Con la tipografía ya cargada las líneas pueden cortar distinto: se vuelven a dividir
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(redividir);
  let anchoPrevio = window.innerWidth;
  window.addEventListener('resize', () => {
    if (window.innerWidth === anchoPrevio) return;
    anchoPrevio = window.innerWidth;
    redividir();
  });
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

// Conversemos (encabezado y tarjeta de ideas) abre en la misma página un popup con el formulario. El envío va a contacto/guardar.php,
// que valida y guarda el mensaje en el servidor. Sin JavaScript, el enlace lleva a #contacto.
(function initContactForm() {
  const dialog = document.getElementById('pl-conversemos');
  const form = document.getElementById('pl-form');
  // En las demás páginas no está el popup: Conversemos lleva al inicio y allí se abre solo
  if (!dialog) {
    const destino = document.documentElement.lang.startsWith('en') ? 'en/#conversemos' : '#conversemos';
    document.querySelectorAll('.header-actions a[href$="#contacto"]').forEach((link) => {
      link.setAttribute('href', link.getAttribute('href').replace(/#contacto$/, destino));
    });
    return;
  }
  if (!form || !dialog.showModal) return;
  const note = document.getElementById('pl-form-note');
  const submit = form.querySelector('button[type="submit"]');
  const enIngles = document.documentElement.lang.startsWith('en');
  // Con el popup abierto se usa el cursor del sistema (el anillo queda detrás del popup)
  let teniaCursor = false;
  const abrir = () => {
    teniaCursor = document.documentElement.classList.contains('has-cursor');
    document.documentElement.classList.remove('has-cursor');
    dialog.showModal();
    dialog.dispatchEvent(new Event('pl:abierto'));
    if (!form.hidden) form.querySelector('input').focus({ preventScroll: true });
  };
  dialog.addEventListener('close', () => { if (teniaCursor) document.documentElement.classList.add('has-cursor'); });
  // Todo enlace de contacto de la página abre el popup: encabezado, menú de celular, artículos y llamados a la acción
  document.querySelectorAll('a[href$="#contacto"], .ideas-cta, [data-abrir-contacto]').forEach((link) => {
    link.addEventListener('click', (event) => { event.preventDefault(); abrir(); });
  });
  if (location.hash === '#conversemos') {
    history.replaceState(null, '', location.pathname + location.search);
    if (document.documentElement.classList.contains('is-loading')) document.addEventListener('loader:fin', abrir, { once: true });
    else abrir();
  }
  dialog.querySelector('[data-close]').addEventListener('click', () => dialog.close());
  // Cierra al hacer clic fuera del popup (no al hacer clic en su contenido ni en su barra de desplazamiento)
  dialog.addEventListener('click', (event) => {
    // Un clic en el contenido nunca cierra, aunque el popup cambie de alto al pasar de un paso a otro
    if (event.target !== dialog) return;
    const r = dialog.getBoundingClientRect();
    const fuera = event.clientX < r.left || event.clientX > r.right || event.clientY < r.top || event.clientY > r.bottom;
    if (fuera) dialog.close();
  });
  // Validación en el navegador, con los mismos límites de contacto/guardar.php.
  // Cada error aparece bajo su campo; el mensaje muestra un contador que se va cumpliendo mientras se escribe.
  const MIN_MENSAJE = 10;
  const MAX_MENSAJE = 2000;
  const textos = enIngles ? {
    nombre: 'Enter your name (at least 2 characters).',
    correo: 'Enter a valid email, for example name@company.com.',
    consentimiento: 'Please accept the use of your data so I can reply.',
    revisar: 'Please check the fields marked in red.',
    minimo: `At least ${MIN_MENSAJE} characters`,
    faltan: (n) => `${n} more character${n === 1 ? '' : 's'} needed · minimum ${MIN_MENSAJE}`,
    enviando: 'Sending…',
    fallo: 'I could not send your message. Email me at contacto@luisdesign.cl.',
  } : {
    nombre: 'Escribe tu nombre (mínimo 2 caracteres).',
    correo: 'Escribe un correo válido, por ejemplo nombre@empresa.cl.',
    consentimiento: 'Acepta el uso de tus datos para poder responderte.',
    revisar: 'Revisa los campos marcados en rojo.',
    minimo: `Mínimo ${MIN_MENSAJE} caracteres`,
    faltan: (n) => `Falta${n === 1 ? '' : 'n'} ${n} caracter${n === 1 ? '' : 'es'} · mínimo ${MIN_MENSAJE}`,
    enviando: 'Enviando…',
    fallo: 'No pude enviar tu mensaje. Escríbeme a contacto@luisdesign.cl.',
  };
  form.noValidate = true;
  const largo = (campo) => [...campo.value.trim()].length;
  const { nombre, correo, mensaje, consentimiento } = form.elements;

  // Texto de ayuda o error debajo de un campo, enlazado para lectores de pantalla
  function crearAyuda(campo, despuesDe, clase) {
    const ayuda = document.createElement('p');
    ayuda.id = `${campo.id || campo.name}-ayuda`;
    ayuda.className = clase;
    despuesDe.after(ayuda);
    campo.setAttribute('aria-describedby', ayuda.id);
    return ayuda;
  }
  const ayudas = {
    nombre: crearAyuda(nombre, nombre.closest('.pl-field'), 'pl-field-error'),
    correo: crearAyuda(correo, correo.closest('.pl-field'), 'pl-field-error'),
    consentimiento: crearAyuda(consentimiento, consentimiento.closest('.pl-check'), 'pl-field-error'),
  };
  ayudas.nombre.hidden = ayudas.correo.hidden = ayudas.consentimiento.hidden = true;
  const contador = crearAyuda(mensaje, mensaje.closest('.pl-field'), 'pl-contador');

  function marcar(campo, error) {
    campo.setAttribute('aria-invalid', error ? 'true' : 'false');
    const ayuda = ayudas[campo.name];
    if (ayuda) { ayuda.textContent = error || ''; ayuda.hidden = !error; }
    if (campo === consentimiento) campo.closest('.pl-check').classList.toggle('is-error', Boolean(error));
  }
  function pintarContador(conError) {
    const n = largo(mensaje);
    const cumple = n >= MIN_MENSAJE;
    contador.textContent = cumple ? `✓ ${n} / ${MAX_MENSAJE}` : (n === 0 ? textos.minimo : textos.faltan(MIN_MENSAJE - n));
    contador.classList.toggle('is-ok', cumple);
    contador.classList.toggle('is-error', !cumple && conError);
    mensaje.setAttribute('aria-invalid', !cumple && conError ? 'true' : 'false');
    return cumple;
  }
  const errorDe = {
    nombre: () => (largo(nombre) < 2 ? textos.nombre : ''),
    correo: () => (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(correo.value.trim()) ? '' : textos.correo),
    consentimiento: () => (consentimiento.checked ? '' : textos.consentimiento),
  };
  function limpiarAviso() { note.textContent = ''; note.classList.remove('is-error'); }

  // El contador se actualiza siempre; un error ya mostrado desaparece apenas se corrige
  mensaje.addEventListener('input', () => {
    pintarContador(mensaje.getAttribute('aria-invalid') === 'true');
    if (note.classList.contains('is-error')) limpiarAviso();
  });
  [nombre, correo, consentimiento].forEach((campo) => {
    campo.addEventListener(campo === consentimiento ? 'change' : 'input', () => {
      if (campo.getAttribute('aria-invalid') === 'true') marcar(campo, errorDe[campo.name]());
      if (note.classList.contains('is-error')) limpiarAviso();
    });
  });
  pintarContador(false);

  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    limpiarAviso();
    [nombre, correo].forEach((campo) => marcar(campo, errorDe[campo.name]()));
    const mensajeOk = pintarContador(true);
    marcar(consentimiento, errorDe.consentimiento());
    const primero = [nombre, correo, mensaje, consentimiento].find((campo) => campo.getAttribute('aria-invalid') === 'true');
    if (primero || !mensajeOk) {
      note.textContent = textos.revisar;
      note.classList.add('is-error');
      primero.focus();
      return;
    }
    submit.disabled = true;
    note.textContent = textos.enviando;
    try {
      const respuesta = await fetch(form.dataset.endpoint || 'contacto/guardar.php', { method: 'POST', body: new FormData(form), credentials: 'omit' });
      const datos = await respuesta.json();
      note.textContent = datos.mensaje;
      note.classList.toggle('is-error', !datos.ok);
      if (datos.ok) { form.reset(); pintarContador(false); }
    } catch (error) {
      note.textContent = textos.fallo;
      note.classList.add('is-error');
    } finally {
      submit.disabled = false;
    }
  });
})();

// Agenda del popup, en tres pasos: día, horario y datos. Pide las horas libres a contacto/agenda.php y reserva allí.
// Si Google no está conectado o falla, el popup muestra el formulario como respaldo. El navegador no carga nada de Google.
(function initAgenda() {
  const dialog = document.getElementById('pl-conversemos');
  const raiz = document.getElementById('pl-agenda');
  const contacto = document.getElementById('pl-form');
  if (!dialog || !raiz || !contacto) return;
  const en = document.documentElement.lang.startsWith('en');
  const locale = en ? 'en-US' : 'es-CL';
  const t = en ? {
    cargando: '…', pasos: { semana: 'Step 1 of 3', horas: 'Step 2 of 3', datos: 'Step 3 of 3' },
    atras: { horas: 'Back to days', datos: 'Back to times' }, conector: 'on', aLas: 'at',
    titulos: { semana: 'Pick a day', horas: 'What time?', datos: 'Under what name?' }, iniciales: ['M', 'T', 'W', 'T', 'F', 'S', 'S'],
    sinHoras: 'no times available', revisar: 'Please check the fields marked in red.',
    nombre: 'Enter your name (at least 2 characters).', correo: 'Enter a valid email, for example name@company.com.',
    consentimiento: 'Please accept the use of your data to schedule.', enviando: 'Scheduling…',
    fallo: 'I could not schedule this. Please try again.', listo: (f) => `${f}, Chile time. The invitation with the Google Meet link is on its way to your email.`,
  } : {
    cargando: '…', pasos: { semana: 'Paso 1 de 3', horas: 'Paso 2 de 3', datos: 'Paso 3 de 3' },
    atras: { horas: 'Volver a los días', datos: 'Volver a los horarios' }, conector: 'el', aLas: 'a las',
    titulos: { semana: 'Elige un día', horas: '¿A qué hora?', datos: '¿A nombre de quién?' }, iniciales: ['L', 'M', 'M', 'J', 'V', 'S', 'D'],
    sinHoras: 'sin horas disponibles', revisar: 'Revisa los campos marcados en rojo.',
    nombre: 'Escribe tu nombre (mínimo 2 caracteres).', correo: 'Escribe un correo válido, por ejemplo nombre@empresa.cl.',
    consentimiento: 'Acepta el uso de tus datos para poder agendar.', enviando: 'Agendando…',
    fallo: 'No pude agendar. Inténtalo de nuevo.', listo: (f) => `${f}, hora de Chile. La invitación con el enlace de Google Meet va en camino a tu correo.`,
  };
  const vistas = {
    semana: raiz.querySelector('[data-vista="semana"]'), horas: raiz.querySelector('[data-vista="horas"]'),
    datos: raiz.querySelector('[data-vista="datos"]'), listo: raiz.querySelector('[data-vista="listo"]'),
  };
  const form = vistas.datos;
  const grid = raiz.querySelector('[data-grid]');
  const listaHoras = raiz.querySelector('[data-horas]');
  const titulo = raiz.querySelector('.ag-titulo');
  const paso = raiz.querySelector('[data-paso]');
  const tituloPaso = raiz.querySelector('[data-titulo]');
  const tituloFijo = raiz.querySelector('.ag-cab-fijo');
  const textoFijo = tituloFijo.textContent;
  const cabecera = raiz.querySelector('[data-cab]');
  const nota = raiz.querySelector('[data-nota]');
  const atras = raiz.querySelector('[data-atras]');
  const aFormulario = raiz.querySelector('[data-a-form]');
  const aAgenda = contacto.querySelector('[data-a-agenda]');
  const aviso = raiz.querySelector('[data-aviso]');
  const enviar = form.querySelector('button[type="submit"]');
  const { nombre, correo, consentimiento } = form.elements;
  let dias = new Map();
  let meses = [];
  let indice = 0;
  let diaActivo = null;
  let elegido = null;
  let iniciada = false;
  let vistaActual = 'semana';
  let fechaElegida = '';

  const fecha = (texto) => new Date(`${texto}T12:00:00Z`);
  const fmt = (texto, opciones) => new Intl.DateTimeFormat(locale, { timeZone: 'UTC', ...opciones }).format(fecha(texto));
  const diaLargo = (texto) => fmt(texto, { weekday: 'long', day: 'numeric', month: 'long' });
  function verVista(nombreVista) {
    Object.entries(vistas).forEach(([clave, el]) => { el.hidden = clave !== nombreVista; });
    cabecera.hidden = nombreVista === 'listo';
    vistaActual = nombreVista;
    atras.hidden = !t.atras[nombreVista];
    if (t.atras[nombreVista]) atras.setAttribute('aria-label', t.atras[nombreVista]);
    const actual = ['semana', 'horas', 'datos'].indexOf(nombreVista);
    if (actual > -1) {
      paso.setAttribute('aria-label', t.pasos[nombreVista]);
      [...paso.children].forEach((punto, i) => {
        punto.classList.toggle('is-hecho', i < actual);
        punto.classList.toggle('is-actual', i === actual);
      });
    }
    aFormulario.hidden = nombreVista !== 'semana';
    // La frase se completa en cada paso: «Agendemos meet el viernes 27 de nov a las 19:00»
    const conFecha = nombreVista === 'horas' || nombreVista === 'datos';
    const frase = conFecha ? `${textoFijo} ${t.conector} ${fechaElegida}` : textoFijo;
    tituloFijo.textContent = nombreVista === 'datos' ? `${frase} ${t.aLas} ${elegido.hora}` : frase;
    tituloFijo.classList.toggle('is-fecha', conFecha);
    if (t.titulos[nombreVista]) tituloPaso.textContent = t.titulos[nombreVista];
  }
  function soloFormulario() {
    raiz.hidden = true;
    contacto.hidden = false;
    aAgenda.hidden = true;
    contacto.style.minHeight = '';
  }
  function volverAgenda() {
    contacto.hidden = true;
    raiz.hidden = false;
  }
  function elegirDia(dia) {
    diaActivo = dia.fecha;
    nota.hidden = true;
    pintarMes();
    const largo = diaLargo(dia.fecha);
    const diaSemana = fmt(dia.fecha, { weekday: 'long' });
    const numero = fmt(dia.fecha, { day: 'numeric' });
    const mesCorto = fmt(dia.fecha, { month: 'short' }).replace('.', '');
    fechaElegida = en ? `${diaSemana}, ${mesCorto} ${numero}` : `${diaSemana} ${numero} de ${mesCorto}`;
    listaHoras.replaceChildren(...dia.horas.map((h) => {
      const b = document.createElement('button');
      b.type = 'button';
      b.className = 'ag-hora';
      b.textContent = h.hora;
      b.setAttribute('aria-label', `${largo}, ${h.hora}`);
      b.addEventListener('click', () => {
        elegido = { inicio: h.inicio, texto: `${largo}, ${h.hora}`, hora: h.hora };
        aviso.textContent = '';
        aviso.classList.remove('is-error');
        verVista('datos');
        nombre.focus({ preventScroll: true });
      });
      return b;
    }));
    verVista('horas');
    listaHoras.querySelector('button').focus({ preventScroll: true });
  }
  // Mes completo, de lunes a domingo: solo los días con horas libres se pueden elegir
  function pintarMes() {
    const [anio, mes] = meses[indice].split('-').map(Number);
    const primero = new Date(Date.UTC(anio, mes - 1, 1));
    const total = new Date(Date.UTC(anio, mes, 0)).getUTCDate();
    const vacios = (primero.getUTCDay() + 6) % 7;
    titulo.textContent = new Intl.DateTimeFormat(locale, { timeZone: 'UTC', month: 'long' }).format(primero);
    raiz.querySelector('[data-mes="-1"]').disabled = indice === 0;
    raiz.querySelector('[data-mes="1"]').disabled = indice === meses.length - 1;
    const celdas = Array.from({ length: vacios }, () => document.createElement('span'));
    for (let n = 1; n <= total; n++) {
      const clave = `${meses[indice]}-${String(n).padStart(2, '0')}`;
      const dia = dias.get(clave);
      const b = document.createElement('button');
      b.type = 'button';
      b.className = 'ag-dia';
      b.textContent = n;
      b.disabled = !dia;
      b.setAttribute('aria-label', dia ? diaLargo(clave) : `${diaLargo(clave)}, ${t.sinHoras}`);
      if (clave === diaActivo) { b.classList.add('is-activo'); b.setAttribute('aria-pressed', 'true'); }
      if (dia) b.addEventListener('click', () => elegirDia(dia));
      celdas.push(b);
    }
    grid.replaceChildren(...celdas);
  }
  async function cargar() {
    titulo.textContent = t.cargando;
    grid.replaceChildren();
    try {
      const idioma = en ? '?idioma=en' : '';
      const r = await fetch(raiz.dataset.endpoint + idioma, { credentials: 'omit' });
      const datos = await r.json();
      const libres = datos.disponible ? datos.semanas.flatMap((s) => s.dias).filter((d) => d.horas.length) : [];
      if (!libres.length) { soloFormulario(); return false; }
      dias = new Map(libres.map((d) => [d.fecha, d]));
      meses = [...new Set(libres.map((d) => d.fecha.slice(0, 7)))].sort();
      indice = 0;
      diaActivo = null;
      pintarMes();
      return true;
    } catch (error) {
      soloFormulario();
      return false;
    }
  }
  dialog.addEventListener('pl:abierto', () => {
    if (iniciada) return;
    iniciada = true;
    raiz.hidden = false;
    contacto.hidden = true;
    verVista('semana');
    cargar();
  });
  dialog.addEventListener('close', () => {
    if (!aAgenda.hidden) volverAgenda();
    if (!raiz.hidden && !vistas.listo.hidden) { form.reset(); verVista('semana'); cargar(); }
  });
  // «O solo envíame un mensaje»: abre el formulario con la misma altura del calendario
  aFormulario.addEventListener('click', () => {
    contacto.style.minHeight = `${raiz.offsetHeight}px`;
    raiz.hidden = true;
    contacto.hidden = false;
    aAgenda.hidden = false;
    contacto.querySelector('input').focus({ preventScroll: true });
  });
  aAgenda.addEventListener('click', () => {
    volverAgenda();
    aAgenda.hidden = true;
    const foco = grid.querySelector('.is-activo, .ag-dia:not(:disabled)');
    if (foco) foco.focus({ preventScroll: true });
  });
  raiz.querySelector('[data-sem]').replaceChildren(...t.iniciales.map((letra) => {
    const span = document.createElement('span');
    span.textContent = letra;
    return span;
  }));
  // Botón de servicios: abre el popup con el servicio escrito en el mensaje, sin borrar lo que la persona ya haya escrito
  let mensajeServicio = '';
  document.querySelectorAll('[data-servicio]').forEach((boton) => boton.addEventListener('click', () => {
    const texto = `${en ? 'I am interested in' : 'Me interesa'}: ${boton.dataset.servicio}`;
    [form.elements.mensaje, contacto.elements.mensaje].forEach((campo) => {
      if (campo.value.trim() && campo.value !== mensajeServicio) return;
      campo.value = texto;
      campo.dispatchEvent(new Event('input', { bubbles: true }));
    });
    mensajeServicio = texto;
  }));
  raiz.querySelectorAll('[data-mes]').forEach((b) => b.addEventListener('click', () => {
    indice += Number(b.dataset.mes);
    pintarMes();
  }));
  // Al volver, el foco pasa a la opción elegida antes, porque la flecha puede desaparecer
  atras.addEventListener('click', () => {
    const destino = vistaActual === 'datos' ? 'horas' : 'semana';
    verVista(destino);
    const foco = destino === 'horas' ? listaHoras.querySelector('button') : grid.querySelector('.is-activo, .ag-dia:not(:disabled)');
    if (foco) foco.focus({ preventScroll: true });
  });

  form.noValidate = true;
  const errores = {};
  [nombre, correo, consentimiento].forEach((campo) => {
    const p = document.createElement('p');
    p.id = `${campo.id || 'ag-consentimiento'}-ayuda`;
    p.className = 'pl-field-error';
    p.hidden = true;
    (campo === consentimiento ? campo.closest('.pl-check') : campo.closest('.pl-field')).after(p);
    campo.setAttribute('aria-describedby', p.id);
    errores[campo.name] = p;
    campo.addEventListener(campo === consentimiento ? 'change' : 'input', () => {
      if (campo.getAttribute('aria-invalid') === 'true') marcar(campo);
    });
  });
  const reglas = {
    nombre: () => ([...nombre.value.trim()].length < 2 ? t.nombre : ''),
    correo: () => (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(correo.value.trim()) ? '' : t.correo),
    consentimiento: () => (consentimiento.checked ? '' : t.consentimiento),
  };
  function marcar(campo) {
    const error = reglas[campo.name]();
    campo.setAttribute('aria-invalid', error ? 'true' : 'false');
    errores[campo.name].textContent = error;
    errores[campo.name].hidden = !error;
    if (campo === consentimiento) campo.closest('.pl-check').classList.toggle('is-error', Boolean(error));
    return !error;
  }
  form.addEventListener('submit', async (event) => {
    event.preventDefault();
    const invalidos = [nombre, correo, consentimiento].filter((campo) => !marcar(campo));
    if (invalidos.length) {
      aviso.textContent = t.revisar;
      aviso.classList.add('is-error');
      invalidos[0].focus();
      return;
    }
    aviso.textContent = t.enviando;
    aviso.classList.remove('is-error');
    enviar.disabled = true;
    enviar.setAttribute('aria-busy', 'true');
    try {
      const cuerpo = new FormData(form);
      cuerpo.set('inicio', elegido.inicio);
      cuerpo.set('idioma', en ? 'en' : 'es');
      const r = await fetch(raiz.dataset.endpoint, { method: 'POST', body: cuerpo, credentials: 'omit' });
      const datos = await r.json();
      if (datos.ok) {
        raiz.querySelector('[data-listo]').textContent = t.listo(elegido.texto);
        verVista('listo');
        vistas.listo.focus({ preventScroll: true });
      } else if (datos.actualizar) {
        const hayHoras = await cargar();
        if (hayHoras) {
          verVista('semana');
          nota.textContent = datos.mensaje;
          nota.hidden = false;
        }
      } else if (datos.usarFormulario) {
        soloFormulario();
        const nota = document.getElementById('pl-form-note');
        nota.textContent = datos.mensaje;
        nota.classList.add('is-error');
      } else {
        aviso.textContent = datos.mensaje;
        aviso.classList.add('is-error');
      }
    } catch (error) {
      aviso.textContent = t.fallo;
      aviso.classList.add('is-error');
    } finally {
      enviar.disabled = false;
      enviar.removeAttribute('aria-busy');
    }
  });
})();

// Servicios: la persona arma su proyecto con uno o varios servicios y la barra lleva esa selección al popup de contacto
(function initArmaProyecto() {
  const seccion = document.getElementById('servicios');
  const barra = seccion && seccion.querySelector('[data-proyecto]');
  if (!barra) return;
  const botones = [...seccion.querySelectorAll('[data-agregar]')];
  const combos = [...seccion.querySelectorAll('[data-combo]')];
  const nombres = barra.querySelector('[data-proyecto-nombres]');
  const enlace = barra.querySelector('[data-servicio]');
  const aviso = seccion.querySelector('[data-proyecto-aviso]');
  const elegidos = new Set();
  const piezas = new Map();
  const sinMovimiento = window.matchMedia('(prefers-reduced-motion: reduce)');
  const curva = 'cubic-bezier(.2, .8, .2, 1)';
  const esMovil = window.matchMedia('(max-width: 39.99em)');
  const centro = () => (esMovil.matches ? 'translateX(-50%)' : 'translateX(0)');
  // En móvil entra desde arriba, bajo el header. Desde tablet entra desde la derecha
  const fuera = () => (esMovil.matches ? 'translateX(-50%) translateY(-24px)' : 'translateX(24px)');
  let salidaBarra = null;
  let pulso = null;

  // Cada servicio es una pieza: la nueva entra, la quitada sale y las demás se deslizan a su nuevo lugar
  function moverPiezas(lista) {
    const animar = !sinMovimiento.matches && !barra.hidden;
    const caja = nombres.getBoundingClientRect();
    const antes = new Map([...piezas].map(([nombre, el]) => [nombre, el.getBoundingClientRect()]));
    const nuevas = new Set();
    [...piezas].forEach(([nombre, el]) => {
      if (lista.includes(nombre)) return;
      piezas.delete(nombre);
      if (!animar) { el.remove(); return; }
      const r = antes.get(nombre);
      el.getAnimations().forEach((a) => a.cancel());
      el.classList.add('is-sale');
      el.style.left = `${r.left - caja.left}px`;
      el.style.top = `${r.top - caja.top}px`;
      nombres.append(el);
      el.animate([{ opacity: 1, transform: 'none' }, { opacity: 0, transform: 'translateY(-10px) scale(.96)' }], { duration: 220, easing: 'ease-in', fill: 'forwards' })
        .finished.then(() => el.remove(), () => el.remove());
    });
    lista.forEach((nombre, i) => {
      let el = piezas.get(nombre);
      if (!el) {
        el = document.createElement('span');
        el.className = 'lb-pieza';
        const boton = botones.find((b) => b.dataset.agregar === nombre);
        const icono = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
        const uso = document.createElementNS('http://www.w3.org/2000/svg', 'use');
        uso.setAttribute('href', boton.querySelector('use').getAttribute('href').replace('i-check', boton.dataset.icono));
        icono.setAttribute('class', 'icon');
        icono.setAttribute('aria-hidden', 'true');
        icono.append(uso);
        el.append(icono, nombre);
        piezas.set(nombre, el);
        nuevas.add(el);
      }
      el.classList.toggle('con-mas', i > 0);
      if (nombres.children[i] !== el) nombres.insertBefore(el, nombres.children[i] || null);
    });
    if (!animar) return;
    piezas.forEach((el, nombre) => {
      if (nuevas.has(el)) {
        el.animate([
          { opacity: 0, transform: 'translateY(12px)', color: 'var(--lima-deep)' },
          { opacity: 1, transform: 'none', color: 'var(--lima-deep)', offset: 0.45 },
          { opacity: 1, transform: 'none' },
        ], { duration: 620, easing: curva });
        return;
      }
      const previo = antes.get(nombre);
      el.getAnimations().forEach((a) => a.cancel());
      const ahora = el.getBoundingClientRect();
      const dx = previo.left - ahora.left;
      const dy = previo.top - ahora.top;
      if (dx || dy) el.animate([{ transform: `translate(${dx}px, ${dy}px)` }, { transform: 'none' }], { duration: 340, easing: curva });
    });
  }

  function latido(agrega) {
    if (sinMovimiento.matches) return;
    if (pulso) pulso.cancel();
    const medio = agrega ? { transform: `${centro()} scale(1.015)`, offset: 0.35 } : { transform: `${centro()} scale(.988)`, offset: 0.35 };
    pulso = barra.animate([{ transform: `${centro()} scale(1)` }, medio, { transform: `${centro()} scale(1)` }], { duration: 420, easing: curva });
  }

  function mostrarBarra(lista) {
    const cantidadAntes = piezas.size;
    if (salidaBarra) { salidaBarra.cancel(); salidaBarra = null; }
    if (lista.length) {
      const estabaOculta = barra.hidden;
      barra.hidden = false;
      moverPiezas(lista);
      if (estabaOculta && !sinMovimiento.matches) {
        barra.animate([{ opacity: 0, transform: fuera() }, { opacity: 1, transform: centro() }], { duration: 380, easing: curva });
      } else if (lista.length !== cantidadAntes || !estabaOculta) {
        latido(lista.length >= cantidadAntes);
      }
      return;
    }
    moverPiezas(lista);
    if (barra.hidden || sinMovimiento.matches) { barra.hidden = true; return; }
    salidaBarra = barra.animate([{ opacity: 1, transform: centro() }, { opacity: 0, transform: fuera() }], { duration: 260, easing: 'ease-in', fill: 'forwards' });
    salidaBarra.onfinish = () => {
      barra.hidden = true;
      salidaBarra.cancel();
      salidaBarra = null;
    };
  }

  function pintar() {
    const lista = botones.map((b) => b.dataset.agregar).filter((n) => elegidos.has(n));
    const texto = lista.join(' + ');
    botones.forEach((b) => {
      const activo = elegidos.has(b.dataset.agregar);
      b.closest('.lb-servicio').classList.toggle('is-elegido', activo);
      b.querySelector('[data-agregar-txt]').textContent = activo ? 'Agregado' : 'Agregar';
    });
    combos.forEach((c) => {
      const partes = c.dataset.combo.split('|');
      c.setAttribute('aria-pressed', String(partes.length === elegidos.size && partes.every((n) => elegidos.has(n))));
    });
    enlace.dataset.servicio = texto;
    mostrarBarra(lista);
    document.documentElement.classList.toggle('lb-con-proyecto', lista.length > 0);
    aviso.textContent = lista.length ? `Tu proyecto: ${texto}` : 'Selección vacía';
  }

  botones.forEach((b) => b.addEventListener('click', () => {
    const nombre = b.dataset.agregar;
    if (!elegidos.delete(nombre)) elegidos.add(nombre);
    pintar();
  }));
  combos.forEach((c) => c.addEventListener('click', () => {
    const quitar = c.getAttribute('aria-pressed') === 'true';
    elegidos.clear();
    if (!quitar) c.dataset.combo.split('|').forEach((n) => elegidos.add(n));
    pintar();
  }));
  // Desde tablet el panel acompaña solo mientras la sección de servicios ocupa el centro de la pantalla
  if ('IntersectionObserver' in window) {
    new IntersectionObserver(([entrada]) => barra.classList.toggle('is-fuera', !entrada.isIntersecting), { rootMargin: '-45% 0px -45% 0px' }).observe(seccion);
  }
  barra.querySelector('[data-proyecto-vaciar]').addEventListener('click', () => {
    elegidos.clear();
    pintar();
    botones[0].focus({ preventScroll: true });
  });
})();

// Servicios: en móvil y tablet cada lista de entregables parte plegada en dos puntos y medio. Con cuatro columnas se ve completa
(function initEntregables() {
  const items = [...document.querySelectorAll('.lb-incluye')].map((caja) => ({ lista: caja.querySelector('ul'), boton: caja.querySelector('.lb-incluye-btn'), abierto: false }));
  if (!items.length) return;
  const plegable = window.matchMedia('(max-width: 74.99em)');
  const dosColumnas = window.matchMedia('(min-width: 40em)');
  const altoPlegado = (lista) => {
    const tercero = lista.children[2];
    return tercero.offsetTop + tercero.offsetHeight / 2;
  };
  function poner(item, abierto) {
    const { lista, boton } = item;
    item.abierto = abierto;
    lista.classList.toggle('is-plegado', !abierto);
    lista.style.maxHeight = `${abierto ? lista.scrollHeight : altoPlegado(lista)}px`;
    boton.setAttribute('aria-expanded', String(abierto));
    const enIngles = document.documentElement.lang.startsWith('en');
    boton.querySelector('[data-incluye-txt]').textContent = abierto ? (enIngles ? 'Show less' : 'Ver menos') : (enIngles ? `See all ${lista.children.length} deliverables` : `Ver los ${lista.children.length} entregables`);
  }
  function aplicar() {
    items.forEach((item) => {
      item.boton.hidden = !plegable.matches;
      if (plegable.matches) {
        poner(item, item.abierto);
      } else {
        item.lista.classList.remove('is-plegado');
        item.lista.style.removeProperty('max-height');
      }
    });
  }
  items.forEach((item) => item.boton.addEventListener('click', () => {
    const abrir = !item.abierto;
    // En dos columnas se abre la fila completa para que las tarjetas sigan parejas
    const indice = items.indexOf(item);
    const fila = dosColumnas.matches ? items.slice(indice - (indice % 2), indice - (indice % 2) + 2) : [item];
    fila.forEach((i) => poner(i, abrir));
  }));
  const reiniciar = () => {
    items.forEach((item) => { item.abierto = false; });
    aplicar();
  };
  plegable.addEventListener('change', reiniciar);
  dosColumnas.addEventListener('change', reiniciar);
  window.addEventListener('resize', aplicar, { passive: true });
  aplicar();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(aplicar);
})();

// Servicios: la propuesta se fija y sus dos tarjetas pasan de 80/20 a 20/80 con el scroll
(function initPropuesta() {
  const seccion = document.querySelector('.lb-propuesta');
  if (!seccion || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const fijo = seccion.querySelector('.lb-propuesta-grid');
  const titulo = seccion.querySelector('h2');
  const tarjetas = [...seccion.querySelectorAll('.lb-tarjetas .card')];
  if (tarjetas.length !== 2) return;
  const escritorio = window.matchMedia('(min-width: 70em)');
  let activo = false;
  let agendado = false;

  const datos = () => ({
    recorrido: seccion.offsetHeight - fijo.offsetHeight,
    inicio: seccion.getBoundingClientRect().top + window.scrollY - parseFloat(getComputedStyle(fijo).top),
  });
  function pintar() {
    agendado = false;
    if (!activo) return;
    const { recorrido, inicio } = datos();
    const segunda = recorrido > 0 && (window.scrollY - inicio) / recorrido >= 0.5;
    tarjetas[0].classList.toggle('is-abierta', !segunda);
    tarjetas[1].classList.toggle('is-abierta', segunda);
  }
  function agendar() {
    if (agendado) return;
    agendado = true;
    window.requestAnimationFrame(pintar);
  }
  function ajustar() {
    seccion.classList.add('is-dos');
    const estilo = getComputedStyle(fijo);
    const libre = fijo.clientHeight - parseFloat(estilo.paddingTop) - parseFloat(estilo.paddingBottom);
    // En columnas el título va al lado; apilado, deben caber título, tarjetas y botón
    activo = escritorio.matches ? titulo.offsetHeight + 76 <= libre && libre >= 360 : titulo.offsetHeight + 40 + 24 + 340 <= libre;
    seccion.classList.toggle('is-dos', activo);
    if (!activo) tarjetas.forEach((t) => t.classList.remove('is-abierta'));
    agendar();
  }
  // Un toque de flecha pasa de A a B, y el siguiente continúa a la sección de servicios
  function tecla(e) {
    if (!activo || e.altKey || e.ctrlKey || e.metaKey || document.querySelector('dialog[open]')) return;
    if (e.target.closest && e.target.closest(e.key === ' ' ? 'a, button, input, textarea, select, [contenteditable]' : 'input, textarea, select, [contenteditable]')) return;
    const baja = e.key === 'ArrowDown' || e.key === 'PageDown' || (e.key === ' ' && !e.shiftKey);
    const sube = e.key === 'ArrowUp' || e.key === 'PageUp' || (e.key === ' ' && e.shiftKey);
    if (!baja && !sube) return;
    const { recorrido, inicio } = datos();
    const y = window.scrollY;
    if (baja ? (y < inicio - 1 || y >= inicio + recorrido - 1) : (y <= inicio + 1 || y > inicio + recorrido + 1)) return;
    e.preventDefault();
    if (e.repeat) return;
    const enSegunda = (y - inicio) / recorrido >= 0.5;
    let top;
    if (baja) top = enSegunda ? inicio + recorrido + fijo.offsetHeight : inicio + recorrido * 0.52;
    else top = enSegunda ? inicio : inicio - 160;
    window.scrollTo({ top, behavior: 'smooth' });
  }
  window.addEventListener('keydown', tecla);
  window.addEventListener('scroll', agendar, { passive: true });
  window.addEventListener('resize', ajustar, { passive: true });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(ajustar);
  ajustar();
})();

// Servicios: «Cómo trabajo» se fija en pantalla y cada tramo de scroll revela una tarjeta. Si no cabe, aparecen en secuencia al bajar
(function initPasos() {
  const seccion = document.querySelector('.lb-proceso');
  const lista = seccion && seccion.querySelector('.lb-pasos');
  if (!lista || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const fijo = seccion.querySelector('.lb-proceso-fijo');
  const cabecera = seccion.querySelector('.lb-proceso-top');
  const tarjetas = [...lista.children];
  lista.classList.add('anima');
  let fijado = false;
  let agendado = false;

  // Trazo flúor decorativo: un tramo por tarjeta, de un número al siguiente, y el último sale por la derecha
  const svgNS = 'http://www.w3.org/2000/svg';
  const vector = document.createElementNS(svgNS, 'svg');
  vector.setAttribute('class', 'lb-proceso-vector');
  vector.setAttribute('aria-hidden', 'true');
  vector.setAttribute('focusable', 'false');
  const tramos = tarjetas.map(() => {
    const tramo = document.createElementNS(svgNS, 'path');
    tramo.setAttribute('pathLength', '1');
    tramo.setAttribute('stroke-dasharray', '1 1');
    vector.append(tramo);
    return tramo;
  });
  fijo.prepend(vector);
  const escritorio = window.matchMedia('(min-width: 70em)');

  function posicion(el) {
    let x = 0;
    let y = 0;
    for (let n = el; n && n !== fijo; n = n.offsetParent) {
      x += n.offsetLeft;
      y += n.offsetTop;
    }
    return { x, y };
  }
  function trazar() {
    if (!fijado || !escritorio.matches) return;
    const titulo = posicion(cabecera.querySelector('h2')).y;
    const puntos = tarjetas.map((tarjeta) => {
      const numero = tarjeta.querySelector('.lb-paso-num');
      const p = posicion(numero);
      const em = parseFloat(getComputedStyle(numero).fontSize);
      return { x: p.x + em * 0.385, y: p.y + numero.offsetHeight / 2 };
    });
    const alturas = [1, 1.14, 0.94];
    const base = Math.max(90, Math.min(200, (puntos[0].y - titulo) * 0.62));
    tramos.forEach((tramo, i) => {
      const a = puntos[i];
      const b = puntos[i + 1];
      if (b) {
        const dx = b.x - a.x;
        const h = base * alturas[i];
        tramo.setAttribute('d', `M${a.x} ${a.y}C${a.x + dx * 0.3} ${a.y - h * 0.62} ${a.x + dx * 0.6} ${a.y - h} ${a.x + dx * 0.78} ${a.y - h}C${a.x + dx * 0.93} ${a.y - h} ${b.x} ${a.y - h * 0.45} ${b.x} ${b.y}`);
      } else {
        const finX = fijo.clientWidth + parseFloat(getComputedStyle(seccion).paddingRight) + 24;
        const finY = Math.max(12, a.y - base * 2.1);
        const dx = finX - a.x;
        const dy = a.y - finY;
        tramo.setAttribute('d', `M${a.x} ${a.y}C${a.x + dx * 0.3} ${a.y - dy * 0.42} ${a.x + dx * 0.62} ${a.y - dy * 0.96} ${finX} ${finY}`);
      }
    });
  }

  function medir() {
    seccion.classList.add('is-fijo');
    // En móvil y tablet, desde la tercera tarjeta el título sale y la pila sube hasta 8 px bajo el header
    seccion.style.setProperty('--alto-cab', `${escritorio.matches ? 0 : Math.max(0, posicion(lista).y - 8)}px`);
    const estilo = getComputedStyle(fijo);
    const libre = fijo.clientHeight - parseFloat(estilo.paddingTop) - parseFloat(estilo.paddingBottom);
    if (escritorio.matches) {
      fijado = cabecera.offsetHeight + parseFloat(getComputedStyle(cabecera).marginBottom) + lista.offsetHeight <= libre;
    } else {
      // Deben caber el título con dos tarjetas y, sin título, la pila completa
      const base = fijo.clientHeight - parseFloat(estilo.paddingBottom);
      const pestana = parseFloat(getComputedStyle(lista).getPropertyValue('--pestana')) || 0;
      fijado = posicion(lista).y + pestana + tarjetas[1].offsetHeight <= base && 8 + lista.offsetHeight <= base;
    }
    seccion.classList.toggle('is-fijo', fijado);
  }
  function pintarFijo() {
    const caja = seccion.getBoundingClientRect();
    const recorrido = caja.height - fijo.offsetHeight;
    const avance = recorrido > 0 ? (parseFloat(getComputedStyle(fijo).top) - caja.top) / recorrido : 1;
    const actual = avance < (escritorio.matches ? -0.04 : -0.2) ? -1 : Math.max(0, Math.min(tarjetas.length - 1, Math.floor(avance * tarjetas.length)));
    tarjetas.forEach((tarjeta, i) => {
      tarjeta.classList.toggle('is-visible', i <= actual);
      tarjeta.classList.toggle('is-pasada', i < actual);
      tarjeta.toggleAttribute('aria-current', i === actual);
    });
    seccion.classList.toggle('pila-arriba', !escritorio.matches && actual >= 2);
    // El trazo llega al número siguiente justo cuando se abre su tarjeta
    const tramoActual = avance * tramos.length;
    tramos.forEach((tramo, i) => {
      const lleno = Math.max(0, Math.min(1, tramoActual - i));
      tramo.style.strokeDashoffset = String(1 - lleno);
      tramo.style.visibility = lleno > 0 ? 'visible' : 'hidden';
    });
  }
  function pintarSecuencia() {
    const alto = window.innerHeight;
    tarjetas.forEach((tarjeta) => {
      tarjeta.classList.remove('is-pasada');
      tarjeta.removeAttribute('aria-current');
      const columna = tarjetas.filter((t) => t.offsetTop === tarjeta.offsetTop).indexOf(tarjeta);
      if (tarjeta.getBoundingClientRect().top < alto * (0.9 - columna * 0.1)) tarjeta.classList.add('is-visible');
    });
  }
  function pintar() {
    agendado = false;
    if (fijado) pintarFijo();
    else pintarSecuencia();
  }
  function agendar() {
    if (agendado) return;
    agendado = true;
    window.requestAnimationFrame(pintar);
  }
  function ajustar() {
    medir();
    trazar();
    agendar();
  }
  // Con la sección fijada, cada toque de flecha, Avanzar/Retroceder página o espacio mueve exactamente una tarjeta
  let destino = null;
  let soltar = 0;
  function teclaPaso(e) {
    if (!fijado || e.altKey || e.ctrlKey || e.metaKey || document.querySelector('dialog[open]') || document.documentElement.classList.contains('has-drawer')) return;
    if (e.target.closest && e.target.closest(e.key === ' ' ? 'a, button, input, textarea, select, [contenteditable]' : 'input, textarea, select, [contenteditable]')) return;
    const baja = e.key === 'ArrowDown' || e.key === 'PageDown' || (e.key === ' ' && !e.shiftKey);
    const sube = e.key === 'ArrowUp' || e.key === 'PageUp' || (e.key === ' ' && e.shiftKey);
    if (!baja && !sube) return;
    const recorrido = seccion.offsetHeight - fijo.offsetHeight;
    const inicio = seccion.getBoundingClientRect().top + window.scrollY - parseFloat(getComputedStyle(fijo).top);
    const y = window.scrollY;
    if (destino === null && (baja ? (y < inicio - 1 || y >= inicio + recorrido - 1) : (y <= inicio + 1 || y > inicio + recorrido + 1))) return;
    e.preventDefault();
    if (e.repeat) return;
    const total = tarjetas.length;
    const actual = destino !== null ? destino : Math.max(0, Math.min(total - 1, Math.floor(((y - inicio) / recorrido) * total)));
    const siguiente = actual + (baja ? 1 : -1);
    let top;
    if (siguiente >= total) {
      const proxima = seccion.nextElementSibling;
      top = proxima.getBoundingClientRect().top + window.scrollY - document.querySelector('.site-header').offsetHeight;
      destino = null;
    } else if (siguiente < 0) {
      top = inicio - 160;
      destino = null;
    } else {
      top = inicio + (recorrido * (siguiente + 0.04)) / total;
      destino = siguiente;
    }
    window.scrollTo({ top, behavior: 'smooth' });
    clearTimeout(soltar);
    soltar = setTimeout(() => { destino = null; }, 700);
  }
  window.addEventListener('keydown', teclaPaso);
  window.addEventListener('scroll', agendar, { passive: true });
  window.addEventListener('resize', ajustar, { passive: true });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(ajustar);
  ajustar();
})();

// Servicios: cada bloque entra al aparecer en pantalla, en secuencia con los que llegan junto a él, y las imágenes tienen un parallax suave
(function initScrollLanding() {
  const raiz = document.documentElement;
  if (!raiz.classList.contains('lb') || !('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  raiz.classList.add('lb-anima');
  const bloques = document.querySelectorAll('.lb-propuesta h2, .lb-tarjetas .card, .lb-servicios-cab > *, .lb-servicio, .lb-proceso-top > *, .lb-exp h2, .lb-exp-pie > *, .lb-casos > li, .lb-contacto h2, .lb-contacto-cta, .lb-contacto-pie > div, .lb-retrato');
  const contador = document.querySelector('.lb-anios strong');

  function contar() {
    const inicio = performance.now();
    const paso = (ahora) => {
      const avance = Math.min((ahora - inicio) / 900, 1);
      contador.textContent = `+${Math.round(8 * (1 - (1 - avance) ** 3))}`;
      if (avance < 1) requestAnimationFrame(paso);
    };
    requestAnimationFrame(paso);
  }
  function mostrar(el, turno) {
    el.style.setProperty('--rv-i', turno);
    el.classList.add('is-visto');
    if (el.querySelector('.lb-subraya')) el.classList.add('lb-marcado');
    if (contador && el.contains(contador)) contar();
    // Al terminar se retiran las clases para devolverle al elemento sus propias transiciones
    setTimeout(() => {
      el.classList.remove('lb-rv', 'is-visto');
      el.style.removeProperty('--rv-i');
    }, 900 + turno * 110);
  }
  const observador = new IntersectionObserver((entradas) => {
    let turno = 0;
    entradas.forEach((entrada) => {
      const yaPaso = entrada.boundingClientRect.bottom < 0;
      if (!entrada.isIntersecting && !yaPaso) return;
      observador.unobserve(entrada.target);
      mostrar(entrada.target, yaPaso ? 0 : turno);
      if (!yaPaso) turno += 1;
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.04 });
  bloques.forEach((el) => {
    el.classList.add('lb-rv');
    observador.observe(el);
  });

  const conParallax = [
    ...[...document.querySelectorAll('.lb-tarjetas .pl-tarjeta-img')].map((el) => ({ el, ref: el.closest('.card'), v: 0.06, tope: 0.04 })),
    { el: document.querySelector('.lb-desafio-img > img:first-child'), ref: document.querySelector('.lb-desafio-img'), v: 0.05, tope: 0.05 },
    { el: document.querySelector('.lb-desafio-img i'), ref: document.querySelector('.lb-desafio-img'), v: -0.05, tope: 0.08 },
    { el: document.querySelector('.lb-contacto-logo'), ref: document.querySelector('.lb-contacto-top'), v: 0.06, tope: 0.08 },
  ].filter((p) => p.el && p.ref);
  const amplio = window.matchMedia('(min-width: 40em)');
  let agendado = false;
  function moverParallax() {
    agendado = false;
    const alto = window.innerHeight;
    conParallax.forEach(({ el, ref, v, tope }) => {
      if (!amplio.matches) { el.style.removeProperty('translate'); return; }
      const r = ref.getBoundingClientRect();
      if (r.bottom < -80 || r.top > alto + 80) return;
      const limite = r.height * tope;
      const y = Math.max(-limite, Math.min(limite, (r.top + r.height / 2 - alto / 2) * v));
      el.style.translate = `0 ${y.toFixed(1)}px`;
    });
  }
  function agendarParallax() {
    if (agendado) return;
    agendado = true;
    requestAnimationFrame(moverParallax);
  }
  window.addEventListener('scroll', agendarParallax, { passive: true });
  window.addEventListener('resize', agendarParallax, { passive: true });
  agendarParallax();
})();

// Inicio: los títulos de sección se mueven como el del hero. Cada palabra se separa en su propio elemento; las palabras
// se agrupan por línea y cada línea entra desde abajo y se desplaza en horizontal con el scroll (una a la izquierda y la
// siguiente a la derecha). Solo en la home (html.inicio); el hero y el titular de contacto tienen su propio código.
(function initSectionTitles() {
  // La landing B (html.lb) usa títulos estáticos
  if (!document.documentElement.classList.contains('inicio') || document.documentElement.classList.contains('lb') || window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
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

// Inglés: cada objeto de ideas nace desde el hueco entre las palabras de su línea y luego se mueve a su lugar final (CSS)
(function alinearObjetosIdeasEn() {
  if (document.documentElement.lang !== 'en') return;
  const sec = document.getElementById('ideas');
  const collage = sec && sec.querySelector('.ideas-collage');
  if (!collage) return;
  const objetos = ['ideas-item-phone', 'ideas-item-beer', 'ideas-item-spray']; // de la línea de arriba a la de abajo
  const sonda = document.createElement('div'); // mide --ideas-fs en píxeles
  sonda.style.cssText = 'position:absolute;visibility:hidden;width:var(--ideas-fs)';
  function alinear() {
    const stage = sec.querySelector('.ideas-stage') || sec;
    stage.appendChild(sonda);
    const fs = sonda.getBoundingClientRect().width || 1;
    sonda.remove();
    const lineas = sec.querySelectorAll('.ideas-title > .ideas-line');
    const c = collage.getBoundingClientRect();
    objetos.forEach((clase, i) => {
      const item = sec.querySelector(`.${clase}`);
      const linea = lineas[i];
      const hueco = linea && linea.querySelector(':scope > .ideas-gap');
      if (!item || !hueco) return;
      const g = hueco.getBoundingClientRect();
      if (g.width === 0) { item.style.removeProperty('--line-x'); item.style.removeProperty('--line'); return; } // móvil: el hueco está oculto
      const l = linea.getBoundingClientRect();
      // Punto de partida de la animación (ver @keyframes ideas-item-in): left = 50% + --line-x·fs, top = 50% + --line·0.95·fs
      item.style.setProperty('--line-x', `${(g.left + g.width / 2 - (c.left + c.width / 2)) / fs}`);
      item.style.setProperty('--line', `${(l.top + l.height / 2 - (c.top + c.height / 2)) / (0.95 * fs)}`);
    });
  }
  alinear();
  window.addEventListener('resize', alinear);
  if (document.fonts) document.fonts.ready.then(alinear);
})();

// Inicio: carrusel de noticias complementarias. Cada botón desplaza una tarjeta (sin librerías)
(function initBlogCarrusel() {
  const suave = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('[data-carrusel]').forEach((carrusel) => {
    const pista = carrusel.querySelector('.pl-carrusel-pista');
    if (!pista) return;
    carrusel.querySelectorAll('[data-paso]').forEach((boton) => {
      boton.addEventListener('click', () => {
        const tarjeta = pista.querySelector(':scope > li');
        const avance = tarjeta.offsetWidth + parseFloat(getComputedStyle(pista).columnGap || 0);
        pista.scrollBy({ left: Number(boton.dataset.paso) * avance, behavior: suave ? 'smooth' : 'auto' });
      });
    });
  });
})();
