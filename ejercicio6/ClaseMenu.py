class Menu():
    def mostrarMenu(self):
        opcion=None
        print('Menú de Opciones: ')
        print('-----------------')
        print('1 - Insertar un aparato en la colección en una posición determinada.')
        print('2 - Agregar un aparato a la colección (solicitar el tipo de aparato, y luego los datos que correspondan)')
        print('3 - Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición')
        print('4 - Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea phillips')
        print('5 - Mostrar la marca de todos los lavarropas que tienen carga superior')
        print('6 - Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta.')
        print('7 - Almacenar los objetos de la colección Lista en el archivo “aparatoselectronicos.json”.')
        print('8 - Salir ')
        opcionCorrecta = False
        while not opcionCorrecta:
            opcion=int(input('Seleccione un número del 1 al 8: '))
            if opcion in [1,2,3,4,5,6,7,8]:
                opcionCorrecta=True
        return opcion
