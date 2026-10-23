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
