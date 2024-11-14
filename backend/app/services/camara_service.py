import cv2
from PIL import Image, ImageTk
import tkinter as tk
import threading

class CameraService:
    
    def __init__(self, window, window_title, width=800, height=600):
        self.window = window
        self.window.title(window_title)
        
        # Establece el tamaño de la ventana
        self.window.geometry(f"{width}x{height}")  # Ancho x Alto

        # Inicializa la cámara por defecto
        self.vid = cv2.VideoCapture(0)
        if not self.vid.isOpened():
            raise Exception("No se pudo abrir la cámara.")

        # Crear el Label para la transmisión de la cámara
        self.canvas = tk.Label(window)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Añadir botones personalizados
        self.add_buttons()

        # Asignar eventos de teclado
        self.window.bind('<Escape>', lambda e: self.exit())
        self.window.bind('<KeyPress>', self.on_key_press)
        self.window.bind("<Configure>", self.on_resize)  # Evento de cambio de tamaño

        # Iniciar la cámara en un hilo separado para no bloquear la UI
        threading.Thread(target=self.start_camera, daemon=True).start()

        self.window.mainloop()

    def start_camera(self):
        """Este método se encarga de iniciar la interfaz gráfica de la cámara"""
        self.update_camera_feed()

    def update_camera_feed(self):
        """Captura los frames de la cámara y los actualiza en la interfaz"""
        ret, frame = self.vid.read()
        if ret:
            # Convertir el frame a RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img_pil = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img_pil)

            # Actualizar la transmisión de la cámara en el canvas
            self.canvas.imgtk = imgtk
            self.canvas.configure(image=imgtk)

        # Programa otra actualización en 10 ms
        self.window.after(10, self.update_camera_feed)

    def on_resize(self, event):
        """Ajusta el tamaño del canvas al cambiar el tamaño de la ventana"""
        self.canvas.config(width=self.window.winfo_width(), height=self.window.winfo_height())

    def add_buttons(self):
        # Añadir botones de ejemplo
        btn = tk.Button(self.canvas, text="Ejemplo Botón", command=self.some_command)
        btn.place(x=50, y=50)  # Posición de ejemplo, puedes ajustarla

    def some_command(self):
        print("Botón presionado")

    def on_key_press(self, event):
        print(f"Tecla presionada: {event.keysym}")

    def exit(self):
        if self.vid.isOpened():
            self.vid.release()  # Libera la cámara
            print("Cámara cerrada correctamente.")
        self.window.destroy()

# Ejemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    app = CameraService(root, "Cámara con Tkinter", width=800, height=600)  # Tamaño ajustado a 800x600
