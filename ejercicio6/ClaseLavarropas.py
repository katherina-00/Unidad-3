from ClaseAparatos import aparatos

class lavarropas(aparatos):
    __capacidadLavado = ""
    __velocidadCentrifugado = 0
    __cantidadProgramas = 0
    __tipoCarga = ""

    def __init__(self,marca,modelo,color,paisFabricacion,precioBase,capacidadLavado,velocidadCentrifugado,cantidadProgramas,tipoCarga):
        aparatos.__init__(self,marca, modelo,color,paisFabricacion,precioBase)
        self.__capacidadLavado = capacidadLavado
        self.__velocidadCentrifugado = velocidadCentrifugado
        self.__cantidadProgramas = cantidadProgramas
        self.__tipoCarga = tipoCarga

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                        marca=self.getMarca(),
                        modelo=self.getModelo(),
                        color=self.getColor(),
                        paisFabricacion=self.getPaisFabricacion(),
                        precioBase=self.getPrecioBase(),
                        capacidadLavado=self.__capacidadLavado,
                        velocidadCentrifugado=self.__velocidadCentrifugado,
                        cantidadProgramas=self.__cantidadProgramas,
                        tipoCarga=self.__tipoCarga
                     )
                )
        return d

    def importeLavarropas(self):
        imp=0
        total = self.getPrecioBase()
        capacidad = self.__capacidadLavado
        if capacidad <= 5:
                imp = total + (total / 100)
        elif capacidad > 5:
                imp = total + (total * 3 / 100)
        return imp
