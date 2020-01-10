import libreria
def identificacion1():
    dni=libreria.pedir_dni("DNI:")
    nombre=libreria.pedir_nombre("nombre")
    edad=libreria.pedir_numero("edad",1,49)
    contenido=dni+"-"+str(nombre)+"-"+str(edad)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("datos guardados")
def identificacion2():
    dni=libreria.pedir_dni("DNI:")
    nombre=libreria.pedir_nombre("nombre")
    edad=libreria.pedir_numero("edad",51,100)
    contenido=dni+"-"+str(nombre)+"-"+str(edad)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("datos guardados")
def verDatos():
    datos=libreria.obtener_datos("info.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo sin datos ")

def menores_de_edad():
    opc=0
    max=3
    while(opc!=max):
        print("#########IDENTIFICACION1###########")
        print("#1.identificacion a menores de 50 años de edad  ")
        print("#2.ver datos")
        print("#3.salir")
        print("########################")
        opc=libreria.pedir_numero("ingrese subopcion",1,3)
        if(opc==1):
           identificacion1()
        if(opc==2):
           verDatos()

def mayores_de_edad():
    opc=0
    max=3
    while(opc!=max):
        print("#########IDENTIFICACION2###########")
        print("#1.identificacion a mayores de 50 años de edad  ")
        print("#2.ver datos")
        print("#3.salir")
        print("########################")
        opc=libreria.pedir_numero("ingrese subopcion",1,3)
        if(opc==1):
           identificacion2()
        if(opc==2):
           verDatos()

opc=0
max=3
while(opc!=max):
    print("#########MENU###########")
    print("#1.menores de edad ")
    print("#2.mayores de edad")
    print("#3.salir")
    print("########################")
    opc=libreria.pedir_numero("ingrese opcion",1,3)
    if(opc==1):
        menores_de_edad()
    if(opc==2):
        mayores_de_edad()
#fin
print("fin del programa")
