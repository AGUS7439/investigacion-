# Leer y copiar un archivo de imagen en modo binario
with open('imagen_original.jpg', 'rb') as img_original:
    contenido = img_original.read()

with open('imagen_copia.jpg', 'wb') as img_copia:
    img_copia.write(contenido)
