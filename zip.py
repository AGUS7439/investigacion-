import zipfile

# Extraer todos los archivos de un ZIP
with zipfile.ZipFile('archivo.zip', 'r') as zip_ref:
    zip_ref.extractall('carpeta_destino')

# Crear un nuevo archivo ZIP con archivos seleccionados
with zipfile.ZipFile('nuevo_archivo.zip', 'w') as zip_write:
    zip_write.write('archivo1.txt')
    zip_write.write('archivo2.txt')
