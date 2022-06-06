import csv
import numpy as np
from ClaseEquipo import equipo

class ManejadorEquipos:
    __cantidad = 0
    __dimension = None

    def __init__(self, dimension):
        self.__equipos = np.empty(dimension, dtype=equipo)
        self.__cantidad = 0
        self.__dimension = dimension
    
    def agregarEquipo(self, unEquipo):
        if self.__cantidad == self.__dimension:
            self.__equipos.resize(self.__dimension)
        self.__equipos[self.__cantidad] = unEquipo
        self.__cantidad += 1
    
    def __str__(self):
        s = ""
        for eq in self.__equipos:
            s += str(eq) + "\n"
        return s

    def crearEquipo(self):
        b = True
        with open("Equipos.csv", "r") as file:
            reader = csv.reader(file, delimiter=",")
            for fila in reader:
                if b:
                    self.__dimension = int(fila[0])
                    b = not b
                else:
                    nomb = fila[0]
                    ciudad = fila[1]
                    unEquipo = equipo(nomb, ciudad)
                    self.agregarEquipo(unEquipo)

    def contrato(self, j, c):
        eq=input("Ingrese nombre del equipo con el cual firmara contrato este jugador: ")
        for i, equipo in enumerate(self.__equipos):
            if eq == equipo.getNomb():
                equipo.addContrato(j, c)

    def muestraContratos(self):
        for i, equipo in enumerate(self.__equipos):
            print("Contratos del equipo {}: ".format(equipo.getNomb()))
            equipo.mostrarContrato()

    def buscaEquipo(self):
        eq = input("Ingrese nombre del equipo: ")
        print("\n")
        b = None
        for i, equipo in enumerate(self.__equipos):
            if eq == equipo.getNomb():
                b = equipo.getEquipo()
        return b

    def buscaNombre(self,indice):
        for i, equipo in enumerate(self.__equipos):
            if i == indice:
                return equipo.getNomb()
