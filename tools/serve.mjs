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

createServer(async (req, res) => {
  try {
    let path = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
    if (path.endsWith('/')) path += 'index.html';
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
