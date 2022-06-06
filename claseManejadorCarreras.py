import csv
from claseCarrera import carrera
class ManejaCarrera:
    def __init__(self):
        self.__Carreras=[]

    def __str__(self):
        s = ""
        for carrera in self.__Carreras:
            s += str(carrera) + '\n'
        return s

    def agregarCarrera(self,unaCarrera):
        self.__Carreras.append(unaCarrera)

    def CrearCarrera(self,fila):
        if len(fila) == 5:
            cod = int(fila[0])
            nombre = fila[1]
            fehcaInicio = fila[2]
            duracion = int(fila[3])
            titulo = int(fila[4])
            unaFacultad = facultad(cod,nombre,fehcaInicio,duracion,titulo)
            self.agregarFacultad(unaFacultad)
