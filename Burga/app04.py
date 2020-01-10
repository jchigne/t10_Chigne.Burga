import libreria

def multiplicar_numeros():
    a=libreria.pedir_numero("ingrese valor su primer numero",-100000,100000)
    b=libreria.pedir_numero("Ingrese valor su segundo numero",-100000,100000)
    contenido="El prodcuto es:" + str(a*b) +"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("Multiplicacion realizada")

def dividir_numeros():
    a=libreria.pedir_numero("ingrese valor su primer numero",-100000,100000)
    b=libreria.pedir_numero("Ingrese valor su segundo numero",-100000,100000)
    print("El cociente de",a,"y",b,"es:",a/b)
opc=0
max=3
while opc != max :
    print("#################")
    print(" 1.   Multiplicar")
    print(" 2.   Dividir")
    print(" 3.   Salir")
    print("#################")

    opc=libreria.pedir_numero("Ingresar opcion:",1,3) #Se hace llamado a la funcion con sus parametros

    if opc == 1: # si se escoge la opcion 1 "multiplicar":
        multiplicar_numeros() #Usaremos la funcion multiplicar_numeros

    if opc == 2: # si se escoge la opcion 2 "dividir"
        dividir_numeros()  #Usaremos la funcion dividir_numeros

#Fin del menu
print("Usted selecciono la opcion Salir, muchas gracias.")
