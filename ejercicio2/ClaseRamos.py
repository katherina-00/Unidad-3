class ramos:
    __tamanio = ""
    __flores= []

    def __init__(self,tamanio=None,flor=None):
        self.__tamanio=tamanio
        if flor!=None:
            self.addFlores(flor,1)

    def addFlores(self,flor,cantidad):
        for i in range (cantidad):
            self.__flores.append(flor)

    def getLista(self):
        return self.__flores
