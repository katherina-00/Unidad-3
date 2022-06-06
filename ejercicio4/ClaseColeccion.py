import numpy as np
import csv
from ClaseCalefactorElectrico import calefactorElectrico
from ClaseCalefactorGas import CalefactorGas
from ClaseCalefactor import calefactor

class coleccion:
    __dimension = 0
    __cantidad = 0
    __coleccion = None

    def __init__(self, dimension):
        self.__coleccion = np.empty(dimension, dtype=calefactor)
        self.__dimension = dimension
        self.__cantidad = 0 #puede ser remplazado con el nombre self__actual
    
    def agregarColeccion(self, unaColeccion):
        self.__coleccion[self.__cantidad] = unaColeccion
        self.__cantidad += 1

    def CrearColeccion(self):
        with open("calefactor-electrico.csv", "r") as file:
            reader = csv.reader(file, delimiter=";")
            for fila in reader:
                marca = fila[0]
                modelo = fila[1]
                potencia = int(fila[2])
                unaColeccion = calefactorElectrico(marca, modelo, potencia)
                self.agregarColeccion(unaColeccion)

        with open("calefactor-a-gas.csv", "r") as file:
            reader = csv.reader(file, delimiter=";")
            for fila in reader:
                marca = fila[0]
                modelo = fila[1]
                matricula = fila[2]
                calorias = int(fila[3])
                unaColeccion = CalefactorGas(marca, modelo, matricula, calorias)
                self.agregarColeccion(unaColeccion)

    def menorConsumo(self,costo,consumo,c):
        menor=9999
        modelo=None
        marca=None
        calefactorMenor=self.__coleccion
        for i in range(self.__cantidad):
            if isinstance(self.__coleccion[i], calefactorElectrico) and c == 1:
                calefactor = self.__coleccion[i]
                aux = calefactor.consumo(costo, consumo)

                if aux < menor:
                    calefactorMenor = self.__coleccion[i]
                    menor = aux

            elif isinstance(self.__coleccion, CalefactorGas) and c == 2:
                    calefactor=self.__coleccion[i]
                    aux = calefactor.consumo(costo, consumo)
                    if aux < menor:
                        modelo = calefactor.getModelo()
                        marca = calefactor.getMarca()
                        calefactorMenor = self.__coleccion[i]
                        menor = aux

        print(str(calefactorMenor)+', Menor consumo: {} \n'.format(menor))

    def MenorCalefactores(self, costo, consumo):
        menor = 9999
        calefactorMenor = self.__coleccion
        for i in range(self.__cantidad):
            calefactor = self.__coleccion[i]
            aux = calefactor.consumo(costo, consumo)
            if aux < menor:
                calefactorMenor = self.__coleccion[i]
                menor = aux

        if isinstance(calefactorMenor, CalefactorGas):
            print("El calefactor de menor consumo es de tipo: Calefacor Gas  y sus datos son: {} \n".format(calefactorMenor))
        else:
            print("El calefactor de menor consumo es de tipo: Calefacor Electrico  y sus datos son: {} \n".format(calefactorMenor))

