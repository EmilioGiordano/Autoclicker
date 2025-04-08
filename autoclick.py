import keyboard
import time
import mouse 
# Configuración
tecla_activacion = 'c'  # Tecla que activa el click rápido
tecla_salida = 'f1'    # Tecla para salir del programa
velocidad_clicks = 0.05 # Tiempo entre clicks en segundos

def enviar_click():
    # Esta función simula un click presionando y soltando el botón izquierdo
    mouse.click('left')
    time.sleep(0.01)        # Pequeña pausa
    mouse.click('left')

print(f"Script de click rápido iniciado. Mantén presionado '{tecla_activacion}' para activar.")
print(f"Presiona '{tecla_salida}' para salir del programa.")

while True:
    if keyboard.is_pressed(tecla_salida):
        print("Programa detenido.")
        break
    
    if keyboard.is_pressed(tecla_activacion):
        enviar_click()
        time.sleep(velocidad_clicks)
    else:
        time.sleep(0.01)  # Pequeña pausa para no sobrecargar la CPU