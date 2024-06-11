import re
from collections import Counter

def limpiar_texto(texto):
    #Limpia el texto eliminando cualquier carácter que no sea una letra.    
    texto_limpio = re.sub(r'[^a-zA-Z]', '', texto)
    return texto_limpio

def contar_letras(texto):
    #Cuenta el número de apariciones de cada letra en el texto.    
    texto_limpio = limpiar_texto(texto)
    conteo = Counter(texto_limpio)
    return conteo

def leer_archivo(nombre_archivo):
    #Lee el contenido de un archivo y lo devuelve como una cadena de texto.
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()
    return contenido

def escribir_archivo(nombre_archivo, conteo):
    #Escribe el resultado de contar letras en un archivo de texto.    
    with open(nombre_archivo, 'w') as archivo:
        for letra, cantidad in sorted(conteo.items()):
            archivo.write(f"{letra}: {cantidad}\n")

def main():
    # Leer el contenido del archivo de entrada
    texto = leer_archivo('entrada_reducer_fi.txt')
    
    # Contar las letras en el texto
    conteo = contar_letras(texto)
    
    # Escribir el resultado en el archivo de salida
    escribir_archivo('salida_reducer_fi.txt', conteo)

# Ejecutar la función principal
if __name__ == "__main__":
    main()