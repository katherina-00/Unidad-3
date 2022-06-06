from ClaseManejadorEquipos import ManejadorEquipos
from ClaseManejadorJugador import ManejadorJugador
from ClaseManejadorContrato import ManejadorContrato
if __name__ == "__main__":
    e = ManejadorEquipos(3)
    e.crearEquipo()
    print(e)

    j = ManejadorJugador()
    b = int(input("Ingrese la cantidad de jugadores a firmar contrato: "))
    c = ManejadorContrato(b)
    while b != 0:
        j.crearJugador()
        e.contrato(j, c)
        b -= 1

    e.muestraContratos()
    c.buscaJugador(j)
    c.buscaEquipo(e)
    c.buscaImportes(e)
    c.generaArchivo(j, e)
