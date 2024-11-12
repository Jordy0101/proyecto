from .audio_service import AudioService
# backend/app/services/button_service.py
from .text_service import TextService  # Asegúrate de importar correctamente

class ButtonService:

    def __init__(self):
        self.is_blocked = False
        self.contador = 0
        self.audio_service = AudioService()  # Suponiendo que AudioService tiene el método
        self.text_service = TextService()

    def on_key_press(self, event):
        if self.is_blocked:
            return  # No hace nada si el teclado está bloqueado
        # Lógica de manejo de eventos de teclas aquí...

    def finish_function(self):
        self.is_blocked = False
        print("Teclado desbloqueado")
    
    def incrementar_contador(self):
        self.contador += 1
        print(f'El contador es ahora: {self.contador}')

    def decrementar_contador(self):
        self.contador -= 1
        print(f'El contador es ahora: {self.contador}')

    def resetear_contador(self):
        self.contador = 0
        print('El contador ha sido reiniciado')

    def button_actionn(self):
        print("Botón * presionado")
        self.start_function()
        print("Tecla '*' presionada")
        is_blocked = True       
        self.incrementar_contador()
        self.info()
        self.executing = False

    def button_actio(self):
        print("Botón / presionado") 
        self.start_function()
        print("Tecla '/' presionada")
        is_blocked = True      
        self.decrementar_contador()
        self.info()
        self.executing = False 

    def button1_action(self):
        print("Botón 1 presionado")
        self.text_service.gemini("Identifica que hay en la imagen, hay texto?, tablas? graficos? en español: solo responde algo como: el contenido del documento es texto, el contenido del documento es gráficos, o el contenido del documento es tablas, o el contenido del documento es texto y tablas o texto y gráficos, o si hay texto tablas y gráficos, o no hay, nada, dependiendo del contenido del documento, no des una explicación del documento.")

    def button2_action(self):
        print("Botón 2 presionado") 
        self.text_service.gemini("extrae el texto que encuentres")
           
    def button3_action(self):
        print("Botón 3 presionado")
        self.text_service.gemini("Narra en español todo el contenido de la tabla de una forma ordenada, coherente y estructurada de forma que se pueda entender TODO el contenido, primero narra las columnas y luego narra los valores de cada fila relacionando con cada columna")

    def button4_action(self):
        print("Botón 4 presionado") 
        self.text_service.gemini("Describe todo el contenido del gráfico en español, y leelo si fuera necesario, de una forma ordenada, coherente y estructurada de forma que se pueda entender TODO el contenido")
        
    def button5_action(self):
        print("Botón 5 presionado")     
        self.text_service.gemini("Extrae el texto de los párrafos y Describe todo el contenido, si hay tablas o gráfico, describe cada fila o sección explicando de forma ordenada, coherente y estructurada de forma que se pueda entender TODO el contenido")

    def button7_action(self):
        print("Botón 7 presionado") 
            
    def button8_action(self):
        print("Botón 8 presionado")

    def button9_action(self):
        print("Botón 9 presionado") 

    def button0_action(self):
        print("Botón 0 presionado")

    def buttonE_action(self):
        print("Botón Enter presionado") 

    def info(self):
        mensajes = {
            1: "Bienvenido a Eye Reader",
            2: "Para iniciar, coloca un documento en la bandeja",
            3: "Con la tecla 1 identifica el tipo de contenido",
            4: "La tecla 2 ejecuta la lectura de texto",
            5: "La tecla 3 para describir una tabla",
            6: "La tecla 4 para describir un gráfico",
            7: "La tecla 5 para leer texto con tablas y/o gráficos",
            8: "Puedes guardar el texto o audio generado; Despues de cada ejecución presiona 7 para guardar el texto, 8 para guardar el audio o 9 para guardar ambos"
        }

        # Reproducir el mensaje si el contador está en el rango de 1 a 8
        if self.contador in mensajes:
            self.audio_service.reproducir_audio_no_save(mensajes[self.contador])
            
            if self.contador == 8:
                self.resetear_contador()
            
            self.finish_function()  # Llamada única después de reproducir el audio

        else:
            self.resetear_contador()  # Resetear el contador si no está en el rango 1-8
            
    def start_function(self):
        self.is_blocked = True
        print("Teclado bloqueado")
