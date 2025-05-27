import time
import subprocess
import os

FOLDER = "galerias/cliente123"
vistas = set(os.listdir(FOLDER))

while True:
    actuales = set(os.listdir(FOLDER))
    nuevas = actuales - vistas

    for archivo in nuevas:
        if archivo.lower().endswith((".jpg", ".jpeg", ".png")):
            print(f"🆕 Nueva imagen detectada: {archivo}")

            # 👉 Subir a Cloudinary y generar postal
            subprocess.call(["python", "subir_a_cloudinary.py", archivo])

            # 👉 Push a GitHub
            subprocess.call(["python", "auto_push.py"])

    vistas = actuales
    time.sleep(10)  # Espera 10 segundos antes de volver a revisar
