// Servidor estático solo para vista previa local (no se publica). Uso: node tools/serve.mjs [puerto]
import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { extname, join, normalize, resolve, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(fileURLToPath(new URL('..', import.meta.url)));
const PORT = Number(process.env.PORT || process.argv[2] || 4173);
const TYPES = { '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.txt': 'text/plain; charset=utf-8', '.xml': 'application/xml', '.ico': 'image/x-icon', '.png': 'image/png', '.webp': 'image/webp' };
// Mismas cabeceras que .htaccess, para detectar violaciones de CSP en local.
const HEADERS = {
  'Content-Security-Policy': "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; font-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'; object-src 'none'",
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  // Solo en local: evita ver versiones antiguas en caché mientras se desarrolla.
  'Cache-Control': 'no-store',
};

// Este servidor no ejecuta PHP. Solo en local, simula contacto/agenda.php con los horarios de la plantilla:
// no consulta Google, no guarda nada y no envía invitaciones.
const ZONA = 'America/Santiago';
const HORAS = ['09:00', '14:00', '17:00'];
const DIAS_AGENDA = [1, 3, 5];
const ANTICIPACION = 2;
const SEMANAS = 4;
const BLOQUEADOS = ['2026-12-08', '2026-12-25'];
const iso = (fecha) => fecha.toISOString().slice(0, 10);
function desfase(dia) {
  const parte = new Intl.DateTimeFormat('en-US', { timeZone: ZONA, timeZoneName: 'longOffset' })
    .formatToParts(new Date(`${dia}T15:00:00Z`)).find((p) => p.type === 'timeZoneName').value;
  return parte.replace('GMT', '') || '+00:00';
}
function semanasSimuladas() {
  const hoy = new Date(`${new Intl.DateTimeFormat('en-CA', { timeZone: ZONA }).format(new Date())}T00:00:00Z`);
  const minimo = new Date(hoy.getTime() + ANTICIPACION * 864e5);
  const lunes = new Date(hoy.getTime() - ((hoy.getUTCDay() + 6) % 7) * 864e5);
  return Array.from({ length: SEMANAS }, (_, s) => {
    const inicio = new Date(lunes.getTime() + s * 7 * 864e5);
    const dias = DIAS_AGENDA.map((n) => {
      const dia = new Date(inicio.getTime() + (n - 1) * 864e5);
      const fecha = iso(dia);
      const libre = dia >= minimo && !BLOQUEADOS.includes(fecha);
      return { fecha, horas: libre ? HORAS.map((hora) => ({ inicio: `${fecha}T${hora}:00${desfase(fecha)}`, hora })) : [] };
    });
    return { lunes: iso(inicio), dias };
  });
}
function agendaSimulada(req, res) {
  req.resume();
  const datos = req.method === 'POST'
    ? { ok: true, mensaje: 'Reunión simulada en local: no se envió nada.' }
    : { ok: true, disponible: true, duracion: 20, semanas: semanasSimuladas() };
  res.writeHead(200, { ...HEADERS, 'Content-Type': 'application/json; charset=utf-8' });
  res.end(JSON.stringify(datos));
}

createServer(async (req, res) => {
  try {
    const url = new URL(req.url, 'http://localhost');
    if (url.pathname === '/contacto/agenda.php') return agendaSimulada(req, res);
    let path = decodeURIComponent(url.pathname);
    // Como .htaccess: /pagina.html y /carpeta/index.html redirigen (301) a /pagina y /carpeta/
    if (path.endsWith('.html') && !path.endsWith('/404.html') && !/^\/google[0-9a-f]+\.html$/.test(path)) {
      const limpio = path.replace(/(^|\/)index\.html$/, '$1').replace(/\.html$/, '');
      res.writeHead(301, { ...HEADERS, Location: limpio + url.search });
      return res.end();
    }
    if (path.endsWith('/')) path += 'index.html';
    // /pagina sirve pagina.html
    else if (!extname(path)) {
      const conHtml = normalize(join(ROOT, path + '.html'));
      if (await stat(conHtml).then((s) => s.isFile(), () => false)) path += '.html';
    }
    const file = normalize(join(ROOT, path));
    // Evita path traversal y archivos ocultos o de herramientas.
    if (!file.startsWith(ROOT + sep) || /[\\/]\.|[\\/]tools[\\/]/.test(file.slice(ROOT.length))) throw Object.assign(new Error(), { code: 'ENOENT' });
    if (!(await stat(file)).isFile()) throw Object.assign(new Error(), { code: 'ENOENT' });
    res.writeHead(200, { ...HEADERS, 'Content-Type': TYPES[extname(file)] || 'application/octet-stream' });
    res.end(await readFile(file));
  } catch {
    const body = await readFile(join(ROOT, '404.html')).catch(() => 'No encontrado');
    res.writeHead(404, { ...HEADERS, 'Content-Type': 'text/html; charset=utf-8' });
    res.end(body);
  }
}).listen(PORT, '127.0.0.1', () => console.log(`luisdesign en http://localhost:${PORT}`));
