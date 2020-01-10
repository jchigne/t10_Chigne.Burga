import libreria
def dato1():
    telefono=libreria.pedir_tlefono("telefono:")
    nombre=libreria.pedir_nombre("nombre")
    contenido=telefono+"-"+str(nombre)+"-"+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("datos guardados")
def dato2():
    continente=libreria.pedir_continente("continente:")
    nombre=libreria.pedir_nombre("nombre")
    contenido=continente+"-"+str(nombre)+"-"+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("datos guardados")
def verDatos():
    datos=libreria.obtener_datos("info.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo sin datos ")

def opc_telefono():
    opc=0
    max=3
    while(opc!=max):
        print("######### Dato1 ###########")
        print("#1.ingresar el numero de telefono ")
        print("#2.ver datos")
        print("#3.salir")
        print("########################")
        opc=libreria.pedir_numero("ingrese subopcion",1,3)
        if(opc==1):
           dato1()
        if(opc==2):
           verDatos()

def opc_residencia():
    opc=0
    max=3
    while(opc!=max):
        print("######### DATO2 ###########")
        print("#1.ingresar en nombre del continente : ")
        print("#2.ver datos")
        print("#3.salir")
        print("########################")
        opc=libreria.pedir_numero("ingrese subopcion",1,3)
        if(opc==1):
           dato2()
        if(opc==2):
           verDatos()

opc=0
max=3
while(opc!=max):
    print("#########MENU###########")
    print("#1.ingresar numero de telefono: ")
    print("#2.ingresar continente de residencia ")
    print("#3.salir")
    print("########################")
    opc=libreria.pedir_numero("ingrese opcion",1,3)
    if(opc==1):
        opc_telefono()
    if(opc==2):
        opc_residencia()
#fin
print("fin del programa")
