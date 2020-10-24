from Clase_Alumno import Alumno
class Lista_Alumno ():
    __Lista = None

    def __init__ (self):
        self.__Lista = []

    def CargarLista (self):
        import csv
        archivo = open("Alumnos.csv")
        leer = csv.reader(archivo,delimiter=";")

        for alumno in leer:
            self.__Lista.append(Alumno(alumno[0],int(alumno[1]),int(alumno[2]),int(alumno[3])))
        #print(len(self.__Lista))
        archivo.close()
    
    def Item1 (self,year,divicion):
        print("{}                {}".format("Alumno","Porcentaje"))
        for alu in range(len(self.__Lista)):
            if int(self.__Lista[alu].getAño()) == int(year) and int(self.__Lista[alu].getDivicion()) == int(divicion):
                if(int(self.__Lista[alu].getCantInasistencia()) > int(self.__Lista[alu].getCantInacistencias())):
                    print("{}            {}%".format(self.__Lista[alu].getNombre(),(self.__Lista[alu].getCantInasistencia()*100)/(self.__Lista[alu].getCantInacistencias())))
    

        
