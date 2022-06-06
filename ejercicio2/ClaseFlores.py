class flores:
    __numero: 0
    __nombre = ''
    __color = ""
    __descripcion = ""

    def __init__(self,numero,nombre,color,descripcion):
        self.__numero=numero
        self.__nombre=nombre
        self.__color=color
        self.__descripcion=descripcion
    
    def __str__(self):
        return "%s %s %s %s" % (self.__numero,self.__nombre,self.__color,self.__descripcion)
