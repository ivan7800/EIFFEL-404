# EIFFEL 404

> Experiencia web interactiva para explorar una interpretación artística 3D de la Torre Eiffel y un entorno inspirado en París.

[**Abrir la demo en GitHub Pages**](https://ivan7800.github.io/EIFFEL-404/)

![Estado de GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-publicado-2ea44f?logo=github)
![Tecnologías](https://img.shields.io/badge/HTML-CSS-JavaScript-orange)
![Modelos](https://img.shields.io/badge/3D-WebGL%20%2B%20Canvas-blue)

## Estado actual

**Release candidata, no certificada como versión final.** La página publicada carga y ofrece el modo Canvas de compatibilidad, pero en la comprobación actual de GitHub Pages no inició WebGL: las funciones de ascensor, mirador, visita guiada, entorno París, bruma, destellos, exposición y Cinema aparecieron desactivadas. La causa de ese fallo todavía no está confirmada.

La cobertura automatizada incluida es mixta: hay comprobaciones funcionales del modo Canvas y pruebas de controles WebGL con GLB inyectados o con un contexto WebGL simulado. Esas pruebas no equivalen a validar el arranque real de los tres modelos en navegadores/GPU de usuarios. Consulta [QA.md](QA.md) para límites y comandos.

## Qué incluye

- Exploración interactiva de la torre: giro, zoom, niveles, día/noche, recorrido panorámico, captura PNG y pantalla completa.
- Tres modelos GLB locales para torre, ciudad y jardines.
- Motor WebGL local y renderizador Canvas de compatibilidad.
- Controles WebGL adicionales: ocaso, ascensor, mirador, visita guiada, bruma, destellos, exposición y modo Cinema.
- Sonido desactivado en el motor WebGL local; la interfaz informa de las funciones no disponibles.
- Modelos estilizados: no son fotogrametría, CAD de precisión ni un gemelo digital.

## Ejecutar en Windows

1. Descarga el ZIP desde **Code → Download ZIP** y descomprímelo.
2. Instala Python 3 si el equipo no lo tiene.
3. Ejecuta `INICIAR_WINDOWS.bat`.
4. Abre `http://localhost:8000/` si no se abre automáticamente.

El servidor local permite cargar los GLB. Al abrir `index.html` con `file://`, se utiliza el Canvas de reserva y el modelo GLB no se carga.

## Ejecutar en otros sistemas

Desde la carpeta del proyecto:

```bash
python3 -m http.server 8000
```

Abre [http://localhost:8000](http://localhost:8000).

## Controles

| Acción | Control |
|---|---|
| Girar | Arrastrar con ratón o dedo |
| Acercar/alejar | Rueda del ratón o gesto de pellizco |
| Cambiar nivel | Botones de nivel o teclas `1`–`4` |
| Día / noche / ocaso | Botones; teclas `D`, `N`, `O` cuando WebGL está activo |
| Modo foto | Botón o tecla `P`; `Escape` para salir |
| Reiniciar | Botón **REINICIAR** |

En Canvas solo están disponibles las funciones implementadas en ese motor. La interfaz desactiva los controles WebGL que no puede ofrecer.

## Estructura

- `index.html`, `styles.css`: interfaz.
- `offline-webgl.js`: motor WebGL sin dependencias externas.
- `app.js`: renderizador Canvas de compatibilidad.
- `assets/*.glb`: modelos 3D locales.
- `assets/architecture-reference.json`: referencias de dimensiones y fuentes oficiales.
- `generate_model.py`: generador de la geometría Eiffel; requiere Python, NumPy y trimesh.
- `blender/crear_torre.py`: prototipo Blender independiente; no reproduce por sí solo todos los modelos GLB publicados.
- `tests/`: pruebas Playwright y capturas de pruebas previas.

## Regenerar el modelo Eiffel

```bash
python -m pip install numpy trimesh
python generate_model.py
```

El script sobrescribe `assets/eiffel_404.glb`. Los GLB de París se distribuyen como recursos ya generados.

## Pruebas

Consulta [QA.md](QA.md). Las pruebas Playwright requieren Python, Chromium y Playwright; las pruebas WebGL usan rutas de simulación y necesitan complementarse con una prueba del sitio servido en navegador real. El proyecto todavía no configura CI automatizada.

## Datos arquitectónicos

Las dimensiones de referencia y fuentes se registran en [assets/architecture-reference.json](assets/architecture-reference.json). La escena y sus proporciones intermedias son interpretaciones visuales; no deben utilizarse para medición técnica.

## Créditos y licencia

Proyecto independiente, sin afiliación con la Société d'Exploitation de la Tour Eiffel. Las marcas y el monumento pertenecen a sus titulares correspondientes.

No se ha especificado una licencia de código en este repositorio. Por tanto, el código y los recursos no se ofrecen bajo una licencia de reutilización explícita. Consulta con el autor antes de reutilizarlos o redistribuirlos.

---

**Versión mostrada por la aplicación:** v7.6 RC  
**Commit revisado:** [`3037eb4`](https://github.com/ivan7800/EIFFEL-404/commit/3037eb4e70b9ec6afaeaaf4bcf80c41df8b91429)