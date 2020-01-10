import libreria

def colocar_nombres():
    a=libreria.pedir_numero("ingrese sus nombres")
    contenido=a+"-"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("nombres registrados")

def colocar_apellidos():
    a=libreria.obtener_datos("info.txt")
    if(a!=""):
        print(a)
    else:
        print("apellidos registrados ")

opc=0
max=3
while opc != max :
    print("######## MENU #########")
    print(" 1.   colocar nombres")
    print(" 2.   colocar apellidos")
    print(" 3.   Salir")
    print("#######################")

    opc=libreria.pedir_numero("Ingresar opcion:",1,3) #Se hace llamado a la funcion con sus parametros

    if opc == 1:
        colocar_nombres()                             # si se escoge la opcion 1 "colocar nombres"

    if opc == 2:                                      # si se escoge la opcion 2 "colocar apellidos"
        colocar_apellidos()                           #Usaremos la funcion colocar apellidos
print("Usted selecciono la opcion Salir, muchas gracias.")


#Fin del menu
