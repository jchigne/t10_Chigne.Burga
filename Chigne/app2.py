# Menu de dni
import libreria
opc=0             # opciones
max=3             # maximo de opciones

def opcionA():
    #El mombre que ingreses no debe contener numero
    a=libreria.validar_nombre(input("Ingrese nombre:"))
    print("El monbre del usurio es:"+str(a))
    contenido=a+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Nombre agregado")

def opcionB():
    #El dni debe contener 8 numeros
    b=libreria.validar_dni(input("Ingrese DNI:"))
    print("El DNI de usuario es:"+ str(b))

while (opc != max):
    # 1. Imprecion del menu
    print("#######################")
    print("###      Renic     ###")
    print("#######################")
    print("1. Nombre:            #")
    print("2. Dni:               #")
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
