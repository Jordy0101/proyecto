# backend/app/core/services/app_service.py
import genai
import tkinter as tk
from PIL import Image, ImageTk

class AppService:
    def __init__(self, window, window_title):
        GOOGLE_API_KEY = 'AIzaSyCI5hk_LHr8V49BjaI4pm6BxpZBwJplxII'
        genai.configure(api_key=GOOGLE_API_KEY)
        
        self.window = window
        self.window.title(window_title)
        self.window.attributes('-fullscreen', True)

        self.image_label = tk.Label(window)
        self.image_label.pack(fill=tk.BOTH, expand=True)
        self.original_image = Image.open("background.jpeg")
        self.update_image()
        self.window.bind("<Configure>", self.on_resize)

        inicialx = self.window.winfo_screenwidth() * 0.6
        inicialy = self.window.winfo_screenheight() * 0.23
        anchotexto = self.window.winfo_screenwidth() / 2.64
        self.text_label = tk.Label(self.image_label, text="Bienvenido a E-Reader", fg="white", bg="black", font=("Arial", 9), wraplength=anchotexto, justify="left")
        self.text_label.place(x=inicialx, y=inicialy)

        self.add_buttons()
        self.executing = False

    def add_buttons(self):
        inicial=self.window.winfo_screenwidth()-180
        # Botón *
        self.buttonn = tk.Button(self.image_label, text="*", command=self.button_actionn, bg='black', fg='white')
        self.buttonn.place(x=inicial-330, y=115) 
        
        # Botón /
        self.butto = tk.Button(self.image_label, text="/", command=self.button_actio, bg='black', fg='white')
        self.butto.place(x=inicial-300, y=115)  
        # Botón 1
        self.button1 = tk.Button(self.image_label, text="1", command=self.button1_action, bg='black', fg='white')
        self.button1.place(x=inicial-270, y=115)
        
        # Botón 2
        self.button2 = tk.Button(self.image_label, text="2", command=self.button2_action, bg='black', fg='white')
        self.button2.place(x=inicial-240, y=115) 
        # Botón 3
        self.button3 = tk.Button(self.image_label, text="3", command=self.button3_action, bg='black', fg='white')
        self.button3.place(x=inicial-210, y=115)
        
        # Botón 4
        self.button4 = tk.Button(self.image_label, text="4", command=self.button4_action, bg='black', fg='white')
        self.button4.place(x=inicial-180, y=115) 

        # Botón 5
        self.button5 = tk.Button(self.image_label, text="5", command=self.button5_action, bg='black', fg='white')
        self.button5.place(x=inicial-150, y=115) 
        
        # Botón 7
        self.button7 = tk.Button(self.image_label, text="7", command=self.button7_action, bg='white', fg='black')
        self.button7.place(x=inicial-120, y=115)
        # Botón 8
        self.button8 = tk.Button(self.image_label, text="8", command=self.button8_action, bg='white', fg='black')
        self.button8.place(x=inicial-90, y=115) 
        
        # Botón 9
        self.button9 = tk.Button(self.image_label, text="9", command=self.button9_action, bg='white', fg='black')
        self.button9.place(x=inicial-60, y=115)
        # Botón 0
        self.button0 = tk.Button(self.image_label, text="0", command=self.button0_action, bg='gray', fg='white')
        self.button0.place(x=inicial, y=115)
        
        # Botón Enter
        self.buttonE = tk.Button(self.image_label, text="Enter", command=self.buttonE_action, bg='gray', fg='white')
        self.buttonE.place(x=inicial+30, y=115)  
 
   