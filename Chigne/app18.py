# SUB MENU 08
import libreria
opc=0             # opciones
max=5             # maximo de opciones

def opcionA():
    print("Se ingreso a Entrada")
    a=libreria.validar_cadena(input("Ingrese mombre del Entrada:"))
    print("PLato escogido:"+str(a))
    contenido=a+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Entrada agregada")


def opcionB():
    print("Se ingreso a la Plato")
    a=libreria.validar_cadena(input("Ingrese mombre del Plato:"))
    print("PLato escogido:"+str(a))
    contenido=a+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Plato agregado")

def opcionC():
    print("Se ingreso a la Bebida")
    a=libreria.validar_cadena(input("Ingrese mombre del Bebida:"))
    print("PLato escogido:"+str(a))
    contenido=a+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Bebida agregada")


def opcionD():
    print("Se ingreso a la Postre")
    a=libreria.validar_cadena(input("Ingrese mombre del Postre:"))
    print("PLato escogido:"+str(a))
    contenido=a+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Postre agregado")


while (opc != max):
    # 1. Imprecion del menu
    print("#######################")
    print("###      MENU       ###")
    print("#######################")
    print("1. Entrada            #")
    print("2. Plato              #")
    print("3. Bebida             #")
    print("4. Postre             #")
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
