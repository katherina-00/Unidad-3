from ClaseAparatos import aparatos

class televisores(aparatos):
    __tipoPantalla = ""
    __pulgadas = ""
    __tipoDefinicion = ""
    __conexionInternet = None

    def __init__(self,marca,modelo,color,paisFabricacion,precioBase,tipoPantalla,pulgadas,tipoDefinicion,conexionInternet):
        aparatos.__init__(self,marca, modelo,color,paisFabricacion,precioBase)
        self.__tipoPantalla = tipoPantalla
        self.__pulgadas = pulgadas
        self.__tipoDefinicion = tipoDefinicion
        self.__conexionInternet = conexionInternet


    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                        marca=self.getMarca(),
                        modelo=self.getModelo(),
                        color=self.getColor(),
                        paisFabricacion=self.getPaisFabricacion(),
                        precioBase=self.getPrecioBase(),
                        tipoPantalla=self.__tipoPantalla,
                        pulgadas=self.__pulgadas,
                        tipoDefinicion=self.__tipoDefinicion,
                        conexionInternet=self.__conexionInternet
                     )
                )
        return d

    def importeTelevision(self):
        imp=0
        total = self.getPrecioBase()
        definicion = self.__tipoDefinicion
        internet = self.__conexionInternet
        if definicion == 'SD':
                imp = total + (total / 100)
        elif definicion == 'HD':
                imp = total + (total * 2 / 100)
        elif definicion == 'FULL HD':
                imp = total + (total * 3 / 100)
        if internet == True:
                imp += total + (total * 10 / 100)
        return imp
