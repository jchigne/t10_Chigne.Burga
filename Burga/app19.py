import libreria
def dato1():

    sexo=libreria.pedir_sexo("nombre")
    contenido=sexo+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("datos guardados")
def dato2():
    continente=libreria.pedir_continente("IGV:")
    nombre=libreria.pedir_nombre("nombre")
    contenido=continente+"-"+str(nombre)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("datos guardados")
def verDatos():
    datos=libreria.obtener_datos("info.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo sin datos ")

def opc_sexo():
    opc=0
    max=3
    while(opc!=max):
        print("#########DATO1###########")
        print("#1.ingresar su  sexo: ")
        print("#2.ver datos")
        print("#3.salir")
        print("########################")
        opc=libreria.pedir_numero("ingrese subopcion",1,3)
        if(opc==1):
           dato1()
        if(opc==2):
           verDatos()

def opc_continente():
    opc=0
    max=3
    while(opc!=max):
        print("#########DATO2###########")
        print("#1.ingresar el continente : ")
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
    print("#1.ingresar sexo:  ")
    print("#2.ingresar continente ")
    print("#3.salir")
    print("########################")
    opc=libreria.pedir_numero("ingrese opcion",1,3)
    if(opc==1):
        opc_sexo()
    if(opc==2):
        opc_continente()
#fin
print("fin del programa")
