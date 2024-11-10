
file_path = 'archivo.txt'
with open(file_path, 'r') as archivo:
    for linea in archivo:
        print(linea.strip())  

with open(file_path, 'a') as archivo:
    archivo.write("\nEste es un mensaje agregado al final del archivo.")
