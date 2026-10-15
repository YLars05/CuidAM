# CuidAM Frames - SIGMA Hackathon 15-10-26 ETSINF-UPV

Presentación web interactiva de una propuesta de detección pasiva de residuos e incidencias urbanas en la ciudad de València mediante fotogramas capturados desde vehículos en circulación.

## Abrir la web

Abre `index.html` o `cuidam-frames.html` en un navegador. No requiere dependencias ni compilación; las imágenes están incorporadas en el HTML.

Para servirla en una red local:

```sh
python3 -m http.server 8766 --bind 0.0.0.0
```

Desde otro equipo de la misma red, abre `http://IP_DEL_EQUIPO:8766`.

## Contenido

- Explicación del proyecto y detección de basura en la vía pública.
- Propuesta de cámaras en 44 autobuses y sensores de llenado selectivos.
- Esquema de corredores EMT y referencias documentales.
- Presupuesto interactivo y simulador de recuperación de inversión.

## Alcance de las cifras

Los costes y ahorros son escenarios de planificación, no ofertas ni resultados demostrados. El gasto de servicio de 5 millones de euros y los porcentajes de ahorro del simulador son supuestos ilustrativos, no datos municipales verificados. El plazo de recuperación resultante no es una garantía: requiere validar costes y ahorro efectivo mediante un piloto.

Propuesta conceptual independiente, sin vinculación institucional oficial con el Ayuntamiento de Valencia o EMT.

## Versiones conservadas

| Archivo | Estado y diferencias |
| --- | --- |
| `cuidam-frames.html` | Versión actual recomendada. La ilustración de portada detecta basura (botella, papel y lata) y muestra «BASURA EN LA CALLE». |
| `ciudadframes.html` | Copia anterior conservada con su nombre original. La portada señala un posible daño en el firme. El contenido ya usa la marca CuidAM Frames. |
| `valencia-circular.html` | Copia idéntica a `ciudadframes.html`, conservada por trazabilidad del nombre anterior. No es una tercera implementación distinta. |
| `index.html` | Acceso directo a la versión actual. |

## Descargar y ejecutar en otro dispositivo

1. En GitHub, pulsa **Code → Download ZIP**, o ejecuta `git clone https://github.com/YLars05/CuidAM.git`.
2. Extrae el ZIP y abre `index.html`. Funciona en navegadores modernos sin instalar librerías.
3. Para compartirlo por Wi-Fi, instala Python 3 y ejecuta `python3 serve.py` (en Windows: `py serve.py`).
4. En el equipo servidor abre `http://localhost:8766`. En otro equipo de la misma red usa `http://IP_LOCAL_DEL_SERVIDOR:8766`.
5. Mantén el servidor encendido. Para detenerlo pulsa Ctrl+C. La red debe permitir conexiones entre dispositivos y el cortafuegos debe permitir Python.

## Construcción y edición

No hay proceso de compilación, npm ni dependencias. Los tres HTML son archivos fuente completos con CSS, JavaScript e imágenes incorporados; no necesitan carpetas de imágenes externas. Edita `cuidam-frames.html` para cambiar la versión actual. Los enlaces a fuentes externas requieren Internet. `serve.py` usa exclusivamente la biblioteca estándar de Python y sirve esta carpeta.
