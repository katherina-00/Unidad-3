from ClaseColeccion import coleccion

if __name__ == "__main__":
    tam = int(input("Ingrese tamanio del arreglo coleccion: "))
    col = coleccion(tam)
    col.CrearColeccion()
    costo = 0
    consumo = 0
    a = int(input("Ingrese 1 si quiere saber el calefactor electrico de menor consumo o 2 si quiere saber el calefactora gas de menor consumo: "))
    if a == 1:
        costo = int(100)   # int(input("Ingrese el costo del kilowatt/h: "))
        consumo = int(2)   # int(input("Ingrese cantidad que se estima consumir por hora: "))
        col.menorConsumo(costo, consumo, a)
    elif a == 2:
        costo = int(100)   # int(input("Ingrese el costo por m3: "))
        consumo = int(2)   # int(input("Ingrese cantidad que se estima consumir en m3: "))
        col.menorConsumo(costo, consumo, a)

    col.MenorCalefactores(costo, consumo)
