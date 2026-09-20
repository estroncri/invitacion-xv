#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cambia la musica de fondo de la invitacion.

Uso:
    python cambiar-musica.py mi-cancion.mp3
    python cambiar-musica.py mi-cancion.mp3 otro-archivo.html

Deja una copia de seguridad (.bak) antes de tocar nada.
"""
import sys, os, re, base64, shutil

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1

    mp3 = sys.argv[1]
    html = sys.argv[2] if len(sys.argv) > 2 else 'index.html'

    if not os.path.isfile(mp3):
        print("No encuentro el MP3:", mp3)
        return 1
    if not os.path.isfile(html):
        print("No encuentro el HTML:", html)
        return 1

    mb = os.path.getsize(mp3) / 1024 / 1024
    if mb > 4:
        print(f"Ojo: el MP3 pesa {mb:.1f} MB. Al meterlo en el HTML crece ~33%,")
        print("o sea que la pagina va a quedar pesada para abrir desde datos.")
        print("Recomendado: 2 MB o menos (recortalo a 1-2 minutos y bajalo a 96 kbps).")
        if input("¿Sigo igual? (s/n): ").strip().lower() not in ('s', 'si', 'sí'):
            return 1

    with open(mp3, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode('ascii')

    with open(html, encoding='utf-8') as f:
        doc = f.read()

    patron = r'(<audio id="bgm"[^>]*src="data:audio/mpeg;base64,)[^"]*(")'
    if not re.search(patron, doc):
        print("No encontre la etiqueta <audio id=\"bgm\"> en", html)
        return 1

    shutil.copy2(html, html + '.bak')
    doc = re.sub(patron, lambda m: m.group(1) + b64 + m.group(2), doc, count=1)

    with open(html, 'w', encoding='utf-8') as f:
        f.write(doc)

    nuevo = os.path.getsize(html) / 1024 / 1024
    print(f"Listo. Musica cambiada por: {os.path.basename(mp3)}")
    print(f"{html} quedo en {nuevo:.2f} MB")
    print(f"Copia de seguridad: {html}.bak")
    return 0

if __name__ == '__main__':
    sys.exit(main())
