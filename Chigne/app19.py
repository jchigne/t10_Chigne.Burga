# SUB MENU 09
import libreria
opc=0             # opciones
max=5             # maximo de opciones

def subopcionA():
    print("Usd jugara a elegido jugar solo")
def subopcionB():
    print("Usd jugara a elegido jugar un grupo de 4")

def subopcionA1():
    print("Usd jugara una partida rapida")
def subopcionB1():
    print("Usd jugara una partida clasificatoria")


def opcionA():
    print("Vienvenido a FORNITE")
    a=libreria.validar_cadena(input("Ingrese ID:"))
    b=libreria.validar_cadena(input("Ingrese contraseña:"))
    print("Ingreso al juego")
    contenido=a+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("ID agregado")
    contenido=b+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Contraseña agregada")


    opc=0
    max=3
    while (opc != max):
        print("###########################")
        print("####      FORNITE      ####")
        print("###########################")
        print("1. SOLO                   #")
        print("2. GRUPAL                 #")
        print("3. Exit                   #")
        print("###########################")
        opc=libreria.pedir_entero("OpcionA:",1,3)
        if (opc == 1):
            subopcionA()
        if (opc == 2):
            subopcionB()
        #Fin_submenuopc


def opcionB():
    print("Vienvenido a LOL")
    a=libreria.validar_cadena(input("Ingrese ID:"))
    b=libreria.validar_cadena(input("Ingrese contraseña:"))
    print("Ingreso al juego")
    contenido=a+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("ID agregado")
    contenido=b+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Contraseña agregada")
    opc=0
    max=3
    while (opc != max):
        print("###########################")
        print("######     LOL       ######")
        print("###########################")
        print("1. PARTIDA RAPIDA         #")
        print("2. PARTIDA RANKED         #")
        print("3. Exit                   #")
        print("###########################")
        opc=libreria.pedir_entero("OpcionA:",1,3)
        if (opc == 1):
            subopcionA1()
        if (opc == 2):
            subopcionB1()
        #Fin_submenuopc

def opcionC():
    print("Vienvenido a DOTA")
    a=libreria.validar_cadena(input("Ingrese ID:"))
    b=libreria.validar_cadena(input("Ingrese contraseña:"))
    print("Ingreso al juego")
    contenido=a+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("ID agregado")
    contenido=b+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Contraseña agregada")
    opc=0
    max=3
    while (opc != max):
        print("###########################")
        print("####       DOTA        ####")
        print("###########################")
        print("1. PARTIDA RAPIDA         #")
        print("2. PARTIDA RANKED         #")
        print("3. Exit                   #")
        print("###########################")
        opc=libreria.pedir_entero("OpcionA:",1,3)
        if (opc == 1):
            subopcionA1()
        if (opc == 2):
            subopcionB1()
        #Fin_submenuopc

def opcionD():
    print("Vienvenido a FREE FIRE")
    a=libreria.validar_cadena(input("Ingrese ID:"))
    b=libreria.validar_cadena(input("Ingrese contraseña:"))
    print("Ingreso al juego")
    contenido=a+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("ID agregado")
    contenido=b+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Contraseña agregada")
    opc=0
    max=3
    while (opc != max):
        print("###########################")
        print("####      FREE FIRE    ####")
        print("###########################")
        print("1. SOLO                   #")
        print("2. GRUPAL                 #")
        print("3. Exit                   #")
        print("###########################")
        opc=libreria.pedir_entero("OpcionA:",1,3)
        if (opc == 1):
            subopcionA()
        if (opc == 2):
            subopcionB()
        #Fin_submenuopc

while (opc != max):
    # 1. Imprecion del menu
    print("#######################")
    print("###    JUEGOS       ###")
    print("#######################")
    print("1. Fornite            #")
    print("2. LOL                #")
    print("3. DOTA               #")
    print("4. FREE FIRE          #")
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
