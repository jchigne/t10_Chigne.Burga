# Menu de vehiculos
import libreria
opc=0             # opciones
max=3             # maximo de opciones

def opcionA():
    print("Ingresio a la opcion A")
    a="MOTOS"
    contenido=a+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("vehiculo agregado")


def opcionB():
    print("Ingreso a la opcion B")
    a="AUTOS"
    contenido=a+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("vehiculo agregado")


while (opc != max):
    # 1. Imprecion del menu
    print("###################################")
    print("###          VEHICULOS          ###")
    print("###################################")
    print("1. Motos:                         #")
    print("2. Carros:                        #")
    print("3. Salir                          #")
    print("###################################")
    # 2. Eleccion de la opcion
    opc=libreria.pedir_entero("Ingrese Opciones:",1,3)

    #3. Mapeo de la opcion
    if(opc == 1):
        opcionA()
    if(opc == 2):
        opcionB()
    #fin mapeo


#fin_while
print("Fin del MENU")
