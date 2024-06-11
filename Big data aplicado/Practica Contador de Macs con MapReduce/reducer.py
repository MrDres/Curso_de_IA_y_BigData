#!/usr/bin/env python
import sys

contador = 0
mac_anterior = None
entrada = open ("entrada_reducer.txt", "r", encoding= "utf8")

for linea in entrada:
    linea = linea.strip()
    lista = linea.split("\t")
    mac = lista[0]

    if mac_anterior == None:
        mac_anterior = mac
    
    if mac == mac_anterior:
        contador += 1
    
    else:
        print(mac_anterior, "\t", contador)
        mac_anterior = mac
        contador = 1
    
print(mac_anterior, "\t", contador)
