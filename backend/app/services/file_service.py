import os
import uuid
from docx import Document
import html2text
import datetime
import keyboard
class FileService:
    def html_to_docx(self, text):
        folder_path = "respuestas"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        output_path = os.path.join(folder_path, "unl-text" + str(uuid.uuid4()) + ".docx")

        doc = Document()
        texto_sin_saltos = text.replace("\n", " ")
        text_content = html2text.html2text(texto_sin_saltos)
        doc.add_paragraph(text_content)
        doc.save(output_path)
        print("Guardado en", folder_path, "como:", output_path)

        try:
            usb_path = os.path.join("/media/unl/KINGSTON", "unl-text" + str(uuid.uuid4()) + ".docx")
            doc.save(usb_path)
        except Exception as e:
            print("No se pudo guardar el archivo en un USB nombrado como Kingston")


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

 