# camera.py
from fastapi import APIRouter,HTTPException, Request
import asyncio
from app.services.camara_service import CameraService
from PIL import Image
import base64
from io import BytesIO
from fastapi.responses import JSONResponse
import threading
router = APIRouter()
camera_service = CameraService()


@router.get("/capturar_foto")
async def capturar_foto():
    img = camera_service.capturarFoto()
    if img:
        img_path = "/path/to/save/image.jpg"
        img.save(img_path)
        return {"message": "Foto capturada", "image_path": img_path}
    return {"error": "Error al capturar la foto"}

@router.post("/capturar_imagen")
async def capturar_imagen():
    try:
        camera_service.subprocess()
        return {"message": "Imagen capturada correctamente."}
    except Exception as e:
        return {"error": str(e)}

@router.post("/cerrar")
async def cerrar():
    response = camera_service.exit()
    return response
@router.post("/guardar")
async def capturar_iniciar(request: Request):
    try:
        # Recibimos la imagen desde el frontend (base64)
        body = await request.json()
        image_data = body.get("image")
        
        if not image_data:
            raise HTTPException(status_code=400, detail="No se recibió ninguna imagen")

        # Decodificamos la imagen desde base64
        img_data = base64.b64decode(image_data)
        img = Image.open(BytesIO(img_data))

        # Guardamos la imagen en el servidor
        img.save("captura.jpg")  # Guardar como ejemplo
        return JSONResponse(content={"message": "Imagen guardada correctamente"}, status_code=200)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al guardar la imagen: {str(e)}")
# WebSocket para transmitir imágenes de la cámara
@router.post("/cerrar")
async def cerrar_camara():
    camera_service.exit()
    return {"message": "Cámara cerrada y recursos liberados"}


# Endpoint para abrir la cámara en una nueva ventana de Tkinter
@app.get("/abrir-camara")
def abrir_camara():
    # Usar un hilo para ejecutar la ventana de Tkinter sin bloquear el servidor FastAPI
    threading.Thread(target=iniciar_ventana_tk).start()
    return {"message": "Interfaz de cámara abierta"}

def iniciar_ventana_tk():
    # Función para iniciar la ventana de Tkinter
    root = tk.Tk()
    app = CameraService(root, "Cámara con Tkinter")
    root.mainloop()