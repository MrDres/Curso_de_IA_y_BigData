#!/usr/bin/python3

entrada = open("bluetoothLog.txt", "r", encoding= "utf8")
salida = open("salida_mapper.txt","w")
label = "Dirección:"
#Leemos cada linea del archivo
for line in entrada:
    #si la linea contiene la label indicada divide el texto por dicha label 
   if label in line:
            divide = line.split(label)
            #comprobamos si la lista divide tiene mas de un elemento significa que hubo division            
            if len(divide) > 1:
                #cojemos el segundo elemento que es la direccion mac que es lo que buscamos y se escribe en el archivo de salida
                macs = divide[1].strip() 
                print (macs, "\t", 1)
                salida.write(macs + "\t" + "1\n")
       
salida.close()
