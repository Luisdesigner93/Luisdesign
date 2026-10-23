'use strict';

// Tema claro/oscuro. Se carga en <head> sin defer para fijar el tema antes de pintar la página (evita el destello claro).
// Prioridad: elección guardada del visitante > preferencia del sistema. Sin JavaScript, el sitio queda en claro.
(function initTheme() {
  const KEY = 'theme';
  const root = document.documentElement;
  const media = window.matchMedia('(prefers-color-scheme: dark)');

  const read = () => { try { return localStorage.getItem(KEY); } catch { return null; } };
  const save = (value) => { try { localStorage.setItem(KEY, value); } catch { /* almacenamiento no disponible */ } };

  function apply(theme) {
    root.dataset.theme = theme;
    const meta = document.querySelector('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', theme === 'dark' ? '#070b13' : '#ffffff');
    document.querySelectorAll('.theme-toggle').forEach((button) => {
      const dark = theme === 'dark';
      button.setAttribute('aria-pressed', String(dark));
      const en = document.documentElement.lang.startsWith('en');
      button.setAttribute('aria-label', dark ? (en ? 'Switch to light mode' : 'Cambiar a modo claro') : (en ? 'Switch to dark mode' : 'Cambiar a modo oscuro'));
    });
  }

  // Pantalla de carga: solo la primera página de la visita y si no se prefiere menos movimiento.
  try {
    if (!sessionStorage.getItem('intro') && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) root.classList.add('is-loading');
  } catch { /* sin almacenamiento: sin pantalla de carga */ }

  const stored = read();
  apply(stored === 'dark' || stored === 'light' ? stored : (media.matches ? 'dark' : 'light'));

  // Si el visitante no ha elegido, sigue los cambios del sistema.
  media.addEventListener('change', (e) => { if (!read()) apply(e.matches ? 'dark' : 'light'); });

  document.addEventListener('DOMContentLoaded', () => {
    apply(root.dataset.theme);
    document.querySelectorAll('.theme-toggle').forEach((button) => {
      button.addEventListener('click', () => {
        const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
        save(next);
        apply(next);
      });
    });
  });
})();
