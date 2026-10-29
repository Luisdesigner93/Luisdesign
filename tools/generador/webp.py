#!/usr/bin/env python3
"""Genera las versiones WebP de las imágenes del sitio en img/webp/ (requiere cwebp: brew install webp).

Uso: python3 tools/generador/webp.py
Por cada JPG o PNG de img/proyectos, img/marca e img/collage crea hasta tres anchos (480, 960 y 1600 px,
sin superar el original). Los originales se mantienen como fuente; build.py usa los WebP en el HTML.
Solo regenera lo que falta o lo que es más antiguo que su original.
"""
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
CARPETAS = ('proyectos', 'marca', 'collage')
ANCHOS = (480, 960, 1600)
# Las imágenes de la sección Ideas (collage) se muestran pequeñas: solo se genera el tamaño que necesita la pantalla
ANCHOS_COLLAGE = (480,)
# Calidad menor para imágenes de fondo o producto donde la compresión extra no se nota (clave: ruta sin extensión, relativa a img/)
CALIDAD = {'marca/hero-fondo': 65, 'collage/fuchi-chao-eliminador': 70, 'collage/khronos-stout': 70, 'collage/yomecontrolo-telefono': 70}


def ancho_original(path):
    out = subprocess.run(['sips', '-g', 'pixelWidth', str(path)], capture_output=True, text=True, check=True).stdout
    return int(out.strip().split()[-1])


def anchos(w, lista=ANCHOS):
    return sorted({min(a, w) for a in lista if a <= w} | ({w} if w < lista[-1] else set()))


def main():
    if not shutil.which('cwebp'):
        sys.exit('Falta cwebp (brew install webp).')
    hechos = 0
    for carpeta in CARPETAS:
        for src in sorted((ROOT / 'img' / carpeta).rglob('*')):
            if src.suffix.lower() not in ('.jpg', '.jpeg', '.png'):
                continue
            rel = src.relative_to(ROOT / 'img').with_suffix('')
            w = ancho_original(src)
            for a in anchos(w, ANCHOS_COLLAGE if carpeta == 'collage' else ANCHOS):
                dest = ROOT / 'img' / 'webp' / f'{rel}-{a}.webp'
                if dest.exists() and dest.stat().st_mtime >= src.stat().st_mtime:
                    continue
                dest.parent.mkdir(parents=True, exist_ok=True)
                # Fotos: calidad 78; PNG con transparencia: se conserva el canal alfa
                q = CALIDAD.get(str(rel), 82 if src.suffix.lower() == '.png' else 78)
                calidad = ['-q', str(q), '-alpha_q', '90'] if src.suffix.lower() == '.png' else ['-q', str(q)]
                tam = ['-resize', str(a), '0'] if a < w else []
                subprocess.run(['cwebp', '-quiet', '-metadata', 'none', *calidad, *tam, str(src), '-o', str(dest)], check=True)
                hechos += 1
    print(f'{hechos} imágenes WebP generadas')


if __name__ == '__main__':
    main()
