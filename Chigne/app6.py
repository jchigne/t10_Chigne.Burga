# Menu Promedio final
import libreria
opc=0             # opciones
max=3             # maximo de opciones

def opcionA():
    # El mombre que ingreses no debe contener numero
    a=libreria.validar_codigo(input("Ingrese codigo:"))
    # La letra no puede ser un numero y solo puede estar formada por una
    b=libreria.validar_letra_codigo(input("Ingrese letra de su codigo:"))
    print("El codigo del alumno es:"+str(a)+str(b))
    contenido=a+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("codigo agregado")


def opcionB():
    #Las notas deben estar en un interbalo de 0 y 20
    nota1=libreria.validar_nota(input("Ingrese nota01:"))
    nota2=libreria.validar_nota(input("Ingrese nota02:"))
    nota3=libreria.validar_nota(input("Ingrese nota03:"))
    #El pormedio es la suma de las 3 notas entre 3
    promedio=(nota1+nota2+nota3)/3
    print("El promedio de notas es:")
    print(promedio)

while (opc != max):
    # 1. Imprecion del menu
    print("###################################")
    print("###            NOTAS            ###")
    print("###################################")
    print("1. Codigo del alumno:             #")
    print("2. Promedio:                      #")
    print("3. Salir                          #")
    print("###################################")
    # 2. Eleccion de la opcion
    opc=libreria.pedir_entero("Ingrese Opciones:",1,3)

    #3. Mapeo de la opcion
    if(opc == 1):
        opcionA()
    if(opc == 2):
        opcionB()
    #fin mapeo


#fin_while
print("Fin del MENU")
