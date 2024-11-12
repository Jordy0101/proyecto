# backend/app/api/endpoints/button.py
from fastapi import APIRouter
from app.services.button_service import ButtonService
from pydantic import BaseModel

router = APIRouter()
button_service = ButtonService()

# Modelo de datos para el evento de la tecla
class KeyPressRequest(BaseModel):
    event_key: str

@router.post("/button_star/")
async def button_star():
    button_service.button_actionn()
    return {"message": "Botón * presionado"}

@router.post("/button_slash/")
async def button_slash():
    button_service.button_actio()
    return {"message": "Botón / presionado"}

# Endpoint para manejar el evento de la tecla
@router.post("/handle_key_press")
async def handle_key_press(request: KeyPressRequest):  # Aquí usamos el modelo KeyPressRequest
    event_key = request.event_key  # Accedemos a event_key del modelo
    button_service.on_key_press(event_key)
    return {"message": f"Evento de tecla {event_key} procesado"}


# Otros botones (1 a 5) como ejemplo
@router.post("/button1/")
async def button1():
    button_service.button1_action()
    return {"message": "Botón 1 presionado"}

@router.post("/button2/")
async def button2():
    button_service.button2_action()
    return {"message": "Botón 2 presionado"}

@router.post("/button3/")
async def button3():
    button_service.button3_action()
    return {"message": "Botón 3 presionado"}

@router.post("/button4/")
async def button4():
    button_service.button4_action()
    return {"message": "Botón 4 presionado"}

@router.post("/button5/")
async def button5():
    button_service.button5_action()
    return {"message": "Botón 5 presionado"}

# Endpoint para procesar el botón de Enter
@router.post("/buttonE/")
async def buttonE():
    button_service.buttonE_action()
    return {"message": "Botón Enter presionado"}