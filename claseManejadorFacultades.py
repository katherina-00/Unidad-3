import csv
from claseFacultad import facultad
class ManejaFacultades:
    def __init__(self):
        self.__Facultades=[]
    
    def __str__(self):
        s = ""
        for facultad in self.__Facultades:
            s += str(facultad) + '\n'
        return s

    def agregarFacultad(self,unaFacultad):
        self.__Facultades.append(unaFacultad)

    def CrearFacultad(self):
        with open("Facultades.csv","r") as file:
                reader=csv.reader(file,delimiter=",")
                for fila in reader:
                    if len(fila) == 6:
                        cod = int(fila[0])
                        nombre = fila[1]
                        direccion = fila[2]
                        localidad = int(fila[3])
                        telefono = int(fila[4])
                        unaFacultad = facultad(cod,nombre,direccion,localidad,telefono)
                        self.agregarFacultad(unaFacultad)
                    else:
                        pass

