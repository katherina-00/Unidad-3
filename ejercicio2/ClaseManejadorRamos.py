from ClaseRamos import ramos
class ManejadorRamo:

    def __init__(self):
        self.__listaRamo=[]
    
    
    def __str__(self):
        s = ""
        for ramos in self.__listaRamo:
            s += str(ramos) + '\n'
        return s
    
    def crearRamo(self):
        objeto=ramos()
        tamanio=input("Ingrese tamanio: ")
        flor=input("Ingrese flor para el ramo, al terminar pulse 'fin': ")
        if flor!="fin":
            objeto=ramos(tamanio,flor)
        else:
            self.__listaRamo.append(objeto.getLista())
    
    def FloresVendidas(self):
        for i in range (len(self.__listaRamo)):
            #if isinstance(i, (len(self.__listaRamo))):
                #self.__listaRamo[i]
            pass
