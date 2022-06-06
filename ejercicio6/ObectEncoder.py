import json
from pathlib import Path
from ClaseColeccion import coleccion


class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_=eval(class_name)

            if class_name=='coleccion':
                aparatos=d['aparatos']
                dAparatos = aparatos[0]
                coleccion = class_()


                for i in range(len(aparatos)):
                    dAparatos=aparatos[i]
                    class_name=dAparatos.pop('__class__')
                    class_=eval(class_name)
                    atributos=dAparatos['__atributos__']
                    unAparato=class_(**atributos)
                    coleccion.agregarAparato(unAparato)

                return coleccion

    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
        return diccionario

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)
