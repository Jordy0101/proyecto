from fastapi import FastAPI
from app.api.endpoints import audio, file, button, camara
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
     CORSMiddleware,
    allow_origins=["*"],  # Permite todas las solicitudes desde cualquier origen
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos los encabezados
)
app.include_router(audio.router, prefix="/audio", tags=["audio"])
app.include_router(file.router, prefix="/file", tags=["file"])
app.include_router(file.router, prefix="/text", tags=["text"])
app.include_router(button.router, prefix="/button", tags=["Button"])
app.include_router(camara.router, prefix="/camera", tags=["camara"])
# Puedes agregar rutas adicionales aquí si lo necesitas
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de FastAPI"}