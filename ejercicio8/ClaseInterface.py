from zope.interface import Interface
from zope.interface import implementer

class IColeccion(Interface):
    def instertarElemento(objeto,pos):
        print("lol")

    def agregarElemento(elemento):
        pass

    def mostrarElemento(elemento,pos):
        pass
