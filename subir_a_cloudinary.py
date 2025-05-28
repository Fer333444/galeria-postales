import cloudinary.uploader
import config_cloudinary  # carga automática desde el archivo .env
import os
import sys
from generar_postales_estilos import generar_postal  # tu función existente

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
