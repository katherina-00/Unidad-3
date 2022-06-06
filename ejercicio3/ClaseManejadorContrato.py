import numpy as np
import csv
from datetime import datetime
from ClaseContrato import contrato
class ManejadorContrato:
    __cantidad = 0
    __dimension = 0

    def __init__(self, dimension):
        self.__contratos = np.empty(dimension, contrato)
        self.__cantidad = 0
        self.__dimension = dimension

    def __str__(self):
        s = ""
        for co in self.__contratos:
            s += str(co) + "\n"
        return s
    
    def agregarContrato(self,unContrato):
        if self.__cantidad == self.__dimension:
            self.__contratos.resize(self.__dimension)
        self.__contratos[self.__cantidad] = unContrato
        self.__cantidad += 1
    
    def crearContrato(self, jugador, equipo):
        fechaInicio = input("Ingrese fecha inicio de contrato (dd/mm/yyyy): ")
        fechaFin = input("Ingrese fecha fin (dd/mm/yyyy): ")
        pagoMensual = input("Ingrese pago mensual: ")
        print("\n")
        cont = contrato(fechaInicio, fechaFin, pagoMensual, jugador, equipo)
        self.agregarContrato(cont)

    def diff_month(self,d1, d2):
        return (d1.year - d2.year) * 12 + d1.month - d2.month

    def buscaJugador(self, j):
        jug = input("Ingrese DNI de jugador a buscar: ")
        print("\n")
        jugador = j.buscaJugador(jug)
        if jugador != None:
            for i, contrato in enumerate(self.__contratos):
                if contrato.getJugador() == jugador:
                    print("El jugador posee un contrato en el equipo: {} y la fecha de finalizacion del mismo es: {}".format(contrato.getEquipo(), contrato.getFechaFin()))
                else:
                    print("Error al buscar jugador")
        else:
            print("El DNI ingresado no corresponde a ningun jugador que tenga contrato")

    def buscaEquipo(self, e):
        equipo = e.buscaEquipo()
        if equipo != None:
            for i, contrato in enumerate(self.__contratos):
                if contrato.getEquipo() == equipo:

                    F_inicio = datetime.strptime(contrato.getFechaInicio(), "%d/%m/%Y")
                    F_final = datetime.strptime(contrato.getFechaFin(), "%d/%m/%Y")
                    mes = self.diff_month(F_inicio, F_final)

                    if mes == 6:
                        print("Jugadores: {} \n".format(contrato.getJugador()))
                    else:
                        print("No hay jugadores en este equipo cuyo contrato vence en 6 meses")
                else:
                    print("Equipo no encontrado")

    def buscaImportes(self, e):
        importe=0
        equipo = e.buscaEquipo()
        if equipo != None:
            for i, contrato in enumerate(self.__contratos):
                if contrato.getEquipo() == equipo:
                    importe += int(contrato.getPagoMensual())
        print("El importe total de los contratos que posee con los jugadores es: {} ".format(importe))

    def generaArchivo(self,j,e):
        with open('contratos.csv', 'w', newline='') as csvfile:
            fieldnames = ['DNI jugador', 'Nombre del equipo', 'Fecha Inicio','Fecha Fin','Pago mes']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            for i, contrato in enumerate(self.__contratos):
                writer.writeheader()
                writer.writerow({'DNI jugador': j.buscaDNI(i), 'Nombre del equipo': e.buscaNombre(i), 'Fecha Inicio': contrato.getFechaInicio(), 'Fecha Fin': contrato.getFechaFin(), 'Pago mes': contrato.getPagoMensual()})
