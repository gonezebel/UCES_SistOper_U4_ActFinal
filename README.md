# Studio Design 3D - Sala de Crisis IT

Web interactiva en Python/Flask para la Actividad Integradora Final de Sistemas Operativos.

La propuesta simula el rol de gerente IT de un estudio de arquitectura y animacion, explicando con escenarios practicos:

- Gestion de procesos: Round Robin y semaforos.
- Gestion de memoria: paginacion, MMU, swapping y LRU.
- Entrada/salida: spooling y DMA.
- Archivos y seguridad: NTFS, ACL y auditoria.
- Redes: DHCP, DNS y Active Directory.

## Ejecutar localmente

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Abrir `http://localhost:5000`.

## Deploy en Render

El repositorio incluye `render.yaml`.

1. Subir el proyecto a GitHub.
2. Crear un nuevo Blueprint en Render y seleccionar este repositorio.
3. Render ejecutara `pip install -r requirements.txt` y levantara la app con `gunicorn app:app`.

Variable opcional:

- `VIDEO_EMBED_URL`: URL de embed de YouTube, por ejemplo `https://www.youtube-nocookie.com/embed/ID_DEL_VIDEO`.

## Nota de privacidad

`.gitignore` excluye las carpetas `00_Bibliografía/`, `01_Consigna/` y `.venv/` para no publicar PDFs ni entorno local.
