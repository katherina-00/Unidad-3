from ObectEncoder import ObjectEncoder
from ClaseColeccion import coleccion
from ClaseMenu import Menu
if __name__ == "__main__":

    jsonF = ObjectEncoder()

    col=coleccion()

    diccionario=jsonF.leerJSONArchivo('aparatoselectronicos.json')
    aparatos=jsonF.decodificarDiccionario(diccionario)


    bandera=True
    while bandera:
        menu=Menu()
        opcion=menu.mostrarMenu()
        if opcion==1:
            p=input("Ingrese indice donde agregara el aparato")
            col.agregarAparato(aparatos)

        elif opcion==2:
            col.agregarAparato_a_Coleccion()
        elif opcion==3:
            pos=input("Ingrese poscion para ver que objeto se encuenta")
            col.mostrarObjeto(pos)
        elif opcion==4:
            col.MuestraMarca()
        elif opcion==5:
            col.LavarropaCargaSuperior()
        elif opcion==6:
            col.mostrarDatosAparatos()
        elif opcion==7:
                d=aparatos.toJSON()
                jsonF.guardarJSONArchivo(d,'aparatoselectronicos.json')
        else:
            bandera=False
            print('Ha seleccionado salir, hasta la vuelta')
