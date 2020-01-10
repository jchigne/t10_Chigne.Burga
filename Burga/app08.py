import libreria
#funciones del menu
def opcTelefono():
    telefono=libreria.pedir_telefono("ingrese el numero de telefono: ")
    compañia=libreria.pedir_nombre("ingrese nombre: ")
    contenido=compañia+"-"+str(telefono)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("ingreso a la opcion  correctament")
def ingresarTelefono():
    datos=libreria.obtener_datos("info.txt")
    if(datos!=""):
        print(datos)
    else:
        print("error,intente de nuevo ")

#menu generico
opc=0
max=3
while(opc != max):
    print("################### MENU #######################")
    print("#1.ingresar telefono ")
    print("#2.mostrar telefono")
    print("#3.salir")
    print("################################################")
    #2.eleccion de la opcion del menu
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    #3.mapeo de las opciones
    if(opc==1):
        opcTelefono()
    if(opc ==2):
        ingresarTelefono()
#fin_while
print("fin del menu ")
