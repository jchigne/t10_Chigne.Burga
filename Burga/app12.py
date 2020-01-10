import libreria
def dato1():
    dni=libreria.pedir_dni("DNI:")
    nombre=libreria.pedir_nombre("nombre")
    edad=libreria.pedir_numero("edad",9999999,8888888)
    contenido=dni+"-"+str(nombre)+"-"+str(edad)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("datos guardados")
def dato2():
    dni=libreria.pedir_dni("DNI:")
    nombre=libreria.pedir_nombre("nombre")
    telefono=libreria.pedir_telefono("edad",9999999,8888888)
    contenido=dni+"-"+str(nombre)+"-"+str(telefono)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("datos guardados")
def verDatos():
    datos=libreria.obtener_datos("info.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo sin datos ")

def opc_dni():
    opc=0
    max=3
    while(opc!=max):
        print("######### DATO1 ###########")
        print("#1.ingresar el numero de su dni  ")
        print("#2.ver datos")
        print("#3.salir")
        print("########################")
        opc=libreria.pedir_numero("ingrese subopcion",1,3)
        if(opc==1):
           dato1()
        if(opc==2):
           verDatos()

def opc_telefono():
    opc=0
    max=3
    while(opc!=max):
        print("#########DATO2###########")
        print("#1.ingresa el numero de telefono actual ")
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
    print("######### DATOS ###########")
    print("#1.ingresar dni: ")
    print("#2.ingresar numero de telefono: ")
    print("#3.salir")
    print("########################")
    opc=libreria.pedir_numero("ingrese opcion",1,3)
    if(opc==1):
        opc_dni()
    if(opc==2):
        opc_telefono()
#fin
print("fin del programa")
