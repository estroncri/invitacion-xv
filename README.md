# Invitación XV Años — Jireth Carolina

Invitación digital en una página HTML. No necesita servidor ni base de datos:
las imágenes van embebidas en base64 dentro del propio `index.html`. La música
va aparte, en `musica.mp3`, para que la página abra al instante.

## Cómo se ve

Se abre con un sobre que hay que tocar. Al abrirlo arranca la música y se pasa
pantalla por pantalla con el botón de la flecha (también funciona deslizando
o con las flechas del teclado).

## Dónde está publicada

<https://invitaciónjirethcervera.online>

**Ojo con la tilde.** El dominio comprado es `invitaciónjirethcervera.online`,
con tilde en la ó. Es un dominio internacionalizado (IDN), y su forma real
para las máquinas es el punycode `xn--invitacinjirethcervera-2fc.online` — que
es lo que va en el archivo `CNAME` de este repo. La versión **sin** tilde,
`invitacionjirethcervera.online`, es otro dominio distinto y no está
registrado: quien la escriba a mano no llega. Por eso la invitación conviene
repartirla siempre como link, nunca dictada.

`www.` también funciona y redirige al dominio principal, igual que el viejo
`estroncri.github.io/invitacion-xv/`.

DNS en Hostinger: cuatro registros A en el apex hacia 185.199.108-111.153 y un
CNAME `www` → `estroncri.github.io`. HTTPS emitido y forzado por GitHub.

Cada `git push` a `main` vuelve a publicar solo, en 1-2 minutos.

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

La música es el archivo `musica.mp3` que está al lado del `index.html`.
Para cambiarla, poné tu MP3 en esta misma carpeta y corré:

```
python cambiar-musica.py mi-cancion.mp3
```

El script lo copia sobre `musica.mp3` y deja una copia de seguridad del
anterior (`musica.mp3.bak`). Después hay que subirlo con `git push` para que
el cambio llegue a la página publicada.

A mano es lo mismo: reemplazar `musica.mp3` por otro MP3 con ese nombre.

Va aparte y no embebida a propósito. Metida en base64 dentro del HTML, una
canción de 4 MB deja la página en ~7 MB y el invitado tiene que bajarla
entera antes de ver el sobre. Como archivo suelto, la página abre de una y
el audio se descarga mientras tanto.

Es una canción comercial en un repo público: queda descargable por cualquiera,
no solo reproducible en la invitación. Para una invitación familiar no suele
pasar nada, pero si llega un reclamo GitHub la baja.

## Datos del evento

- Sábado 7 de Noviembre de 2026, 9:00 PM
- Carrera 3c # 49e 51
- Confirmaciones por WhatsApp
