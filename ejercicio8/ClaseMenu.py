class Menu:
    def mostrarMenu(self):
        opcion=None
        print('Menú de Opciones: ')
        print('-----------------')
        print('1 - Insertar a agentes a la coleccion.')
        print('2 - Agregar agentes a la coleccion')
        print('3 - Dada una posición de la Lista: Mostrar por pantalla qué tipo de agente que se encuentra almacenado en dicha posición')
        print('4 - Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos '
              'de los agentes que se desempeñan como docentes investigadores.')
        print('5 - Dada un área de investigación, contar la cantidad de agentes que son docente    investigador, '
              'y la cantidad de investigadores que trabajen en ese área.')
        print('6 - Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.')
        print('7 - Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado, listar apellido, nombre e importe extra por docencia'
              ' e investigación, de todos los docentes investigadores que poseen esa categoría, al final del listado deberá mostrar el total de dinero'
              ' que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores '
              'de la categoría solicitada. ')
        print('8 - Almacenar los datos de todos los agentes en el archivo “personal.json ')
        print('9 - Salir ')
        opcionCorrecta = False
        while not opcionCorrecta:
            opcion=int(input('Seleccione un número del 1 al 9: '))
            if opcion in [1,2,3,4,5,6,7,8,9]:
                opcionCorrecta=True
        return opcion
