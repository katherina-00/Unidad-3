from ClaseCalefactor import calefactor


class CalefactorGas(calefactor):
    __matricula = ""
    __calorias = int(0)

    def __init__(self,marca, modelo, matricula, calorias):
        calefactor.__init__(self,marca, modelo)
        self.__matricula = matricula
        self.__calorias = int(calorias)

    def __str__(self):
        return "Marca: %s, Modelo: %s, Matricula: %s, Calorias: %d" % (self.getMarca(),self.getModelo(),self.__matricula,self.__calorias)

    def consumo(self, costo, consumo):
        menor = 0
        if consumo >= self.__calorias/costo:
            menor = self.__calorias/costo
        return menor
