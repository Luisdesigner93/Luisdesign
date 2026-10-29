// Pantalla de carga: solo la primera página de la visita y si no se prefiere menos movimiento.
// Se carga en <head> sin defer para marcar la página antes de pintarla.
(function initIntro() {
  try {
    if (!sessionStorage.getItem('intro') && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      document.documentElement.classList.add('is-loading');
    }
  } catch { /* sin almacenamiento: sin pantalla de carga */ }
})();
