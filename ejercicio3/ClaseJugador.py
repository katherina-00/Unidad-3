class jugador:
    __nombre = ""
    __dni = 0
    __ciudadNatal = ""
    __pais = ""
    __fechaNacimiento = ""

    def __init__(self, nomb, dni, ciudadNatal, pais, nac):
        self.__nombre = nomb
        self.__dni = dni
        self.__ciudadNatal = ciudadNatal
        self.__pais = pais
        self.__fechaNacimiento = nac
    
    def __str__(self):
        return "%s %s %s %s %s" % (self.__nombre, self.__dni, self.__ciudadNatal, self.__pais, self.__fechaNacimiento)
    
    def getNombre(self):
        return self.__nombre
    def getDNI(self):
        return self.__dni
    def getCiudad(self):
        return self.__ciudadNatal
    def getPais(self):
        return self.__pais
    def getNacimiento(self):
        return self.__fechaNacimiento

    def getJugador(self):
        return self
