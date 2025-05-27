import os
import time
import subprocess
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
from generar_postales_estilos import generar_postal

# Configuración inicial
carpeta = "galerias/cliente123"
archivos_vistos = set()
INTERVALO = 3  # segundos

# Cargar variables de entorno desde .env
load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET")
)

def subir_a_cloudinary(imagen):
    ruta = f"{carpeta}/{imagen}"
    try:
        respuesta = cloudinary.uploader.upload(ruta)
        url = respuesta["secure_url"]
        print("✅ Subido:", url)
    except Exception as e:
        print("❌ Error subiendo a Cloudinary:", e)

def generar_y_subir(imagen):
    try:
        generar_postal(imagen)
        print(f"✅ Postal generada de: {imagen}")
        subir_a_cloudinary(f"postcard_final_{imagen}")
    except Exception as e:
        print(f"❌ Error generando postal de {imagen}:", e)

def hacer_push():
    try:
        subprocess.call(["git", "add", "."])
        subprocess.call(["git", "commit", "-m", "🖼️ Auto update"])
        subprocess.call(["git", "push"])
        print("🚀 Push realizado correctamente")
    except Exception as e:
        print("❌ Error haciendo push:", e)

# Cargar archivos ya existentes
if os.path.exists("archivos_vistos.txt"):
    with open("archivos_vistos.txt", "r") as f:
        archivos_vistos = set(f.read().splitlines())

print("🔄 Esperando nuevas imágenes...")

# Monitor en bucle
while True:
    nuevos = []
    for archivo in os.listdir(carpeta):
        if archivo.lower().endswith((".jpg", ".jpeg", ".png")) and archivo not in archivos_vistos:
            print(f"🖼️ Nueva imagen detectada: {archivo}")
            nuevos.append(archivo)
            archivos_vistos.add(archivo)
            generar_y_subir(archivo)

    # Guardar archivo de vistos
    with open("archivos_vistos.txt", "w") as f:
        f.write("\n".join(archivos_vistos))

    if nuevos:
        hacer_push()

    time.sleep(INTERVALO)
