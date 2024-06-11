#!/usr/bin/python3
import array
label = "Dirección:"

with open("bluetoothLog.txt", "r", encoding= "utf8") as archivo_entrada:
    for line in archivo_entrada:
        if label in line:
            divide = line.split(label)            
            if len(divide) > 1:
                mac = divide[1].strip()
                