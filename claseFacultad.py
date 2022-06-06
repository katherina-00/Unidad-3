from claseCarrera import carrera

class facultad:
    __codigo = 0
    __nombre = ""
    __direccion = ""
    __localidad = ""
    __telefono = 0
    __careras = []

    def __init__(self, codigo,nombre,direccion,localidad,telefono,carrera):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__direccion=direccion
        self.__localidad=localidad
        self.__telefono=telefono
        if carrera != None:
            self.addCarrera(carrera,1)

    def addCarrera(self,carrera,cantidad):
        for i in range (cantidad):
            self.__carreras.append(carrera)

    def __str__(self):
        s= "Codigo: {} \n Nombre{}\n Direccion{}\n Localidad{}\n Telefono{}\n Carrera{}".format(self.__codigo,self.__nombre,self.__direccion,self.__localidad,self.__telefono,self.__carreras)

