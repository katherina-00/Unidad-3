from ClaseDocente import docente
from ClaseInvestigador import investigador
class docenteInvestigador(docente,investigador):
    __categoriaProgramaIncentivos = ""
    __importeExtra = 0

    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,carrera,cargo,catedra,areaInvestigacion,tipoInvestigacion,catProgInc,importeExtra):
        docente.__init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,carrera,cargo,catedra)
        investigador.__init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,areaInvestigacion,tipoInvestigacion)
        self.__categoriaProgramaIncentivos = catProgInc
        self.__importeExtra = importeExtra


    def getCategoria(self):
        return self.__categoriaProgramaIncentivos

    def sueldo(self):
        sueldo=self.getBasico() + (self.getAntiguedad()/100)
        if self.__cargo == "simple":
            sueldo += sueldo*10/100
        elif self.__cargo == "semiexclusivo":
            sueldo += sueldo*20/100
        elif self.__cargo == "exclusivo":
            sueldo += sueldo*50/100

        sueldo += self.__importeExtra

        return sueldo
