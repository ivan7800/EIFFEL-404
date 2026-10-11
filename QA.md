# QA — EIFFEL 404

## Alcance revisado

- Commit base auditado: `3037eb4e70b9ec6afaeaaf4bcf80c41df8b91429`.
- La demo pública responde en GitHub Pages.
- En la comprobación actual, el arranque WebGL no se completó y la página cayó al Canvas de compatibilidad.
- Los controles WebGL (ascensor, mirador, visita guiada, ciudad, jardines, bruma, destellos, exposición y Cinema) aparecen desactivados en dicho modo.
- La carga real de los tres GLB en GitHub Pages queda como **incidencia abierta**.

## Pruebas presentes

| Archivo | Cobertura | Límite |
|---|---|---|
| `tests/test_canvas_fallback.py` | Niveles, día/noche, reinicio, recorrido panorámico y ayuda | Inyecta HTML/CSS/JS; no es ejecución integral del sitio servido |
| `tests/test_visual_v7.py` | Canvas a 1440×900 y 390×844; errores JS y capturas | No ejecuta WebGL |
| `tests/test_injected_webgl.py` | Arranque con GLB inyectado y navegador WebGL | No verifica los recursos desplegados en Pages |
| `tests/test_stage6_controls.py` | Controles con respuestas GLB inyectadas | Usa un contexto WebGL simulado, no renderizado GPU real |
| `tests/test_offline_webgl.py` | Intento de carga local con Chromium/SwiftShader | Puede reportar `BROWSER_UNAVAILABLE`; no es un gate fiable |

Las capturas existentes son de pruebas previas y no evidencias de esta revisión.

## Ejecutar los scripts existentes

Requisitos: Python 3, Chromium y Playwright. Por ejemplo:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install playwright
python -m playwright install chromium
```

Linux/macOS:

```bash
source .venv/bin/activate
python -m pip install playwright
python -m playwright install chromium
```

Ejecuta desde la raíz del proyecto:

```bash
python tests/test_canvas_fallback.py
python tests/test_visual_v7.py
python tests/test_injected_webgl.py
python tests/test_stage6_controls.py
python tests/test_offline_webgl.py
```

Son scripts independientes; no están integrados como suite de CI y no deben interpretarse como una certificación de producción.

## Gate manual pendiente para una versión estable

1. Servir el proyecto por HTTP y probar en Chromium, Firefox o Edge actuales con WebGL habilitado.
2. Confirmar HTTP 200 para `assets/eiffel_404.glb`, `assets/paris_city.glb` y `assets/paris_parks.glb`.
3. Confirmar estado `3D WEBGL LOCAL · PARÍS 3D · VISITA INMERSIVA` y ausencia de errores de consola.
4. Probar giro, zoom, cuatro niveles, ciudad, jardines, día/noche/ocaso, ascensor, mirador, visita guiada, detener, bruma, destellos, exposición, modo foto, PNG, reinicio y pantalla completa.
5. Repetir en móvil y con navegador/GPU real.
6. Cerrar la incidencia de Pages y actualizar el README antes de etiquetar una versión estable.

## Veredicto

**Release candidata; no certificada como final.** La ruta pública observada degrada a Canvas y las pruebas WebGL existentes usan inyección o simulación.