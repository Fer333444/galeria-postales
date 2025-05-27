import cloudinary
import cloudinary.uploader
import os
import sys
from dotenv import load_dotenv
from generar_postales_estilos import generar_postal  # tu función existente

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("dlcbxtcin"),
    api_key=os.getenv("453723362245378"),
    api_secret=os.getenv("Fn3h6rp_oG6lvaDRk7i6Dil1oQw")
)

# Imagen que llega por argumento
imagen = sys.argv[1]
ruta = f"galerias/cliente123/{imagen}"

# Subir a Cloudinary
respuesta = cloudinary.uploader.upload(ruta)
url = respuesta["secure_url"]
print("✅ Subido:", url)

# Generar postal
generar_postal(imagen)
