import os
import time
from subprocess import call

CARPETA = "galerias/cliente123"
ARCHIVO_CONTROL = "archivos_vistos.txt"

if os.path.exists(ARCHIVO_CONTROL):
    with open(ARCHIVO_CONTROL, "r") as f:
        vistos = set(f.read().splitlines())
else:
    vistos = set()

print("🔄 Esperando nuevas imágenes...")

while True:
    archivos = set(os.listdir(CARPETA))
    nuevos = [a for a in archivos if a.lower().endswith(".jpg") and a not in vistos and not a.startswith("postcard_final")]

    for nuevo in nuevos:
        print(f"🖼️ Nueva imagen detectada: {nuevo}")
        call(["python", "subir_a_cloudinary.py", nuevo])
        vistos.add(nuevo)
        with open(ARCHIVO_CONTROL, "a") as f:
            f.write(nuevo + "\n")

    time.sleep(5)
