import libreria
opc=0
max=3

def opcionA():
    a=libreria.validar_nombre(input("ingrese nombre:"))
    print("el nombre del usuario es:"+str(a))

def opcionB():
    b=libreria.validar_sexo(input("ingrese sexo:"))
    print("el sexo del paciente es "+str(b))

while (opc!=max):
    #colocar menu
    print("#############################")
    print("######### SEXO ##############")
    print("#1. nombre:                 #")
    print("#2. sexo:                   #")
    print("#3. salir:                  #")
    print("#############################")
    #seleccion de la opcion
    opc=libreria.pedir_numero("ingrese opciones:",1,3)
    #mapeo de las opciones
    if(opc ==1):
        opcionA()
    if(opc==2):
        opcionB()
#fin del mapeo
