# Menu Generico
import libreria
opc=0             # opciones
max=5             # maximo de opciones

def opcionA():
    print("Se ingreso a la opcion A")
def opcionB():
    print("Se ingreso a la opcion B")
def opcionC():
    print("Se ingreso a la opcion C")
def opcionD():
    print("Se ingreso a la opcion D")

while (opc != max):
    # 1. Imprecion del menu
    print("#######################")
    print("###      MENU       ###")
    print("#######################")
    print("1. opcion A           #")
    print("2. opcion B           #")
    print("3. opcion C           #")
    print("4. opcion D           #")
    print("5. Salir              #")
    print("#######################")
    # 2. Eleccion de la opcion
    opc=libreria.pedir_entero("Ingrese Opciones:",1,5)

    #3. Mapeo de la opcion
    if(opc == 1):
        opcionA()
    if(opc == 2):
        opcionB()
    if(opc == 3):
        opcionC()
    if(opc == 4):
        opcionD()


#fin_while
print("Fin del MENU")
