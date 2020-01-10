# Menu de juegos online
import libreria
opc=0             # opciones
max=5             # maximo de opciones

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
