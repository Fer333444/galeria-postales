import os
import time
from PIL import Image, ImageOps, ImageEnhance
import qrcode

# Configuración
FOTOS_ORIG = "C:/FotosOriginales"
FOTOS_ESTILO = "C:/FotosEstilizadas"
FOLDER_QR = "C:/QRs"

# Estilos simulados localmente
def aplicar_estilo(imagen_path, estilo):
    imagen = Image.open(imagen_path)
    nombre = os.path.basename(imagen_path)
    salida = os.path.join(FOTOS_ESTILO, f"{estilo}_{nombre}")

    if estilo == "boceto":
        imagen = imagen.convert("L")  # escala de grises
    elif estilo == "realce_color":
        enhancer = ImageEnhance.Color(imagen)
        imagen = enhancer.enhance(2.0)
    elif estilo == "invertido":
        imagen = ImageOps.invert(imagen.convert("RGB"))
    elif estilo == "sepia":
        sepia = ImageOps.colorize(imagen.convert("L"), "#704214", "#C0A080")
        imagen = sepia

    imagen.save(salida)
    return salida

def generar_qr(imagen_path):
    filename = os.path.basename(imagen_path)
    ruta_local = f"file:///{imagen_path.replace(os.sep, '/')}"
    qr = qrcode.make(ruta_local)
    qr_path = os.path.join(FOLDER_QR, f"qr_{filename}.png")
    qr.save(qr_path)
    return qr_path

def procesar_nueva_foto(foto_path):
    estilos = ["boceto", "realce_color", "invertido", "sepia"]
    for estilo in estilos:
        estilizada = aplicar_estilo(foto_path, estilo)
        qr = generar_qr(estilizada)
        print(f"[✔] Generado: {qr}")

def detectar_y_procesar():
    ya_procesadas = set()
    while True:
        fotos = [f for f in os.listdir(FOTOS_ORIG) if f.lower().endswith(('.jpg', '.png'))]
        for f in fotos:
            ruta = os.path.join(FOTOS_ORIG, f)
            if ruta not in ya_procesadas:
                print(f"[📸] Nueva foto detectada: {f}")
                procesar_nueva_foto(ruta)
                ya_procesadas.add(ruta)
        time.sleep(3)

if __name__ == "__main__":
    detectar_y_procesar()
