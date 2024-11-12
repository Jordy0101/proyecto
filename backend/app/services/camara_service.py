# camera_service.py
import cv2
from PIL import Image
import base64
from io import BytesIO
from fastapi import FastAPI
from fastapi.responses import JSONResponse
class CameraService:
    
    def capturarFoto(self):
        ret, frame = self.vid.read()
        if ret:
            retval, buffer = cv2.imencode('.jpg', frame)
            img_bytes = BytesIO(buffer.tobytes())
            img_pil = Image.open(img_bytes) 

            return img_pil
        
        else:
            print("Error al capturar la foto.")
            return None
        
    def iniciar_camara(self):
        if not self.vid.isOpened():
            self.vid.open(0)  # Asegúrate de que la cá
    
    def __init__(self):
        # Inicializa la cámara
        self.vid = cv2.VideoCapture(0)  # Abre la cámara
        if not self.vid.isOpened():
            raise Exception("No se pudo abrir la cámara.")
        
    def subprocess(self):
        # Ejecutar el comando del sistema para capturar imagen
        subprocess.run(
            ["nvgstcapture-1.0", "--automate", "--capture-auto", "--image-res", "3"],
            shell=False, capture_output=True, text=True, check=True
        )
        # Puedes agregar lógica para verificar la salida y manejarla si es necesario

    def exit(self):
        # Cerrar la cámara y liberar los recursos
        if self.vid.isOpened():
            self.vid.release()  # Libera la cámara
            print("Cámara cerrada correctamente.")
        cv2.destroyAllWindows()  # Cierra cualquier ventana de OpenCV abierta
        return {"message": "Cámara cerrada correctamente."}   
    
 
    def convertir_a_base64(self, img):
        # Convierte la imagen PIL a base64
        buffer = BytesIO()
        img.save(buffer, format="JPEG")
        return base64.b64encode(buffer.getvalue()).decode("utf-8")

