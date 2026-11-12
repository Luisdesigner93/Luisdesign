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
})();
