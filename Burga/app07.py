import libreria
#funciones del menu
def pedirCarrera():
    carrera=libreria.pedir_carrera("ingrese fruta: ")
    contenido=carrera+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("se pidio la carrera")
def opcionCarrera():
    data=libreria.obtener_datos("info.txt")
    if(data!=""):
        print(data)
    else:
        print("intente de nuevo")

#menu generico
opc=0
max=3
while(opc != max):
    print("################### MENU #######################")
    print("#1.ingrese carrera: ")
    print("#2.opciones de carrera: ")
    print("#3.salir")
    print("################################################")
    #2.eleccion de la opcion del menu
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    #3.mapeo de las opciones
    if(opc==1):
        pedirCarrera()
    if(opc ==2):
        opcionCarrera()
#fin_while
print("fin del menu ")
