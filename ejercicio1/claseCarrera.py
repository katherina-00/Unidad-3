class carrera:
    __codigo = 0
    __nombre = ""
    __duracion = ""
    __titulo = ""
    __tipo = ""

    def __init__(self, codigo, nombre, titulo, duracion, tipo):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__titulo = titulo
        self.__duracion = duracion
        self.__tipo = tipo

    def getCodigo(self):
        return self.__codigo
    def getNombre(self):
        return self.__nombre
    def getTitulo(self):
        return self.__titulo
    def getDuracion(self):
        return self.__duracion
    def getTipo(self):
        return self.__tipo

    def __str__(self):
        cadena ="Carrera: \n"
        cadena += "Nombre: {}, Titulo: {}".format(self.__nombre, self.__titulo)
        cadena += "Duracion: {}, Tipo: {}\n".format(self.__duracion, self.__tipo)
        return cadena
