from ClaseAparatos import aparatos

class heladera(aparatos):
    __capacidadLitros = ""
    __freezer = None
    __ciclica = None

    def __init__(self,marca,modelo,color,paisFabricacion,precioBase,capacidadLitros,freezer,ciclica):
        aparatos.__init__(self,marca, modelo,color,paisFabricacion,precioBase)
        self.__capacidadLitros = capacidadLitros
        self.__freezer = freezer
        self.__ciclica = ciclica

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                        marca=self.getMarca(),
                        modelo=self.getModelo(),
                        color=self.getColor(),
                        paisFabricacion=self.getPaisFabricacion(),
                        precioBase=self.getPrecioBase(),
                        capacidadLitros=self.__capacidadLitros,
                        freezer=self.__freezer,
                        ciclica=self.__ciclica
                     )
                )
        return d

    def importeHeladera(self):
        total = self.getPrecioBase()
        freezer = self.__freezer
        ciclica = self.__ciclica
        if freezer:
                imp = total + (total * 5 / 100)
        else:
                imp = total + (total / 100)
        if ciclica:
                imp += total + (total * 10 / 100)
        return imp
