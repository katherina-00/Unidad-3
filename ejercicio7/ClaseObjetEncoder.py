import json
from pathlib import Path
from ClaseColeccion import personal


class ObjectEncoder:
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_=eval(class_name)

            if class_name=='coleccion':
                personal=d['personal']
                dPersonal = personal[0]
                coleccion = class_()


                for i in range(len(personal)):
                    dPersonal=personal[i]
                    class_name=dPersonal.pop('__class__')
                    class_=eval(class_name)
                    atributos=dPersonal['__atributos__']
                    unPersonal=class_(**atributos)
                    coleccion.agregarAparato(unPersonal)

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
