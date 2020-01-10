
def validar_entero(n):
    if (isinstance(n,int)): # Pregunta si el numero ingresado(n) es un entero
        return True      # Si cumple retorna True
    else:
        return False     # De no ser un entero retornara False


def validar_rango(n, ri, rf): # Se le envia el numero con el rango (ri,rf) rango inical y final respectiamente
    if ( validar_entero(n) == True): # Si cumple el validar_entero entonces:
                                     # Empezara a validar si esta dentro del rango
        if ( n >= ri and n<= rf):    # El numero debe ser mayor igual que ri y menor igual que rf
            return True  # Si cumple retorna True
        else:
            return False # Sino retorna False
    else:
        return False # De no cumplirse validar_entero retorna False



def pedir_numero(msg, ri, rf):               # Los parametros seran el mensaje rango inicial
                                             #     y el rango final
    n=""                                        # n es nuesta cadena vacia
    while ( validar_rango(n, ri, rf) == False): # Mientas validar rango sea falso:
        n=input(msg)                            # Pedira ingresar el valor a n
        if (n.isdigit() == True):               # Se pregunta si la cadena posee digitos:
            n=int(n)                            # Si es asì lo convertiremos a entero

    #fin while
    return n                                    # Si validar rango es verdadero retorna el valor de n
#fin_pedir_numero

def validar_fruta(fruta):
    if(isinstance(fruta,str)):
        if(len(fruta)>=3):
            return True
    else:
        return False

def pedir_fruta(msg):
    n=""
    while(validar_fruta(n)==False):
        n=input(msg)
    return  n


def validar_nombre(nombre):
    if(isinstance(nombre,str)):
        if(len(nombre)>=3):
            return True
        else:
            return False
    else:
        return False

def pedir_nombre(msg):
    nombre=""
    while(validar_nombre(nombre)==False):
        nombre=input(msg)
    #fin_while
    return False
#fin_pedir_nombre

def validar_sexo(sexo):
    if(isinstance(sexo,str)):
        if(len(sexo)== 8 or len(sexo)==9):
            if(sexo=="Masculino"or sexo=="Femenino"):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
def pedir_sexo(msg):
    sexo=""
    while(validar_sexo(sexo)==False):
        sexo=input(msg)
    #fin_while
    return sexo
def validar_carrera(carrera):
    if(isinstance(carrera,str)):
        if(carrera=="medicina " or carrera=="derecho" or carrera=="arquitectura" or carrera=="ing.civil"):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_carrera(msg):
    carrera=""
    while(validar_carrera(carrera)==False):
        carrera=input(msg)
    #fin_while
    return carrera
#fin_def

def validar_telefono(msg):
    if (isinstance(msg,str)):

        return True
    else:
        return False
#fin_def
def pedir_telefono(msg):
    n=-1
    while(validar_telefono(n)==False):
        n=input(msg)
        if (len(n)==9 and n.isdigit()==True):
            return n
        else:
            return "nooo es:"
#fin_def

def validar_continente(cont):
    if(isinstance(cont,str)):
        if(cont=="america" or cont=="asia" or cont=="africa" or cont=="europa "):
            return  True
        else:
            return False
    else:
        return False

def pedir_continente(msg):
    cont=""
    while(validar_continente(cont)==False):
        cont=input (msg)
    #fin_while
    return cont
#fin_pedir_cont



def validar_pais(pais):
    if(isinstance(pais,str)):
        if(pais=="peru" or pais=="chile" or pais=="argentina" or pais=="ecuador"):
            return True
        else:
            return False
    else:
        return False
#fin_def

def pedir_pais(msg):
    pais=""
    while(validar_carrera(pais)==False):
        pais=input(msg)
    #fin_while
    return pais
def validar_igv(precio):
    if(isinstance(precio,float) or isinstance(precio,int)):
        if(precio>0):
            return (precio/1.18)*(18/100)
        else:
            return False
    else:
        return False

def pedir_igv(msg):
    n=-1
    while(pedir_igv(n)==False):
        n=input(msg)
        return pedir_igv(n)


def validar_dni(dni):
    # verificar si es un numero
    if(isinstance(dni,int) or isinstance(dni,str)):
        if(dni>9999999 and dni<888888888):
            return True
    else:
        return False
    # tiene que tener 8 digitos
def pedir_dni(msg):
    n=""
    while(pedir_dni(n)==False):
        n=input(msg)
        return pedir_dni(n)



def validar_nota(msg):
    if(isinstance(msg,float)):
        if(msg>=0.0 and msg<=20.0):
            return msg
        else:
            return False
    else:
        return False
def pedir_nota(msg):
    n=""
    while(pedir_nota(n)==False):
        n=input(msg)
        return pedir_nota(n)

def validar_año(año):
    # 1. Verificar si año es una cadena
    # 2. Verificar si año tiene 4 caracteres
    # 3. Verificar si año tiene forma de numeros
    # 4. Verificar si el año > 0 y <= 9999
    if ( isinstance(año, str) ):
        if ( len(año) == 4 ):
            if ( año.isdigit() == True ):
                if ( int(año) > 0 and int(año) <= 9999 ):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def pedir_año(msg):
    año=""
    while(validar_año(año)==False):
        año=input(msg)
    #fin_while
    return año
#fin_def


def validar_mes(mes):
    # 1. Verificar si mes es una cadena
    # 2. Verificar si mes tiene 2 caracteres
    # 3. Verificar si mes tiene forma de numeros
    # 4. Verificar si el mes > 0 y <= 12
    if ( isinstance(mes, str) ):
        if ( len(mes) == 2 ):
            if ( mes.isdigit() == True ):
                if ( int(mes) > 0 and int(mes) <= 12 ):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def validar_dia(dia):
    # 1. Verificar si dia es una cadena
    # 2. Verificar si dia tiene 2 caracteres
    # 3. Verificar si dia tiene forma de numeros
    # 4. Verificar si el dia > 0 y <= 31
    if ( isinstance(dia, str) ):
        if ( len(dia) == 2 ):
            if ( dia.isdigit() == True ):
                if ( int(dia) > 0 and int(dia) <= 31 ):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def guardar_datos(nombre_archivo,contenido,modo):
    archivo=open(nombre_archivo,modo)
    archivo.write(contenido)
    archivo.close()

def obtener_datos(nombre_archivo):
    archivo=open(nombre_archivo)
    contenido=archivo.read()
    archivo.close()
    return contenido



























