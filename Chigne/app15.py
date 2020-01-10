# SUB MENU 05
import libreria
opc=0             # opciones
max=3             # maximo de opciones

def subopcionA():
    print("Su empresa es NACIONAL ")
def subopcionB():
    print("Su empresa es PRIVADA")

def opcionA():
    #El mombre que ingreses no debe contener numero
    a=libreria.validar_nombre(input("Ingrese Empresa:"))
    contenido=a+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Empresa agregada")
    opc=0
    max=3
    while (opc != max):
        print("###########################")
        print("#### TIPO  DE EMPRESA  ####")
        print("###########################")
        print("1. NACIONAL               #")
        print("2. PRIVADO                #")
        print("3. Exit                   #")
        print("###########################")
        opc=libreria.pedir_entero("OpcionA:",1,3)
        if (opc == 1):
            subopcionA()
        if (opc == 2):
            subopcionB()
        #Fin_submenuopc

    print("El monbre del usurio es:"+str(a))

def opcionB():
    #El numero que ingreses debe contener 12 digitos
    b=libreria.validar_ruc(input("Ingrese Numero de ruc:"))
    print("El ruc de la empresa es:"+ str(b))
    contenido=b+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("RUC agregado")


while (opc != max):
    # 1. Imprecion del menu
    print("#######################")
    print("###    INDECOPI     ###")
    print("#######################")
    print("1. Empresa:           #")
    print("2. Numero ruc:        #")
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
