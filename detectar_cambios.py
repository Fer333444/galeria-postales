import os
import time
import subprocess

carpeta = "galerias/cliente123"
vistas_anteriores = set(os.listdir(carpeta))

while True:
    actuales = set(os.listdir(carpeta))
    nuevas = actuales - vistas_anteriores
    if nuevas:
        print("Nuevos archivos detectados:", nuevas)
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-m", "Agregadas nuevas postales"])
        subprocess.run(["git", "push"])
        vistas_anteriores = actuales
    time.sleep(10)  # Verifica cada 10 segundos
