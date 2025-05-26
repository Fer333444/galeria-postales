import os
import time

FOLDER = "galerias/cliente123"
INTERVAL = 10  # segundos

def get_files():
    return set(os.listdir(FOLDER))

def push_changes():
    os.system("git add .")
    os.system("git commit -m \"Auto update\"")
    os.system("git push")

print("⏳ Observando la carpeta para detectar nuevos archivos...")
prev = get_files()

while True:
    time.sleep(INTERVAL)
    curr = get_files()
    if curr != prev:
        print("🟢 Cambios detectados. Subiendo...")
        push_changes()
        prev = curr
    else:
        print("🕓 Sin cambios...")
