import re
import pygame
import os
import subprocess
import google.generativeai as genai  #GEMINI-1 
from PIL import Image
import glob
import datetime
from app.services.audio_service import AudioService

class TextService:
    
    def gemini(self, prompt):
            self.start_function()  
            prompt=prompt
            if self.contiene_palabra(prompt, "Identifica"):   
                print("Ejecutar sin guardar- (Identificación del contenido del documento)")
                try:  
                    print("Ingresnado a gemini_UNl")
                    res = self.gemini_unl(prompt)
                    print("Saliendo a gemini_UNl")  
                    #REPRODUCIR 
                    print("Ingresando a audio no save")
                    self.audio_service.reproducir_audio_no_save(res)
                    print("Ingresando a audio no save")
                    self.audio_service.desconexion_audio()
                    self.executing = False
                    self.finish_function()  

                except Exception as e:
                    print("Hubo un error en la ultima funcion!")
                    self.error()
                    self.executing = False
                    self.finish_function()  
                    print('{type(e).__name__}: '+str(e))    
            else: 
                print("Ejecutar y guardar - (Lectura del documento)") 
                try:  
                    res = self.gemini_unl(prompt) 
                    #REPRODUCIR 
                    self.audio_service.reproducir_audio(res)  
                    self.audio_service.desconexion_audio()
                    self.executing = False
                    self.finish_function()  

                except Exception as e:
                    print("Hubo un error en la ultima funcion!")
                    self.error()
                    self.executing = False
                    self.finish_function()  
                    print('{type(e).__name__}:'+str(e))   

    def to_plain_string(self, text):
        # Eliminar caracteres especiales excepto letras, números y tildes
        cleaned_text = re.sub(r'[^\w\sáéíóúÁÉÍÓÚ.,;:?!¡¿%]', '', text)
        return cleaned_text

    def contiene_palabra(self, cadena, palabra):
        # Verificar si la cadena no es None antes de intentar la comparación
        if cadena is not None:
            cadena = cadena.lower()  # Convertir la cadena a minúsculas
            palabra = palabra.lower()  # Convertir la palabra a minúsculas
            return palabra in cadena
        else:
            return False
        
    def finish_function(self):
        self.is_blocked = False
        print("Teclado desbloqueado")
        def gemini_unl(self, mensaje):
                print("ingresando a tomar foto")
                foto, path =self.tomarFoto() 
                print(path)
                #Eliminar Foto del repositorio 
                os.remove(path)  
                print(" mensaje ",mensaje)  
                print(" foto ",foto)    
                model = genai.GenerativeModel('gemini-1.5-flash')  
                # Seguridad https://ai.google.dev/docs/safety_setting_gemini?hl=es-419

                safety_settings = {
                    "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
                    "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE",
                    "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE",
                    "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE"} 
                try:
                    response = model.generate_content([mensaje, foto], safety_settings=safety_settings)
                    #time.sleep(1)   
                    response.resolve() 
                    self.text_label.config(text=response)
                    print(response)
                    if response.candidates[0].content.parts: 
                        try: 
                            respuesta= response.candidates[0].content.parts[0].text   
                            respuesta= self.to_plain_string(respuesta) 
                            #Devolviendo respuesta
                            print(respuesta) 
                            self.text_label.config(text=respuesta)
                            return(respuesta)  
                        except Exception as e:
                            print("Entró al Primer CATCH, ERROR - - ERROR - - ERROR")
                            print('f{type(e).__name__}: ',{e})     
                            try:  # Si solo hay una respuesta: 
                                print("!!!!!!!!!!!!!!!")
                                a=response.text    
                                respuestab=self.to_plain_string(a)
                                #Devolviendo respuesta
                                self.text_label.config(text=respuestab)
                                return(respuestab)  

                            except Exception as e:
                                print("Entró al segundo CATCH, ERROR - - ERROR - - ERROR")
                                self.hablar("No se pudo generar una respuesta")
                                self.text_label.config(text="No se pudo generar una respuesta")
                                print('{type(e).__name__}: '+{e})     

                    else: # Si solo hay una respuesta:
                        try:  
                            print("Parece que solo hay una respuesta. :)")
                            print("!!!!!!!!!!!!!!!")
                            a=response.text   
                            print("response.text")
                            respuesta=self.to_plain_string(respuesta)  
                            #Devolviendo respuesta
                            self.text_label.config(text=respuesta)
                            return(respuesta)  

                        except Exception as e:
                            print("Entró al segundo CATCH, del Else")
                            print('{type(e).__name__}: '+{e})     
                            try:  # Si solo hay una respuesta:
                                print("Parece que solo hay una respuesta. :)")  
                                respuesta= response.candidates[0].content.parts[0].text 
                                #Devolviendo respuesta
                                return(respuesta)  

                            except Exception as e:
                                print("ERROR - - ERROR")
                                self.error()
                                print('f{type(e).__name__}: ',+str(e))     
                    
                except Exception as e:
                    print("No se pudo generar una respuesta")
                    self.error() 
                    print('f{type(e).__name__}: ',{e})    
         
    def start_function(self):
        self.is_blocked = True
        print("Teclado bloqueado")
    
    def error(self):
        pygame.init()
        try:
         #     pygame.mixer.music.load("3")
          #    pygame.mixer.music.play()
          #  while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        except pygame.error as e:
            print("Error al reproducir el audio:", e)
        finally:
            pygame.quit() 
     
    def tomarFoto(self):
        
        self.subprocess()
        # Busca todos los archivos JPG en el directorio
        archivos_jpg = glob.glob(os.path.join(".", "*.jpg"))

        # Ordena los archivos por fecha de creación
        archivos_jpg.sort(key=os.path.getmtime)
        
        # Obtiene el último archivo creado
        ultimo_archivo_jpg = archivos_jpg[-1]
        
        # Abre el último archivo JPG
        imagen = Image.open(ultimo_archivo_jpg)  

	#Colocar la imagen en el fondo 
        #overlay_photo = ImageTk.PhotoImage(imagen) 
        #self.text_label.config(image=overlay_photo)
        #self.text_label = tk.Label(self.image_label, image=overlay_photo)
        #self.text_label.place(x=50, y=50)  # Ajusta la posición según sea necesario
        #os.remove(ultimo_archivo_jpg)
         
        return (imagen,ultimo_archivo_jpg) 
    
    def subprocess(self): 
        #subprocess.run(["nvgstcapture-1.0", "--automate", "--capture-auto", "--image-res", "3"], shell=False, capture_output=True, text=True, check=True)
            subprocess.run(["nvgstcapture-1.0", "--automate", "--capture-auto", "--image-res", "3"], shell=False, capture_output=True, text=True, check=True)


########