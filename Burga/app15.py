import libreria
def dato1():

    fruta=libreria.pedir_fruta("nombre")
    contenido=fruta+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("datos guardados")
def dato2():
    igv=libreria.pedir_igv("IGV:")
    nombre=libreria.pedir_nombre("nombre")
    contenido=igv+"-"+str(nombre)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("datos guardados")
def verDatos():
    datos=libreria.obtener_datos("info.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo sin datos ")

def opc_frutas():
    opc=0
    max=3
    while(opc!=max):
        print("#########DATO1###########")
        print("#1.ingresar frutas: ")
        print("#2.ver datos")
        print("#3.salir")
        print("########################")
        opc=libreria.pedir_numero("ingrese subopcion",1,3)
        if(opc==1):
           dato1()
        if(opc==2):
           verDatos()

def opc_igv():
    opc=0
    max=3
    while(opc!=max):
        print("#########DATO2###########")
        print("#1.ingresar el igv : ")
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
    print("#1.elegir frutas:  ")
    print("#2.mostrar igv total: ")
    print("#3.salir")
    print("########################")
    opc=libreria.pedir_numero("ingrese opcion",1,3)
    if(opc==1):
        opc_frutas()
    if(opc==2):
        opc_igv()
#fin
print("fin del programa")
