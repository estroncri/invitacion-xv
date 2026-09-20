# Invitación XV Años — Jireth Carolina

Invitación digital en una sola página HTML. No necesita servidor, base de datos
ni archivos externos: las imágenes y la música van embebidas en base64.

## Cómo se ve

Se abre con un sobre que hay que tocar. Al abrirlo arranca la música y se pasa
pantalla por pantalla con el botón de la flecha (también funciona deslizando
o con las flechas del teclado).

## Dónde está publicada

<https://estroncri.github.io/invitacion-xv/>

GitHub Pages ya está configurado en la rama `main`, carpeta raíz. Cada
`git push` a `main` vuelve a publicar solo, en 1-2 minutos.

## Privacidad

El archivo lleva el nombre completo de una menor de edad, una dirección y un
número de teléfono. Incluye `robots.txt` y la etiqueta `noindex`, así que no
debería aparecer en buscadores.

**El repositorio es público**, porque GitHub Pages solo funciona con repos
públicos en las cuentas gratuitas. Eso significa que esos datos están a la
vista de cualquiera que abra el repo, no solo de quien tenga el link de la
invitación. Para cerrarlo hay que pasar el repo a privado (se cae Pages) y
publicar la invitación en Netlify, Cloudflare Pages o Vercel, que sí sirven
sitios estáticos desde repos privados sin costo.

## El mapa

La pantalla «El Lugar» trae un mapa de Google embebido apuntando a
Carrera 3C # 49E-51, Barranquilla. Va con un filtro CSS que lo oscurece para
que combine con el azul de la invitación. Es el único recurso que la página
pide a internet: sin conexión, todo lo demás sigue funcionando.

Para mover el mapa a otra dirección hay que cambiar la consulta en los dos
lugares donde aparece dentro de `index.html`: el `src` del `<iframe>` y el
`href` del botón «Cómo llegar».

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
