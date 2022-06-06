import csv
from claseFacultad import facultad
from claseCarrera import carrera
class ManejaFacultades:
    def __init__(self):
        self.__Facultades=[]
    
    def __str__(self):
        s = ""
        for facultad in self.__Facultades:
            s += str(facultad) + '\n'
        return s

    def agregarFacultad(self,unaFacultad):
        self.__Facultades.append(unaFacultad)

    def CrearFacultad(self):
        with open("Facultades.csv", "r") as file:
            reader = csv.reader(file, delimiter=",")
            fila = next(reader)
            bandera = True
            while bandera:
                listaCarrera = []
                print("carreras:")
                filaCarrera = next(reader)
                while bandera and fila[0]==filaCarrera[0]:
                    objeto = carrera(fila[0],fila[1],fila[2],fila[3],fila[4])
                    listaCarrera.append(objeto)
                    try:
                        filaCarrera = next(reader)
                    except StopIteration:
                        bandera = False
                #print("{}".format(listaCarrera))
                cod = fila[0]
                nombre = fila[1]
                direccion = fila[2]
                localidad = fila[3]
                telefono = fila[4]
                unaFacultad = facultad(cod,nombre,direccion,localidad,telefono,listaCarrera)
                self.agregarFacultad(unaFacultad)
                fila=filaCarrera
    
    def mostrarSegunCodigo (self,cod=1):
        for i, facultad in enumerate (self.__Facultades):
            if cod == facultad.getCodigo():
                print("Nombre de la facultad: {}".format(facultad.getNombre()))
                print("Datos de la/las carreras de la facultad: {}".format(facultad.getDatosCarrera(cod)))
    
    def mostrarSegunNombreCarrera(self,nom="Ingeniería Electrónica"):
        for i, facultad in enumerate (self.__Facultades):
            if nom in facultad.getDatosCarrera():
                print("Codigo: {}".format(facultad.getCodigo()+facultad.getDatosCarrera(0)))
                print("Nombre de la facultad: {}. Localidad donde se dicta {}".format(facultad.getNombre,facultad.__localidad()))
