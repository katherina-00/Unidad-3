class personal:
    __cuil = 0
    __apellido = ""
    __nombre = ""
    __sueldoBasico = 0
    __antiguedad = 0

    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldoBasico = sueldoBasico
        self.__antiguedad = antiguedad

    def getCuil(self):
        return self.__cuil

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getBasico(self):
        return self.__sueldoBasico

    def getAntiguedad(self):
        return self.__antiguedad
