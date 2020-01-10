# SUB MENU 10
import libreria
opc=0             # opciones
max=5             # maximo de opciones

def subopcionA():
    print("GRUPO A : DEL APELLIDO 'A' HASTA 'H' ")
def subopcionB():
    print("GRUPO A : DEL APELLIDO 'I' HASTA 'Z' ")

def opcionA():
    print("Programacion I")
    a=libreria.validar_cadena(input("Ingrese Cliclo:"))
    b=libreria.validar_codigo(input("Ingrese codigo:"))
    print("Su codigo es :"+str(b))
    contenido=a+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Ciclo agregado")
    contenido=b+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Codigo agregado")
    opc=0
    max=3
    while (opc != max):
        print("###########################")
        print("####   PROGRAMACIONI   ####")
        print("###########################")
        print("1. GRUPOA                 #")
        print("2. GRUPOB                 #")
        print("3. Exit                   #")
        print("###########################")
        opc=libreria.pedir_entero("OpcionA:",1,3)
        if (opc == 1):
            subopcionA()
        if (opc == 2):
            subopcionB()
        #Fin_submenuopc

def opcionB():
    print("Mate Basica")
    a=libreria.validar_cadena(input("Ingrese Cliclo:"))
    b=libreria.validar_codigo(input("Ingrese codigo:"))
    print("Su codigo es :"+str(b))
    contenido=a+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Ciclo agregado")
    contenido=b+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Codigo agregado")
    opc=0
    max=3
    while (opc != max):
        print("############################")
        print("#### MATEMATICA BASICA  ####")
        print("###########################")
        print("1. GRUPOA                 #")
        print("2. GRUPOB                 #")
        print("3. Exit                   #")
        print("###########################")
        opc=libreria.pedir_entero("OpcionA:",1,3)
        if (opc == 1):
            subopcionA()
        if (opc == 2):
            subopcionB()
        #Fin_submenuopc

def opcionC():
    print("Analisis Mate")
    a=libreria.validar_cadena(input("Ingrese Cliclo:"))
    b=libreria.validar_codigo(input("Ingrese codigo:"))
    print("Su codigo es :"+str(b))
    contenido=a+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Ciclo agregado")
    contenido=b+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Codigo agregado")
    opc=0
    max=3
    while (opc != max):
        print("############################")
        print("#### ANALISIS MATEMATICO ####")
        print("###########################")
        print("1. GRUPOA                 #")
        print("2. GRUPOB                 #")
        print("3. Exit                   #")
        print("###########################")
        opc=libreria.pedir_entero("OpcionA:",1,3)
        if (opc == 1):
            subopcionA()
        if (opc == 2):
            subopcionB()
        #Fin_submenuopc

def opcionD():
    print("Quimica")
    a=libreria.validar_cadena(input("Ingrese Cliclo:"))
    b=libreria.validar_codigo(input("Ingrese codigo:"))
    print("Su codigo es :"+str(b))
    contenido=a+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Ciclo agregado")
    contenido=b+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Codigo agregado")
    opc=0
    max=3
    while (opc != max):
        print("###########################")
        print("######    QUIMICA    ######")
        print("###########################")
        print("1. GRUPOA                 #")
        print("2. GRUPOB                 #")
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
    print("###      MENU       ###")
    print("#######################")
    print("1. Programacion       #")
    print("2. Mate Basica        #")
    print("3. Analisis Mate      #")
    print("4. Quimica            #")
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
