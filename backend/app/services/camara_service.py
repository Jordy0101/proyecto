import cv2
from PIL import Image, ImageTk
import tkinter as tk
from io import BytesIO
import base64

class CameraService:
    
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.window.attributes('-fullscreen', True)

        # Inicializa la cámara por defecto
        self.vid = cv2.VideoCapture(0)
        if not self.vid.isOpened():
            raise Exception("No se pudo abrir la cámara.")

        # Configurar el fondo de pantalla
        self.image_label = tk.Label(window)
        self.image_label.pack(fill=tk.BOTH, expand=True)
        self.original_image = Image.open("background.jpeg")
        self.update_image()  # Ajustar la imagen de fondo según el tamaño inicial

        # Crear el Label para la transmisión de la cámara
        self.canvas = tk.Label(window)
        self.canvas.place(x=0, y=60)

        # Label con texto de bienvenida
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        self.text_label = tk.Label(
            self.image_label,
            text="Bienvenido a E-Reader",
            fg="white",
            bg="black",
            font=("Arial", 9),
            wraplength=screen_width / 2.64,
            justify="left"
        )
        self.text_label.place(x=screen_width * 0.6, y=screen_height * 0.23)

        # Añadir botones personalizados
        self.add_buttons()

        # Llama a la función de actualización de la cámara
        self.update_camera_feed()

        # Asignar eventos de teclado
        self.window.bind('<Escape>', lambda e: self.exit())
        self.window.bind('<KeyPress>', self.on_key_press)
        self.window.bind("<Configure>", self.on_resize)  # Evento de cambio de tamaño
        self.window.mainloop()

    def update_camera_feed(self):
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

    def update_image(self):
        # Redimensiona y muestra la imagen de fondo
        bg_image = self.original_image.resize(
            (self.window.winfo_width(), self.window.winfo_height()), Image.ANTIALIAS
        )
        self.background_image = ImageTk.PhotoImage(bg_image)
        self.image_label.configure(image=self.background_image)

    def on_resize(self, event):
        # Actualiza la imagen de fondo al cambiar el tamaño de la ventana
        self.update_image()

    def add_buttons(self):
        # Añadir botones de ejemplo
        btn = tk.Button(self.image_label, text="Ejemplo Botón", command=self.some_command)
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
    app = CameraService(root, "Cámara con Tkinter")
