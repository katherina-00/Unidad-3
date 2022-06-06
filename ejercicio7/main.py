from ClaseMenu import Menu
from ClaseObjetEncoder import ObjectEncoder
from ClaseColeccion import coleccion

if __name__ == '__main__':

    jsonF = ObjectEncoder()

    c = coleccion()

    dic = jsonF.leerJSONArchivo("personal.json")
    coleccion = jsonF.decodificarDiccionario(dic)


    bandera=True
    while bandera:
        menu=Menu()
        opcion=menu.mostrarMenu()
        if opcion==1:
            p=input("Ingrese indice donde agregara el aparato")
            c.insertarElemento(p,coleccion)
        elif opcion==2:
            c.agregarElemento(coleccion)
        elif opcion==3:
            pos=input("Ingrese poscion para ver que objeto se encuenta")
            c.mostrarElemento(pos)
        elif opcion==4:
            c.generaListadoDocenteInvestigador()
        elif opcion==5:
            area=input("Ingrese area")
            c.segunArea(area)
        elif opcion==6:
            c.listadoOrdenadoApellido()
        elif opcion==7:
            cat=input("Ingrese categoria")
            c.segunCategoria(cat)
        elif opcion==8:
                d=coleccion.toJSON()
                jsonF.guardarJSONArchivo(d,'personal.json')
        else:
            bandera=False
            print('Ha salido')

