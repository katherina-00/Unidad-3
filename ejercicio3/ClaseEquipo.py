class equipo:
    __nombre = ""
    __ciudad = ""
    __contrato = None

    def __init__(self, nomb, ciudad):
        self.__nombre = nomb
        self.__ciudad = ciudad
        self.__contrato = []

    def __str__(self):
        return "%s %s" % (self.__nombre, self.__ciudad)
    
    def getNomb(self):
        return self.__nombre
    def getCiudad(self):
        return self.__ciudad
    
    def addContrato(self, jugador,contrato):
        contrato.crearContrato(jugador, self)

        self.__contrato.append(contrato)

    def mostrarContrato(self):
        for contrato in self.__contrato:
            print(contrato)

    def getEquipo(self):
        return self
