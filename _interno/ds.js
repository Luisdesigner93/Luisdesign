// Página interna del design system: las etiquetas de prueba se activan y desactivan al hacer clic
document.querySelectorAll('.ds-prueba .pj-chip').forEach(function (b) {
  b.addEventListener('click', function () { b.setAttribute('aria-pressed', b.getAttribute('aria-pressed') === 'true' ? 'false' : 'true'); });
});
