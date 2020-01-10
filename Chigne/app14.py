# SUB MENU 04
import libreria
opc=0             # opciones
max=3             # maximo de opciones


def subopcionA1():
    print("Su operador es MOVISTAR")
def subopcionB1():
    print("Su operador es CLARO")
def subopcionC1():
    print("Su operador es ENTEL")
def subopcionD1():
    print("Su operador es VITEL")


def subopcionA():
    print("Su genero es MASCULINO ")
def subopcionB():
    print("Su genero es FEMENINO ")


def opcionA():
     #El mombre que ingreses no debe contener numero
    a=libreria.validar_nombre(input("Ingrese nombre:"))
    print("El monbre del usurio es:"+str(a))
    contenido=a+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Nombre agregado")

    opc=0
    max=3
    while (opc != max):
        print("#### SEXO DEL USUARIO ####")
        print("1. MASCULINO  ")
        print("2. FEMENINO  ")
        print("3. Exit")
        print("######################")
        opc=libreria.pedir_entero("OpcionA:",1,3)
        if (opc == 1):
            subopcionA()
        if (opc == 2):
            subopcionB()
        #Fin_submenuopc

def opcionB():
    #El numero que ingreses debe contener 9 digitos
    b=libreria.validar_telefono(input("Ingrese Telefono:"))
    print("El Telefono de usuario es:"+ str(b))
    opc=0
    max=5
    while(opc != max):
        print("##########################")
        print("####     OPERADOR     ####")
        print("##########################")
        print("#1. Movistar             #")
        print("#2. Claro                #")
        print("#3. Entel                #")
        print("#4. Vitel                #")
        print("#5. Salir                #")
        print("##########################")
        opc=libreria.pedir_entero("OpcionB:",1,5)
        if (opc == 1):
            subopcionA1()
        if (opc == 2):
            subopcionB1()
        if (opc == 3):
            subopcionC1()
        if (opc == 4):
            subopcionD1()




while (opc != max):
    # 1. Imprecion del menu
    print("#######################")
    print("###    Movistar     ###")
    print("#######################")
    print("1. Nombre:            #")
    print("2. Numero cel:        #")
    print("3. Salir              #")
    print("#######################")
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
