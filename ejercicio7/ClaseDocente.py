from ClasePersonal import personal

class docente(personal):
    __categoriaProgramaIncentivos = ""
    __cargo = ""
    __catedra = ""

    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,carrera,cargo,catedra):
        personal.__init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad)
        self.__categoriaProgramaIncentivos = carrera
        self.__cargo = cargo
        self.__catedra = catedra

    def sueldo(self):
        sueldo=self.getBasico() + (self.getAntiguedad()/100)
        if self.__cargo == "simple":
            sueldo += sueldo*10/100
        elif self.__cargo == "semiexclusivo":
            sueldo += sueldo*20/100
        elif self.__cargo == "exclusivo":
            sueldo += sueldo*50/100

        return sueldo
