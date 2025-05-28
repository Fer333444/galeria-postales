import cloudinary
import cloudinary.api
import os
from dotenv import load_dotenv

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET")
)

def buscar_en_cloudinary(nombre_imagen):
    nombre_sin_extension = nombre_imagen.replace(".jpg", "")
    resultado = cloudinary.api.resources(type="upload", prefix="", max_results=100)
    for recurso in resultado.get("resources", []):
        if recurso["public_id"].endswith(nombre_sin_extension):
            return recurso["secure_url"]
    return None

# Ejemplo de uso
nombre = "postcard_final_Imagen de WhatsApp 2025-05-26 a las 17.01.32_8f544786.jpg"
print(buscar_en_cloudinary(nombre))
