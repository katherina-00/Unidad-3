from ClaseCalefactor import calefactor


class calefactorElectrico(calefactor):
    __potenciaMax = int(0)

    def __init__(self, marca, modelo, potencia):
        calefactor.__init__(self, marca, modelo)
        self.__potenciaMax = int(potencia)
    
    def __str__(self):
        return "Marca: %s, Modelo: %s, Potencia: %d" % (self.getMarca(), self.getModelo(), self.__potenciaMax)

    def consumo(self, costo, consumo):
        menor = 0
        if consumo >= self.__potenciaMax/costo:
            menor = self.__potenciaMax/costo
        return menor
