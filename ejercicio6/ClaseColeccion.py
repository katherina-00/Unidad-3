from ClaseLavarropas import lavarropas
from ClaseHeladeras import heladera
from ClaseTelevisores import televisores
class Nodo:
    __aparatos = None
    __siguiente = None

    def __init__(self, aparatos):
        self.__aparatos = aparatos
        self.__siguiente = None

    def setSiguiente(self,siguiente):
        self.__siguiente = siguiente

    def getSiguiente(self):
        return self.__siguiente

    def getDato(self):
        return self.__aparatos


class coleccion:
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0

    def __init__(self):
        self.__comienzo=None
        self.__actual=None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
        return dato

    def toJSON(self):
        d = dict(__class__= self.__class__.__name__, __aparatos=[aparato.toJSON() for aparato in self.__comienzo])
        return d

    def agregarAparato(self, aparato):
        nodo = Nodo(aparato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def insertarAparato(self,pos,aparato):
        if pos > self.__sizeof__() - 1:
            print("Posicion fuera del rango")
        actual = self.__comienzo
        anterior = None
        aux = 0
        if pos is 0:
            self.agregarAparato(aparato)
        else:
            nuevo = Nodo(aparato)
            while aux < pos:
                aux += 1
                anterior = actual
                actual = actual.getSiguiente()
            anterior.setSiguiente(nuevo)
            nuevo.setSiguiente(actual)

    def importeTelevision(self):
        imp=0
        total = self.__actual.getDatos().getPrecioBase()
        definicion = self.__actual.getDatos().getTipoDefinicion()
        internet = self.__actual.getDatos().getInternet()
        if definicion == 'SD':
                imp = total + (total / 100)
        elif definicion == 'HD':
                imp = total + (total * 2 / 100)
        elif definicion == 'FULL HD':
                imp = total + (total * 3 / 100)
        if internet == True:
                imp += total + (total * 10 / 100)
        return imp

    def importeLavarropas(self):
        imp=0
        total = self.__actual.getDatos().getPrecioBase()
        capacidad = self.__actual.getDatos().getCapacidadLavado()
        if  capacidad <= 5:
                imp = total + (total / 100)
        elif capacidad > 5:
                imp = total + (total * 3 / 100)
        return imp

    def importeHeladera(self):
        total = self.__actual.getDatos().getPrecioBase()
        freezer = self.__actual.getDatos.getFreezer()
        ciclica = self.__actual.getDatos().getCiclica()
        if  freezer:
                imp = total + (total * 5 / 100)
        else:
                imp = total + (total / 100)
        if ciclica:
                imp += total + (total * 10 / 100)
        return imp

    def agregarAparato_a_Coleccion(self):
        tipo=input("Ingrese tipo de aparato a agregar: (Televisor, Lavarropa, Heladera) ")
        if tipo == "Televisor":
            pass
        elif tipo == "Lavarropa":
            pass
        elif tipo == "Heladera":
            pass
        # Agregar un aparato a la colección (solicitar el tipo de aparato, y luego los datos que correspondan).

    def mostrarObjeto(self,pos):
        dato = None
        if pos > self.__sizeof__():
            print("Index out of bounds")

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

        if isinstance(dato,heladera):
            print("El elemento es una heladera")
        elif isinstance(dato,televisores):
            print("El elemento es un televisor")
        elif isinstance(dato,lavarropas):
            print("El elemento es un lavarropas")

    def MuestraMarca(self):
        actual = self.__comienzo
        while actual is not None:
            if actual.getDato().getMarca() == "Philips":
                print(actual.getDato())
                self.__comienzo = actual.getSiguiente()
                self.__tope -= 1
            else:
                anterior = actual
                actual = actual.getSiguiente()
                while actual !=None:
                    if actual.getDato().getMarca() == "Philips":
                        print(actual.getDato().getMarca())
                    else:
                        anterior = actual
                        actual = actual.getSiguiente()

    def LavarropaCargaSuperior(self):

        actual = self.__comienzo
        while actual is not None:
            if isinstance(actual.getDato(), lavarropas) and actual.getDato().getCarga == "Superior":
                print(actual.getDato().getMarca())
                self.__comienzo = actual.getSiguiente()
                self.__tope -= 1
            else:
                anterior = actual
                actual = actual.getSiguiente()
                while actual !=None:
                    if isinstance(actual.getDato(), lavarropas) and actual.getDato().getCarga == "Superior":
                        print(actual.getDato().getMarca())
                    else:
                        anterior = actual
                        actual = actual.getSiguiente()

    def mostrarDatosAparatos(self):
        aux = self.__comienzo
        while aux!=None:
            print(aux.getDato().getMarca())
            print(aux.getDato().getPaisFabricacion())
            if isinstance(aux,heladera):
                print(aux.importeHeladera())

            elif isinstance(aux,lavarropas):
                print(aux.importeLavarropas())

            elif isinstance(aux,televisores):
                print(aux.importeTelevision())
            aux=aux.getSiguiente()
