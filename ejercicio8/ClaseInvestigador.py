from ClasePersonal import personal

class investigador(personal):
    __areaInvestigacion = ""
    __tipoInvestigacion = ""

    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,areaInvestigacion,tipoInvestigacion):
        personal.__init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad)
        self.__areaInvestigacion = areaInvestigacion
        self.__tipoInvestigacion = tipoInvestigacion

    def getArea(self):
        return self.__areaInvestigacion

    def sueldo(self):
        sueldo=self.getBasico() + (self.getAntiguedad()/100)

        return sueldo
