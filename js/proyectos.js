// Página de proyectos: filtros por tipo de trabajo y disciplina.
// Un valor activo por grupo; volver a pulsarlo lo quita. Sin JavaScript se ven todos los casos.
(function () {
  var items = document.querySelectorAll('.pj-item');
  if (!items.length) return;
  var activos = {};
  var total = document.querySelector('[data-pj-total]');
  var vacio = document.querySelector('.pj-empty');
  document.querySelectorAll('.pj-chip').forEach(function (b) {
    b.addEventListener('click', function () {
      var g = b.dataset.grupo;
      var on = activos[g] !== b.dataset.valor;
      document.querySelectorAll('.pj-chip[data-grupo="' + g + '"]').forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
      if (on) { activos[g] = b.dataset.valor; b.setAttribute('aria-pressed', 'true'); } else { delete activos[g]; }
      var n = 0;
      items.forEach(function (it) {
        var f = ' ' + it.dataset.filtros + ' ';
        var ok = Object.keys(activos).every(function (k) { return f.indexOf(' ' + activos[k] + ' ') > -1; });
        it.hidden = !ok;
        if (ok) n++;
      });
      if (total) total.textContent = '(' + n + ')';
      vacio.hidden = n > 0;
    });
  });

  // Pantallas táctiles (sin hover): el primer toque muestra la capa con disciplinas, año y «Ver proyecto»;
  // el segundo abre el caso. Tocar fuera de las tarjetas cierra la capa.
  var sinHover = window.matchMedia('(hover: none)');
  var tarjetas = document.querySelectorAll('.pj-card');
  function cerrar(excepto) {
    tarjetas.forEach(function (t) { if (t !== excepto) t.classList.remove('is-open'); });
  }
  tarjetas.forEach(function (t) {
    t.addEventListener('click', function (e) {
      if (!sinHover.matches || t.classList.contains('is-open')) return;
      e.preventDefault();
      cerrar(t);
      t.classList.add('is-open');
    });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.pj-card')) cerrar(null);
  });
})();

// Proyectos: cada tarjeta alterna su portada con otras dos imágenes del caso, en orden aleatorio: se sortea qué tarjeta
// cambia y qué imagen muestra. Solo en pantalla, se detiene con el mouse o la capa abierta y no corre con "reducir movimiento".
(function () {
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var FUNDIDO = 950;
  var ESPERA_MIN = 700;
  var ESPERA_MAX = 1500;
  var visibles = new WeakSet();
  var observador = 'IntersectionObserver' in window ? new IntersectionObserver(function (entradas) {
    entradas.forEach(function (e) { if (e.isIntersecting) visibles.add(e.target); else visibles.delete(e.target); });
  }, { threshold: 0.2 }) : null;
  var azar = function (lista) { return lista[Math.floor(Math.random() * lista.length)]; };
  var cargada = function (img) { return img.complete && img.naturalWidth > 0; };

  var tarjetas = [];
  document.querySelectorAll('.pj-card').forEach(function (el) {
    var extra = Array.prototype.slice.call(el.querySelectorAll('.pj-rota'));
    if (extra.length < 2) return;
    if (observador) observador.observe(el); else visibles.add(el);
    // actual: imagen extra a la vista; null es la portada
    tarjetas.push({ el: el, extra: extra, actual: null, ocupada: false });
  });
  if (!tarjetas.length) return;

  var cambiar = function (t) {
    var opciones = [null].concat(t.extra).filter(function (img) { return img !== t.actual && (img === null || cargada(img)); });
    if (!opciones.length) return false;
    var nueva = azar(opciones);
    var previa = t.actual;
    t.ocupada = true;
    t.actual = nueva;
    if (nueva) {
      // La nueva aparece encima; la anterior se retira cuando ya quedó cubierta
      if (previa) previa.style.zIndex = 1;
      nueva.style.zIndex = 2;
      nueva.classList.add('is-activa');
    } else if (previa) {
      previa.classList.remove('is-activa');
    }
    setTimeout(function () {
      if (previa && nueva) { previa.classList.remove('is-activa'); previa.style.zIndex = ''; }
      t.ocupada = false;
    }, FUNDIDO);
    return true;
  };

  var ultima = null;
  var turno = function () {
    if (!document.hidden) {
      var libres = tarjetas.filter(function (t) {
        return visibles.has(t.el) && !t.ocupada && !t.el.matches(':hover') && !t.el.classList.contains('is-open');
      });
      var candidatas = libres.length > 1 ? libres.filter(function (t) { return t !== ultima; }) : libres;
      if (candidatas.length) {
        var elegida = azar(candidatas);
        if (cambiar(elegida)) ultima = elegida;
      }
    }
    setTimeout(turno, ESPERA_MIN + Math.random() * (ESPERA_MAX - ESPERA_MIN));
  };
  setTimeout(turno, ESPERA_MAX);
})();
