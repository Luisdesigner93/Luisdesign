// Pantalla de carga: la firma completa en la primera página de la visita y, al pasar entre páginas, el logo ya dibujado
// mientras carga la siguiente. Se respeta "reducir movimiento". Se carga en <head> sin defer para marcar la página antes de pintarla.
(function initIntro() {
  try {
    const root = document.documentElement;
    const salida = Number(sessionStorage.getItem('transicion'));
    sessionStorage.removeItem('transicion');
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    if (salida && Date.now() - salida < 8000) root.classList.add('is-loading', 'is-transition');
    else if (!sessionStorage.getItem('intro')) root.classList.add('is-loading');
  } catch { /* sin almacenamiento: sin pantalla de carga */ }
})();
