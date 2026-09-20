# Invitación XV Años — Jireth Carolina

Invitación digital en una sola página HTML. No necesita servidor, base de datos
ni archivos externos: las imágenes y la música van embebidas en base64.

## Cómo se ve

Se abre con un sobre que hay que tocar. Al abrirlo arranca la música y se pasa
pantalla por pantalla con el botón de la flecha (también funciona deslizando
o con las flechas del teclado).

## Publicar con GitHub Pages

1. Settings → Pages
2. Source: `Deploy from a branch`
3. Branch: `main` / carpeta `/ (root)` → Save
4. A los 1-2 minutos queda en `https://USUARIO.github.io/REPO/`

## Privacidad

El archivo lleva el nombre completo de una menor de edad, una dirección y un
número de teléfono. Por eso incluye `robots.txt` y la etiqueta `noindex`, para
que no aparezca en Google. Aun así, cualquiera con el link puede verlo:
**no publiques el repositorio como público si no querés que el código quede
a la vista** (GitHub Pages funciona igual con repo privado en cuentas Pro;
en cuentas gratuitas el repo debe ser público).

## Cambiar la música

La pista actual es generada, de relleno. Para cambiarla, poné tu MP3 en esta
misma carpeta y corré:

```
python cambiar-musica.py mi-cancion.mp3
```

El script mete el MP3 dentro del `index.html` y deja una copia de seguridad
(`index.html.bak`). Recomendado: un MP3 de 2 MB o menos (1-2 minutos a 96 kbps),
porque al incrustarlo el archivo crece alrededor de un 33%.

A mano también se puede: reemplazar todo lo que va después de
`base64,` en el `src` de `<audio id="bgm">`.

## Datos del evento

- Sábado 7 de Noviembre de 2026, 9:00 PM
- Carrera 3c # 49e 51
- Confirmaciones por WhatsApp
