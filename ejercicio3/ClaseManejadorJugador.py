from ClaseJugador import jugador

class ManejadorJugador:
    __listaJugadores = []

    def __init__(self):
        self.__listaJugadores = []

    def __str__(self):
        s = ""
        for ju in self.__listaJugadores:
            s += str(ju) + "\n"
        return s

    def agregarJugador(self,unJugador):
        self.__listaJugadores.append(unJugador)
    
    def crearJugador(self):
        print("------------- Nuevo jugador -------------")
        nomb = input("Ingrese nombre del jugador: ")
        DNI = input("Ingrese dni: ")
        ciudad = input("Ingrese ciudad natal: ")
        pais = input("Ingrese pais: ")
        fechaNac = input("Ingrese fecha de nacimiento: ")
        print("\n")
        unJugador = jugador(nomb, DNI, ciudad, pais, fechaNac)
        self.agregarJugador(unJugador)

    def buscaJugador(self, jug):
        b = None
        for i, jugador in enumerate(self.__listaJugadores):
            if jug == jugador.getDNI():
                b = jugador.getJugador()
        return b

    def buscaDNI(self,indice):
        for i, jugador in enumerate(self.__listaJugadores):
            if i == indice:
                return jugador.getDNI()
