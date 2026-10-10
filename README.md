# EIFFEL 404 — v7.2 · Etapa 3: modelo enriquecido

**Objetivo:** elevar el detalle arquitectónico del modelo GLB sin cambiar el contrato con el visor WebGL local de v7.1.

## Ejecutar
Descomprime el archivo y ejecuta `INICIAR_WINDOWS.bat` con Python 3 instalado. Abre la URL local que indique el lanzador. Si abres `index.html` directamente con `file://`, la aplicación utiliza el renderizador Canvas de reserva, que no carga el modelo GLB.

## Qué cambia
Nuevo `assets/eiffel_404.glb` con 35.448 vértices, 59.080 triángulos, celosías secundarias, plataformas con barandillas, guías de ascensor, pisos y antena. Es una reconstrucción **estilizada**, no un modelo métrico exacto ni fotogrametría.

Se incluye `generate_model.py` para reproducir el GLB con `numpy` y `trimesh` (`pip install numpy trimesh`). `blender/crear_torre.py` se conserva como prototipo de una torre editable en Blender; NO exporta automáticamente la geometría actual de alta densidad. Para editar esta versión en Blender, importa `assets/eiffel_404.glb` desde Archivo > Importar > glTF 2.0.

## Estado de la aplicación
La arquitectura WebGL nativa y el modo Canvas de reserva son los de v7.1. La fase de integración de Three.js local sigue pendiente, y la nueva geometría todavía necesita validación visual WebGL. Los controles avanzados no implementados en WebGL se muestran desactivados.

Más detalles: `QA_V7_ETAPA3.md`.


## v7.3 — París 3D
Tres GLB locales: Torre Eiffel, ciudad/Sena/Trocadéro y jardines/Campo de Marte. Inicia `INICIAR_WINDOWS.bat` y usa los botones CIUDAD y JARDINES. Los monumentos y distancias son interpretaciones estilizadas.


## Novedades v7.4 — Etapa 5
Visita inmersiva con cámara de ascensor, cabina simplificada, mirador, visita guiada y cancelación. Véase QA_V7_ETAPA5.md.


## v7.5 — Etapa 6
WebGL local: ocaso, bruma, destellos estilizados, exposición, Cinema y modo foto. Sonido ambiental permanece deshabilitado en WebGL local. Ver `QA_V7_ETAPA6.md` para pruebas y límites.
