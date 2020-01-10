# Menu de numero de ruc
import libreria
opc=0             # opciones
max=3             # maximo de opciones

def opcionA():
     #El mombre que ingreses no debe contener numero
    a=libreria.validar_nombre(input("Ingrese Empresa:"))
    print("El monbre del usurio es:"+str(a))
    contenido=a+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Empresa  agregado")

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
