import time
import pygame
import keyboard
from gtts import gTTS
from io import BytesIO
from langdetect import detect

class AudioService:
    def hablar(self, texto):
        print(texto)
        with BytesIO() as f:
            tts = gTTS(text=texto, lang='es', slow=False)
            tts.write_to_fp(f)
            f.seek(0)
            
            # Reproducir el audio usando pygame mixer
            pygame.mixer.init()
            pygame.mixer.music.load(f)
            pygame.mixer.music.play()
            
            # Esperar hasta que termine de reproducirse el audio
            while pygame.mixer.music.get_busy():
                if keyboard.is_pressed('Enter'):
                    pygame.mixer.music.stop()
                    time.sleep(0.1)
                    break
                continue

#https://gtts.readthedocs.io/en/latest/cli.html
    def reproducir_audio(self,texto):
        try:
            with BytesIO() as f:
                texto_sin_saltos = texto.replace("\n", " ") 
                #tts = gTTS(text=texto_sin_saltos, lang='pt')
                lang =detect(texto_sin_saltos)
                tts = gTTS(text=texto_sin_saltos, lang=lang)
                tts.write_to_fp(f)

                f.seek(0) 
                pygame.mixer.init()
                pygame.mixer.music.load(f)
                pygame.mixer.music.play()
                
                while pygame.mixer.music.get_busy():
                    if keyboard.is_pressed('0'):
                        pygame.mixer.music.stop()
                        time.sleep(0.1)
                        self.desconexion_audio()
                        break
                    
                    if keyboard.is_pressed('+'):
                        pos=pygame.mixer.music.get_pos()
                        pygame.mixer.music.set_pos(pos + 1) #adelantar un segundo 
                        
                    if keyboard.is_pressed('-'):
                        pos=pygame.mixer.music.get_pos()
                        pygame.mixer.music.set_pos(pos - 1) #adelantar un segundo 
                        
                    # Detectar si se ha pulsado la tecla "Enter"
                    pausado = False
                    if pausado == False:

                        #print("Esperando el . para pause")
                        if keyboard.is_pressed('Enter'):
                            pausado = True
                            pygame.mixer.music.pause()
                            pygame.mixer.music.pause()
                            #time.sleep(0.1)
                            print("pause")
                        elif keyboard.is_pressed('0'):
                            pygame.mixer.music.stop()
                            time.sleep(0.1) 
                            break 
                        while pausado == True:
                                print("Esperando el . para play")
                                if keyboard.is_pressed('Enter'):
                                    pausado==False 
                                    pygame.mixer.music.unpause()
                                    #time.sleep(0.1)
                                    print("Play") 
                                    break

                                elif keyboard.is_pressed('0'):
                                    pygame.mixer.music.stop()
                                    break
                    continue    
                self.preguntar_guardar(texto,tts) 
        except Exception as e:
            print("reproducir_audio(); GTTS ERROR - - ERROR - - ERROR   GTTS")
            self.error()
            print('{type(e).__name__}: '+ str(e))     


    def guardado_exitoso(self):
        # Inicializar pygame
        pygame.init()
        try:
            # Iniciar la reproducción del audio
            pygame.mixer.music.load("guardado_exitoso.mpeg")
            pygame.mixer.music.play()

            # Esperar hasta que el audio termine de reproducirse
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        except pygame.error as e:
            print("Error al reproducir el audio:", e)
            self.error()
        finally:
            # Detener pygame
            pygame.quit() 

    def desconexion_audio(self):
        # Inicializar pygame
        pygame.init()

        try:
            # Iniciar la reproducción del audio
            pygame.mixer.music.load("desconexion.mpeg")
            pygame.mixer.music.play()
            # Esperar hasta que el audio termine de reproducirse
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        except pygame.error as e:
            print("Error al reproducir el audio:", e)
            self.error()
        finally:
            # Detener pygame
            pygame.quit()

    def error(self):
        pygame.init()
        try:
            pygame.mixer.music.load("error.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
        except pygame.error as e:
            print("Error al reproducir el audio:", e)
        finally:
            pygame.quit() 

    def reproducir_audio_no_save(self,texto):
        try:
            with BytesIO() as f:
                texto_sin_saltos = texto.replace("\n", " ")  
                lang =detect(texto_sin_saltos)
                tts = gTTS(text=texto_sin_saltos, lang=lang)
                tts.write_to_fp(f)

                f.seek(0) 
                pygame.mixer.init()
                pygame.mixer.music.load(f)
                pygame.mixer.music.play()
                
                while pygame.mixer.music.get_busy():
                    if keyboard.is_pressed('0'):
                        pygame.mixer.music.stop()
                        time.sleep(0.1)
                        self.desconexion_audio()
                        break
                    
                    if keyboard.is_pressed('+'):

                        pos=pygame.mixer.music.get_pos()
                        pygame.mixer.music.set_pos(pos + 1) #adelantar un segundo 
                        
                    if keyboard.is_pressed('-'):
                        pos=pygame.mixer.music.get_pos()
                        pygame.mixer.music.set_pos(pos - 1) #adelantar un segundo 
                        
                    # Detectar si se ha pulsado la tecla "Enter"
                    pausado = False
                    if pausado == False:

                        #print("Esperando el . para pause")
                        if keyboard.is_pressed('Enter'):
                            pausado = True
                            pygame.mixer.music.pause()
                            #time.sleep(0.1)
                            print("pause")
                        elif keyboard.is_pressed('0'):
                            pygame.mixer.music.stop()
                            time.sleep(0.1) 
                            break 
                        while pausado == True:

                                print("Esperando el . para play")
                                if keyboard.is_pressed('Enter'):
                                    pausado==False 
                                    pygame.mixer.music.unpause()
                                    #time.sleep(0.1)
                                    print("Play") 
                                    break

                                elif keyboard.is_pressed('0'):
                                    pygame.mixer.music.stop()
                                    break
                    continue     
        except Exception as e:
            print("reproducir_audio(); GTTS ERROR - - ERROR - - ERROR   GTTS")
            self.error()
            print('{type(e).__name__}: '+ str(e))     


#https://gtts.readthedocs.io/en/latest/cli.html
    def reproducir_audio_nosound(self,texto):
        try:
            with BytesIO() as f:
                texto_sin_saltos = texto.replace("\n", " ") 
                lang =detect(texto_sin_saltos)
                tts = gTTS(text=texto_sin_saltos, lang=lang)
                tts.write_to_fp(f)

                f.seek(0) 
                pygame.mixer.init()
                pygame.mixer.music.load(f)
                pygame.mixer.music.play()
                
                while pygame.mixer.music.get_busy():
                    if keyboard.is_pressed('0'):
                        pygame.mixer.music.stop()
                        time.sleep(0.1) 
                        break
                    continue    

        except Exception as e:
            print("reproducir_audio(); GTTS ERROR - - ERROR - - ERROR   GTTS")
            self.error()
            print('{type(e).__name__}: '+ str(e))     

    def preguntar_guardar(self,texto,tts):
        try:
            self.reproducir_audio_nosound("Guardar texto tecla 7, audio 8, o ambos 9")
            tecla = keyboard.read_key()  
            if tecla=="7":
                self.html_to_docx(texto)    
                self.guardado_exitoso()
            if tecla=="8":
                tts = tts
                # Obtener la fecha y hora actual
                now = datetime.datetime.now()
                name = "respuestas/unl-audio-"+str(uuid.uuid4()) + ".mp3"

                # Carpeta donde se guardarán los audios 
                folder_path = "respuestas"
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)   
                tts.save(name)  
                
                try:
                    # USB donde se guardarán los audios   
                    nombre_audio_usb="/media/unl/KINGSTON/unl-audio-"+str(uuid.uuid4())+".mp3"
                    tts.save(nombre_audio_usb)
                    print("Guardado en KINGSTON")
                except Exception as e:              
                    try:
                        # USB donde se guardarán los audios   
                        nombre_audio_usb="/media/unl/kingston/unl-audio-"+str(uuid.uuid4())+".mp3"
                        tts.save(nombre_audio_usb)
                        print("Guardado en kingston")
                    except Exception as e:
                        print("No se guardó en kingston o KINGSTON")
                self.guardado_exitoso()
            if tecla=="9":
                self.html_to_docx(texto) 

                tts = tts
                # Obtener la fecha y hora actual
                now = datetime.datetime.now()

                # Carpeta donde se guardarán los audios 
                folder_path = "respuestas"
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)  
                nombre_audio = "respuestas/unl-audio-"+str(uuid.uuid4()) + ".mp3"
                tts.save(nombre_audio)
                try:
                    # USB donde se guardarán los audios   
                    nombre_audio_usb="/media/unl/KINGSTON/unl-audio-"+str(uuid.uuid4())+".mp3"
                    tts.save(nombre_audio_usb)
                    print("Guardado en KINGSTON")
                except Exception as e:              
                    try:
                        # USB donde se guardarán los audios   
                        nombre_audio_usb="/media/unl/kingston/unl-audio-"+str(uuid.uuid4())+".mp3"
                        tts.save(nombre_audio_usb)
                        print("Guardado en kingston")
                    except Exception as e:

                        print("No se guardó en kingston o KINGSTON")

                self.guardado_exitoso()

            elif not tecla=="0":
                exit 
        
        except Exception as e:
            print("Error en la guardada del archivo")
            self.error()
            print('{type(e).__name__}: '+ str(e))     

 

