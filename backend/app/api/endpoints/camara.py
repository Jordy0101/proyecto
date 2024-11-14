from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
import base64
from io import BytesIO
from PIL import Image
import threading
import tkinter as tk
from app.services.camara_service import CameraService

router = APIRouter()
camera_service = None  # Definir la cámara de forma global para controlarla

# Endpoint para capturar una foto y guardarla en el servidor
@router.get("/capturar_foto")
async def capturar_foto():
    global camera_service
    if not camera_service:
        raise HTTPException(status_code=400, detail="Cámara no iniciada")
    try:
        img = camera_service.capturarFoto()
        if img:
            img_path = "captura.jpg"  # Ruta para guardar la imagen capturada
            img.save(img_path)
            return {"message": "Foto capturada", "image_path": img_path}
        return {"error": "Error al capturar la foto"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al capturar la foto: {str(e)}")

# Endpoint para procesar una imagen en la cámara
@router.post("/capturar_imagen")
async def capturar_imagen():
    global camera_service
    if not camera_service:
        raise HTTPException(status_code=400, detail="Cámara no iniciada")
    try:
        camera_service.subprocess()
        return {"message": "Imagen capturada correctamente."}
    except Exception as e:
        return {"error": str(e)}

# Endpoint para recibir y guardar una imagen en base64
@router.post("/guardar")
async def guardar_imagen(request: Request):
    try:
        body = await request.json()
        image_data = body.get("image")
        if not image_data:
            raise HTTPException(status_code=400, detail="No se recibió ninguna imagen")

        # Decodifica la imagen de base64 y la guarda en el servidor
        img_data = base64.b64decode(image_data)
        img = Image.open(BytesIO(img_data))
        img.save("captura.jpg")
        return JSONResponse(content={"message": "Imagen guardada correctamente"}, status_code=200)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al guardar la imagen: {str(e)}")

# Endpoint para cerrar la cámara y liberar los recursos
@router.post("/cerrar")
async def cerrar_camara():
    global camera_service
    if camera_service:
        camera_service.exit()
        camera_service = None
        return {"message": "Cámara cerrada y recursos liberados"}
    return {"message": "La cámara ya estaba cerrada"}

# Endpoint para abrir la cámara en una nueva ventana de Tkinter
@router.get("/abrir-camara")
async def abrir_camara():
    global camera_service
    if camera_service:
        return {"message": "La cámara ya está en ejecución"}
    
    # Iniciar la cámara en un hilo separado para no bloquear FastAPI
    threading.Thread(target=iniciar_ventana_tk, daemon=True).start()  # Usar daemon=True para que el hilo termine cuando el servidor FastAPI termine
    return {"message": "Interfaz de cámara abierta"}

def iniciar_ventana_tk():
    # Función para iniciar la ventana de Tkinter sin bloquear FastAPI
    global camera_service
    try:
        root = tk.Tk()
        camera_service = CameraService(root, "Cámara con Tkinter")
        root.mainloop()
    except Exception as e:
        print(f"Error al iniciar la ventana de Tkinter: {str(e)}")
