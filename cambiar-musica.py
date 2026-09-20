#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cambia la musica de fondo de la invitacion.

Uso:
    python cambiar-musica.py mi-cancion.mp3

La musica va como archivo aparte (musica.mp3, al lado del index.html), no
embebida en el HTML. Este script solo pone tu MP3 en su lugar, guardando
una copia de seguridad del anterior.

Despues hay que subirlo:
    git add musica.mp3 && git commit -m "Nueva musica" && git push
"""
import sys, os, shutil

DESTINO = 'musica.mp3'


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1

    mp3 = sys.argv[1]
    if not os.path.isfile(mp3):
        print("No encuentro el MP3:", mp3)
        return 1
    if not mp3.lower().endswith('.mp3'):
        print("Ojo: el archivo no termina en .mp3. El navegador puede no reproducirlo.")

    carpeta = os.path.dirname(os.path.abspath(__file__))
    destino = os.path.join(carpeta, DESTINO)

    if os.path.abspath(mp3) == destino:
        print("Ese ya es el archivo de musica actual, no hay nada que cambiar.")
        return 0

    mb = os.path.getsize(mp3) / 1024 / 1024
    if mb > 8:
        print(f"Ojo: el MP3 pesa {mb:.1f} MB.")
        print("Como va aparte, la pagina abre igual de rapido, pero el invitado")
        print("gasta esos datos para escuchar la cancion completa.")
        if input("¿Sigo igual? (s/n): ").strip().lower() not in ('s', 'si', 'sí'):
            return 1

    if os.path.isfile(destino):
        shutil.copy2(destino, destino + '.bak')
        print("Copia de seguridad:", DESTINO + '.bak')

    shutil.copy2(mp3, destino)
    print(f"Listo. Musica cambiada por: {os.path.basename(mp3)} ({mb:.2f} MB)")
    print("Falta subirlo:  git add musica.mp3 && git commit -m \"Nueva musica\" && git push")
    return 0


if __name__ == '__main__':
    sys.exit(main())
