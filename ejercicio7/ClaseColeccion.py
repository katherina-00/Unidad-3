from zope.interface import implementer
from ClaseInterface import IColeccion
from ClasePersonal import personal
from ClaseDocente import docente
from ClaseInvestigador import investigador
from ClasePersonalApoyo import personalApoyo
from ClaseDocenteInvestigador import docenteInvestigador


class Nodo:
    __personal = None
    __siguiente = None

    def __init__(self, personal):
        self.__personal = personal
        self.__siguiente = None

    def setSiguiente(self, siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__personal


@implementer(IColeccion)
class coleccion:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
        return dato

    def agregarElemento(self, personal):

        actual = self.__comienzo
        anterior = None
        pos = 0
        tamanio = self.__sizeof__()
        while pos < tamanio:
            anterior = actual
            actual = actual.getSiguiente()
            pos += 1
        nuevo = Nodo(personal)
        if anterior is None:
            nuevo.setSiguiente(actual)
            self.__comienzo = nuevo
        else:
            anterior.setSiguiente(nuevo)
        self.__tope += 1

    def toJSON(self):
        d = dict(__class__= self.__class__.__name__, __aparatos=[personal.toJSON() for personal in self.__comienzo])
        return d

    def insertarElemento(self,pos,agente):
        if pos > self.__sizeof__() - 1:
            raise IndexError("Posicion fuera del rango")
        actual = self.__comienzo
        anterior = None
        aux = 0
        if pos is 0:
            self.agregarAparato(agente)
        else:
            nuevo = Nodo(agente)
            while aux < pos:
                aux += 1
                anterior = actual
                actual = actual.getSiguiente()
            anterior.setSiguiente(nuevo)
            nuevo.setSiguiente(actual)

    def mostrarElemento(self,pos):
        dato = None
        if pos > self.__sizeof__():
            raise Exception ("Index out of bounds")

        actual = self.__comienzo
        if pos is None:
            dato = actual.getDato()
            self.__comienzo = actual.getSiguiente()
        else:
            aux = 0
            anterior = None
            while aux < pos:
                anterior = actual
                actual = actual.getSiguiente()
                aux += 1
                dato = actual.getDato()
            anterior.setSiguiente(actual.getSiguiente())

        if isinstance(dato,docente):
            print("El elemento es un docente")
        elif isinstance(dato,investigador):
            print("El elemento es un investigador")
        elif isinstance(dato,personalApoyo):
            print("El elemento es un personal de apoyo")
        elif isinstance(dato,docenteInvestigador):
            print("El elemento es un docente investigador")


    def generaListadoDocenteInvestigador(self):
        pass

    def segunArea(self,area):
        contD=0
        contA=0
        actual = self.__comienzo
        while actual is not None:
            if isinstance(actual.getDato(),docenteInvestigador):
                contD += 1
                if actual.getArea()==area:
                    contA += 1
                self.__comienzo = actual.getSiguiente()
                self.__tope -= 1
            else:
                anterior = actual
                actual = actual.getSiguiente()
                while actual !=None:
                    if isinstance(actual.getDato(),docenteInvestigador):
                        contD += 1
                        if actual.getArea()==area:
                            contA += 1
                    else:
                        anterior = actual
                        actual = actual.getSiguiente()

    def listadoOrdenadoApellido(self):
        pass

    def segunCategoria(self,categoria):
        actual = self.__comienzo
        while actual is not None:
            if isinstance(actual.getDato(), docenteInvestigador) and actual.getDato().getCategoria() == categoria:
                print(actual.getDato())
                print(actual.getDato().importeExtra())
                self.__comienzo = actual.getSiguiente()
                self.__tope -= 1
            else:
                anterior = actual
                actual = actual.getSiguiente()
                while actual !=None:
                    if isinstance(actual.getDato(), docenteInvestigador) and actual.getDato().getCategoria() == categoria:
                        print(actual.getDato())
                        print(actual.getDato().importeExtra())
                    else:
                        anterior = actual
                        actual = actual.getSiguiente()
