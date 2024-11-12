import pygame

pygame.mixer.init()

try:
    pygame.mixer.music.load(r'C:\Users\Jordy\Documents\SERVICOM2\proyecto\backend\app\services\error.mpeg')
    print("Archivo cargado exitosamente")
    pygame.mixer.music.play()
except Exception as e:
    print(f"Error al cargar el archivo: {e}")
