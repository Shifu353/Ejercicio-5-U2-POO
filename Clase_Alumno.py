class Alumno (object):
    __nombre = ""
    __año = 0
    __divicion = 0
    __cantidadInacistencia= 0
    MaximaCantidadInacistencia = 5 
    CantTotalClases = 15

    def __init__ (self,nom,año,divicion,cantAsistencia):
        if type(nom) == str and type(año) == int and type(divicion) == int and type(cantAsistencia) == int:
            self.__nombre = nom
            self.__año = año
            self.__divicion = divicion
            self.__cantidadInacistencia = cantAsistencia
        else:
            print("Error de Tipeo")

    @classmethod
    def getCantInacistencias (cls):
        return cls.MaximaCantidadInacistencia
    @classmethod
    def setCant (self,cant):
        self.MaximaCantidadInacistencia = cant

    def getCantInasistencia (self):
        return self.__cantidadInacistencia
    
    def getNombre (self):
        return self.__nombre
    
    def __str__ (self):
        s = "Nombre {}".format(str(self.__nombre)) +"\n"
        s += "Año {}".format(str(self.__año)) + "\n"
        s += "Divicion {}".format(str(self.__divicion)) + "\n"
        s += "Cantidad de Inasistemcias {}".format(str(self.__cantidadInacistencia))
        return s

    def getAño (self):
        return self.__año
    
    def getDivicion (self):
        return self.__divicion
