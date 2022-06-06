class contrato:
    __fechaInicio = ""
    __fechaFin = ""
    __pagoMensual= 0
    __jugador=None
    __equipo=None

    def __init__(self,inicio,fin,pagoMensual,UnJugador,UnEquipo):
        self.__fechaInicio=inicio
        self.__fechaFin=fin
        self.__pagoMensual=pagoMensual
        self.__jugador=UnJugador
        self.__equipo=UnEquipo

    def __str__(self):
        return "%s %s %s %s %s" % (self.__fechaInicio, self.__fechaFin,self.__pagoMensual,self.__jugador,self.__equipo)
    
    def getFechaInicio(self):
        return self.__fechaInicio

    def getFechaFin(self):
        return self.__fechaFin

    def getPagoMensual(self):
        return self.__pagoMensual

    def getJugador(self):
        return self.__jugador

    def getEquipo(self):
        return self.__equipo

