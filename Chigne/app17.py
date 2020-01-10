# SUB MENU 07
import libreria
opc=0             # opciones
max=3             # maximo de opciones

def subopcionA2():
    print("Su vehiculo es una CAMIONETA")
def subopcionB2():
    print("Su vehiculo es una TICO")

def subopcionA():
    print("Su moto es lineal")
def subopcionB():

    print("Su vehiculo es una trimoto")

def opcionA():
    print("Ingresio a la opcion A")
    print("MOTOS")
    opc=0
    max=3
    while (opc != max):
        print("###########################")
        print("#### TIPO  DE MOTOS    ####")
        print("###########################")
        print("1. LINIAL                 #")
        print("2. TRIMOTO                #")
        print("3. Exit                   #")
        print("###########################")
        opc=libreria.pedir_entero("OpcionA:",1,3)
        if (opc == 1):
            subopcionA()
        if (opc == 2):
            subopcionB()
        #Fin_submenuopc


def opcionB():
    print("Ingreso a la opcion B")
    print("AUTOS")
    opc=0
    max=3
    while (opc != max):
        print("###########################")
        print("#### TIPO  DE EMPRESA  ####")
        print("###########################")
        print("1. CAMIONETAS               #")
        print("2. TICOS                #")
        print("3. Exit                   #")
        print("###########################")
        opc=libreria.pedir_entero("OpcionA:",1,3)
        if (opc == 1):
            subopcionA2()
        if (opc == 2):
            subopcionB2()
        #Fin_submenuopc

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
