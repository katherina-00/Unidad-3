class carrera:
    __codigo=0
    __nombre=""
    __fechaInicio=""
    __duracion=0
    __titulo=""

def __init__(self,codigo,nombre,fechaInicio,duracion,titulo):
    self.__codigo=codigo
    self.__nombre=nombre
    self.__fechaInicio=fechaInicio
    self.__duracion=duracion
    self.__titulo=titulo

def __str__(self):
        return "%d %s %s %d %s" % (self.__codigo, self.__nombre, self.__fechaInicio, self.__duracion, self.__titulo)

