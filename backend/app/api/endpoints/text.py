from fastapi import APIRouter
from pydantic import BaseModel
from app.services.text_service import TextService

router = APIRouter()
text_service = TextService()

class TextRequest(BaseModel):
    text: str
    palabra: str = None

@router.post("/to_plain_string/")
async def to_plain_string(data: TextRequest):
    return {"cleaned_text": text_service.to_plain_string(data.text)}

@router.post("/contiene_palabra/")
async def contiene_palabra(data: TextRequest):
    if data.palabra:
        return {"contains_word": text_service.contiene_palabra(data.text, data.palabra)}
    return {"error": "Palabra no especificada"}

@router.post("/geminiunl/")
async def gemini_unll(mensaje: str):
    return text_service.gemini_unl(mensaje)

@router.post("/gemini/")
async def gemini(prompt: str):
    try:
        return text_service.gemini(prompt)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en gemini: {e}")