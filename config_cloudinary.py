from dotenv import load_dotenv
import os
import cloudinary

# Cargar variables desde .env
load_dotenv()

# Configurar Cloudinary
cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET")
)
