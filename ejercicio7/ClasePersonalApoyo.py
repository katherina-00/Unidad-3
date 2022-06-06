from ClasePersonal import personal

class personalApoyo(personal):
    __categoria = ""

    def __init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad,categoria):
        personal.__init__(self,cuil,apellido,nombre,sueldoBasico,antiguedad)
        self.__categoria = categoria

    def sueldo(self):
        sueldo=self.getBasico() + (self.getAntiguedad()/100)
        if 1 <= self.__categoria <= 10:
            sueldo += sueldo*10/100
        elif 11 <= self.__categoria <= 20:
            sueldo += sueldo*20/100
        elif 21 <= self.__categoria <= 22:
            sueldo += sueldo*30/100

        return sueldo
