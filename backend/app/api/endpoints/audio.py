from fastapi import APIRouter
from pydantic import BaseModel
from app.services.audio_service import AudioService

router = APIRouter()
audio_service = AudioService()

class TextRequest(BaseModel):
    text: str

@router.post("/hablar/")
async def hablar(data: TextRequest):
    audio_service.hablar(data.text)
    return {"message": "Audio generado y reproducido"}

@router.post("/reproducir_audio/")
async def reproducir_audio(data: TextRequest):
    audio_service.reproducir_audio(data.text)
    return {"message": "Audio generado y reproducido"}

@router.post("/desconexion_audio/")
async def desconexion_audio():
    audio_service.desconexion_audio()
    return {"message": "Desconexión de audio reproducida"}

@router.post("/guardado_exitoso/")
async def guardado_exitoso():
    audio_service.guardado_exitoso()
    return {"message": "Audio de guardado exitoso reproducido"}

@router.post("/error_audio/")
async def error_audio():
    audio_service.error()
    return {"message": "Audio de error reproducido"}

@router.get("/play_audio")
async def play_audio():
    audio_service.reproducir_audio_no_save("Texto de audio aquí")
    return {"message": "Audio reproducido"}

