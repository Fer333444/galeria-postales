import os
from urllib.parse import unquote

carpeta = "galerias/cliente123"
nombre_archivo_url = "postcard_final_de%20WhatsApp%202025-05-26%20a%20las%2017.01.32_8f544786.jpg"

# Decodificar el nombre
nombre_archivo = unquote(nombre_archivo_url)

# Ruta completa
ruta = os.path.join(carpeta, nombre_archivo)

print("🔎 Verificando:", ruta)

# Verificar existencia
if os.path.exists(ruta):
    print("✅ El archivo existe y es accesible.")
else:
    print("❌ El archivo NO existe. Revisa si el nombre está mal codificado o fue eliminado.")
