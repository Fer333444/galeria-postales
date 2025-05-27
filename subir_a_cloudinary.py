import cloudinary
import cloudinary.uploader
import os
import sys
from dotenv import load_dotenv
from generar_postales_estilos import generar_postal  # tu función existente

load_dotenv()

# 👇 Verifica que las variables del entorno se cargan correctamente
print("✅ CLOUD_NAME:", os.getenv("CLOUD_NAME"))
print("✅ API_KEY:", os.getenv("API_KEY"))
print("✅ API_SECRET:", os.getenv("API_SECRET"))

# Configurar Cloudinary
cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET")
)

# Imagen que llega por argumento
imagen = sys.argv[1]
ruta = f"galerias/cliente123/{imagen}"

# Subir a Cloudinary
try:
    respuesta = cloudinary.uploader.upload(ruta)
    url = respuesta["secure_url"]
    print("✅ Subido:", url)
except Exception as e:
    print("❌ Error subiendo a Cloudinary:", e)

# Generar postal
generar_postal(imagen)
