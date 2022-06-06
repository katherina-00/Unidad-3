
class aparatos(object):
    __marca = ""
    __modelo = ""
    __color = ""
    __paisFabricacion = ""
    __precioBase = ""

    def __init__(self, marca, modelo, color, paisFabricacion, precioBase):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__paisFabricacion = paisFabricacion
        self.__precioBase = precioBase

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getColor(self):
        return self.__color

    def getPaisFabricacion(self):
        return self.__paisFabricacion

    def getPrecioBase(self):
        return self.__precioBase
