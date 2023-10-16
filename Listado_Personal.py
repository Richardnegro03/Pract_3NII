#Listado_Personal
#Listado en Json

import json


with open(r"C:\Users\RICARDO RODRIGUEZ\Documents\Curso Programacion\PYTHON AVANZADO\Clase 3\List_Pers.json ","r") as f:
    data=json.load(f)
    
    print(data)

    
#Listado en csv

import csv


with open(r"C:\Users\RICARDO RODRIGUEZ\Documents\Curso Programacion\PYTHON AVANZADO\Clase 3\List_Pers.csv") as file:

    csv_reader=csv.reader(file,delimiter= ",")

    for row in csv_reader:
        print(row)
    file.close()
#Escribimos datos en el archivo csv

from csv import writer

#data a agregar

Pers_incorp=["Vellido","Jose","None","Serv Aux","Salta"]


with open("output-writer.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(Pers_incorp)
print(Pers_incorp)            

f.close()            

