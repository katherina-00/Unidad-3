
class facultad:
    __codigo = 0
    __nombre = ""
    __direccion = ""
    __localidad = ""
    __telefono = ""
    __carera = []

    def __init__(self, codigo,nombre,direccion,localidad,telefono,carreras):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__direccion=direccion
        self.__localidad=localidad
        self.__telefono=telefono

        for i in range(len(carreras)):
            self.__carera.append(carreras)

    def __str__(self):

        return "Codigo: {} \n Nombre{}\n Direccion{}\n Localidad{}\n Telefono{}\n Carrera{}".format(self.__codigo,self.__nombre,self.__direccion,self.__localidad,self.__telefono, self.__carera)
    
    def getNombre(self):
        return self.__nombre
    
    def getCodigo(self):
        return self.__codigo
    
    def getDatosCarrera(self,id):
        for i in range (len(self.__carera)):
            return self.__carera
    
    def getLocalidad(self):
        return self.__localidad
