# SUB MENUS 01
import libreria
opc=0
max=5

def subopcionA():
    print("Jugardor 1 ")
def subopcionB():
    print("Jugador 2 ")
def subopcionC():
    print("Mode")
    opc=0
    max=3
    while(opc != max):
        print("######Mode DK #####")
        print("1. Historia")
        print("2. Aventura")
        print("3. Salir")
        print("###################")
        opc=libreria.pedir_entero("Ocion Madev DK:",1,3)
        if (opc == 1):
            print("Mode Historia :D")
        if (opc == 2):
            print("Mode Avetura :D")

######################################################
def opcionA():
    a_invalido=True
    while (a_invalido):
        a=int(input("Ingrese 2 coins:"))
        a_invalido=(a!=2)
    print("Ingreso al juego")

    opc=0
    max=4
    while (opc != max):
        print("#### Donkey Kong ####")
        print("1. Jugador1  ")
        print("2. Jugador2  ")
        print("3. Mode")
        print("4. Exit")
        print("######################")
        opc=libreria.pedir_entero("OpcionA:",1,4)
        if (opc == 1):
            subopcionA()
        if (opc == 2):
            subopcionB()
        if (opc == 3):
            subopcionC()
        #Fin_submenu
# Fin A

##########################################################
def opcionB():
    a_invalido=True
    while (a_invalido):
        a=int(input("Ingrese 3 coins:"))
        a_invalido=(a!=3)
    print("Ingreso al juego")

    opc=0
    max=4
    while (opc != max):
        print("#### Mario Bros ####")
        print("1. Jugador1 ")
        print("2. Jugador2 ")
        print("3. Mode")
        print("4. Exit")
        print("######################")
        opc=libreria.pedir_entero("OpcionB:",1,4)
        if (opc == 1):
            subopcionA()
        if (opc == 2):
            subopcionB()
        if (opc == 3):
            subopcionC()
        #Fin_submenu
# Fin B

##################################################################
def opcionC():
    a_invalido=True
    while (a_invalido):
        a=int(input("Ingrese 1 coins:"))
        a_invalido=(a!=1)
    print("Ingreso al juego")

    opc=0
    max=4
    while (opc != max):
        print("#### Space Invaders ####")
        print("1. Jugador1 ")
        print("2. Jugador2 ")
        print("3. Mode")
        print("4. Exit")
        print("######################")
        opc=libreria.pedir_entero("OpcionB:",1,4)
        if (opc == 1):
            subopcionA()
        if (opc == 2):
            subopcionB()
        if (opc == 3):
            subopcionC()
        #Fin_submenu
# Fin C

##################################################################
def opcionD():
    a_invalido=True
    while (a_invalido):
        a=int(input("Ingrese 4 coins:"))
        a_invalido=(a!=4)
    print("Ingreso al juego")
    opc=0
    max=4
    while (opc != max):
        print("#### CONTRA ####")
        print("1. Jugador1 ")
        print("2. Jugador2 ")
        print("3. Mode")
        print("4. Exit")
        print("######################")
        opc=libreria.pedir_entero("OpcionB:",1,4)
        if (opc == 1):
            subopcionA()
        if (opc == 2):
            subopcionB()
        if (opc == 3):
            subopcionC()
        #Fin_submenu
# Fin D

##############################################################################3
##############################################################################3

while (opc != max):
    print("########### ARCADE ###########")
    print("1. Donkey Kong     (2 coins)")
    print("2. Mario Bros      (3 coins)")
    print("3. Space Invaders  (1 coins)")
    print("4. Contra          (4 coins) ")
    print("5. Salir ")
    print("##############################")
    opc=libreria.pedir_entero("Opcion:",1,5)
    if (opc == 1):
        opcionA()
    if (opc == 2):
        opcionB()
    if (opc == 3):
        opcionC()
    if (opc == 4):
        opcionD()
    # Fin While

print("Game over")
