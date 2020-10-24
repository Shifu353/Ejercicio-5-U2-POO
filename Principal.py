from ManejadorAlumno import Lista_Alumno

if __name__ == "__main__":
    alumno = Lista_Alumno()
    alumno.CargarLista()

    def op1 ():
        Año =  int(input("Ingrese Año: "))
        divicion = int(input("Ingrese Divicion: "))
        alumno.Item1(Año,divicion)
    def op2 ():
        from Clase_Alumno import Alumno
        nuevo = input("Ingrese Nueva cantidad de inasistencia: ")
        Alumno.setCant(nuevo)
        print("El Valor se Cambio por: ",Alumno.getCantInacistencias())
    opcion = None
    diccionario = {1:op1,2:op2}

    while opcion!=3:
        print("| Ingrese 1 para ver Porcentaje de Inasistencia         |")
        print("| Ingrese 2 para Modificar la Cant. Max de Inasistecia  |")
        print("| Ingrese 3 para Salir                                  |")
        opcion = int(input("Ingrese Opcion: "))
        op = diccionario.get(opcion,lambda: print("Opcion Incorrecta"))
        op()
