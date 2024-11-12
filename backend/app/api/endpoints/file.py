from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.file_service import FileService
from gtts import gTTS  # Importar gTTS para la conversión de texto a voz

router = APIRouter()
file_service = FileService()

class HTMLRequest(BaseModel):
    text: str

@router.post("/html_to_docx/")
async def html_to_docx(data: HTMLRequest):
    file_service.html_to_docx(data.text)
    return {"message": "Archivo .docx generado y guardado"}

@router.post("/preguntar_guardar/")
async def guardado_exitoso():
    return file_service.preguntar_guardar()


@router.post("/preguntar_guardar/")
async def preguntar_guardar(texto: str, mensaje: str):
    try:
        # Crear el objeto tts usando gTTS
        tts = gTTS(mensaje, lang="es")
        return file_service.preguntar_guardar(texto, tts)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en preguntar_guardar: {e}")