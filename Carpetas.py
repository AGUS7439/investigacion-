import os


os.makedirs('nueva_carpeta', exist_ok=True)


archivos = os.listdir('.')
print("Archivos en el directorio:", archivos)
