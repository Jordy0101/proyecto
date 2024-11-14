import cv2
from PIL import Image, ImageTk
import tkinter as tk
import threading
from io import BytesIO
class CameraService:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Inicializa la cámara
        self.vid = cv2.VideoCapture(0)  # Abre la cámara por defecto
        if not self.vid.isOpened():
            raise Exception("No se pudo abrir la cámara.")
        
        # Crear un canvas para mostrar el video
        self.canvas = tk.Label(window)
        self.canvas.pack()  # Se coloca la cámara en la ventana

        # Añadir botones de control
        self.add_buttons()

        # Asignar eventos de teclado
        self.window.bind('<Escape>', lambda e: self.exit())
        self.window.bind('<KeyPress>', self.on_key_press)

        # Empezar el hilo para la cámara
        self.executing = False
        threading.Thread(target=self.start_camera, daemon=True).start()

    def start_camera(self):
        """Inicia el flujo de la cámara y actualiza la interfaz con el video."""
        while True:
            ret, frame = self.vid.read()
            if ret:
                # Convertir la imagen a RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img_pil = Image.fromarray(frame)
                imgtk = ImageTk.PhotoImage(image=img_pil)
                
                # Actualizar la imagen en el canvas
                self.canvas.imgtk = imgtk
                self.canvas.configure(image=imgtk)
                
            self.window.after(10, self.start_camera)  # Llama la función cada 10ms para actualizar

    def add_buttons(self):
        # Botones de ejemplo
        self.button1 = tk.Button(self.window, text="Ejemplo Botón", command=self.button1_action, bg='black', fg='white')
        self.button1.pack()  # Los botones pueden añadirse de la forma que gustes

    def button1_action(self):
        print("Botón 1 presionado")

    def on_key_press(self, event):
        print(f"Tecla presionada: {event.keysym}")

    def exit(self):
        if self.vid.isOpened():
            self.vid.release()  # Cierra la cámara
            print("Cámara cerrada correctamente.")
        self.window.destroy()
        
    def capturarFoto(self):
        ret, frame = self.vid.read()
        if ret:
            retval, buffer = cv2.imencode('.jpg', frame)
            img_bytes = BytesIO(buffer.tobytes())
            img_pil = Image.open(img_bytes) 
            return img_pil
        else:
            print("Error al capturar la foto.")
