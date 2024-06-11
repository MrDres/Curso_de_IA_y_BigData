#!/usr/bin/python3
import re
from unicodedata import normalize

with open("datos/Whatsapp_filipino.txt","r", encoding="utf8") as archivo_entrada:
    texto = archivo_entrada.read()
    
    texto = texto.lower()
# NFD y eliminar diacríticos visto en internet la expresion regular   
    texto = re.sub(
    	r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
    	normalize( "NFD", texto), 0, re.I
    )
 
texto = normalize( 'NFC', texto)
#Con esto limpiamos el texto de espacios y caracteres que no son letras
textolimpio = re.sub(r'[^a-zA-Z]', '', texto)
resultado = [(letra , 1) for letra in textolimpio]
print(resultado)
def escribir_a_archivo(nombre_archivo, lista_tuplas):
    with open(nombre_archivo, 'w') as archivo:
        for clave, valor in lista_tuplas:
            archivo.write(f"{clave}: {valor}\n")

nombre_archivo = "salida_mapper_fi.txt"
escribir_a_archivo(nombre_archivo, resultado)