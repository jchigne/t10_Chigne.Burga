import libreria
#funciones del menu
def opcionA():
    nombre=libreria.pedir_nombre("ingrese fruta: ")
    numero=libreria.pedir_numero("ingrese numero:",1,100)
    contenido=str(numero)+"-"+nombre+"-"+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se selecciono la primera opcion")
def opcionB():
    data=libreria.obtener_datos("info.txt")
    if(data!=""):
        print(data)

#menu generico
opc=0
max=3
while(opc != max):
    print("################### MENU #######################")
    print("#1.ingresar nombre ")
    print("#2.ingresar continente ")
    print("#3.salir")
    print("################################################")
    #2.eleccion de la opcion del menu
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    #3.mapeo de las opciones
    if(opc==1):
        opcionA()
    if(opc ==2):
        opcionB()
#fin_while
print("fin del menu ")
