import numpy as np
import csv
from ClaseFlores import flores
class ManejadorFlores:
    __cantidad: 0
    __dimension: 0

    def __init__(self, dimension):
        self.__ListaFlores = np.empty(dimension, dtype=flores)
        self.__dimension = dimension
        self.__cantidad = 0
        #self.__ListaFlores=[]

    def __str__(self):
        s = ""
        for flores in self.__ListaFlores:
            s += str(flores) + '\n'
        return s

    def crearFlor(self,unaFlor):
        if self.__cantidad == self.__dimension:
            self.__ListaFlores.resize(self.__dimension)
        self.__ListaFlores[self.__cantidad] = unaFlor
        self.__cantidad += 1

    def leerFlores(self):
        with open("flores.csv","r") as file:
            reader=csv.reader(file,delimiter=";")
            for fila in reader:
                numero = fila[0]
                nombre = fila[1]
                color = fila[2]
                descripcion = fila[3]
                unaFlor = flores(numero,nombre,color,descripcion)
                self.crearFlor(unaFlor)
                #reader = np.loadtxt(file, delimiter=";")

    
