# validar entero
def validar_entero_positivo(num):
    # 1. La instancia de num es int
    # 2. num > 0
    if (isinstance(num,int)):
        if (num > 0):
            return True
        else:
            return False
    else:
        return False
# fin_def
def pedir_entero(msg,ri,rf):
    n=0
    while(validar_entero_positivo(n)==False):
        n=input(msg)
        if (n.isdigit()== True):
            n=int(n)
    # fin_while
    return int(n)
#fin_def


def validar_real(num):
    if ( isinstance(num, float)):
        if ( num > 0 or num==float):
            return True
        else:
            return False
    else:
        return False
    #fin_if
#fin_def

def validar_cadena(cad):
    if ( isinstance(cad, str)):
        if ( cad != ""):
            return cad
        else:
            return False
    else:
        return False
    #fin_if
#fin_def


def validar_booleano(b):
    if ( isinstance(b, bool)):
        return True

    else:
        return False
    #fin_if
#fin_def

# validar DNI
def validar_dni(dni):
    if (dni.isdigit()== True):
        if (len(dni)==8):
            dni=int(dni)
            return dni
        else:
            print("DNI INCORRECTO")
            input("Ingrese DNI NUEVAMENTE:")
    else:
        print("DNI INCORRECTO")
        input("Ingrese DNI NUEVAMENTE:")


# validar sexo
sexo,sexo_invalido="",False
def validar_sexo(sexo):
    sexo=sexo.upper()
    sexo_invalido=(sexo!="MASCULINO" and sexo!="FEMENINO")
    while(sexo_invalido==True):
        print("SEXO INVÁLIDO")
        sexo=input("ingrese sexo nuevamente:")
        sexo=sexo.upper()
        sexo_invalido=(sexo!="MASCULINO" and sexo!="FEMENINO")
    #fin_while
    return sexo
#fin_def)

# validar nombre
def validar_nombre (nombre):
    nombre=nombre.upper()
    if (nombre.isalpha()==True):
        return nombre
    else:
        print("NOMBRE INVALIDO")
        input("Ingrese nombre nuevamente:")

# validar telefono
def validar_telefono(telefono):
    if (telefono.isdigit()== True):
        if (len(telefono)==9):
            telefono=int(telefono)
            return telefono
        else:
            input("Ingrese telefono:")
    else:
        input("Ingrese telefono:")


# Validar nota Profe
def validar_nota(nota):
    if (isinstance(nota,float) or isinstance(nota,int)):
        nota=float(nota)
        if (nota>=0.0 and nota <= 20.0):
            return nota
        else:
            return False
    else:
        return False

# fin def

# Validar numero de ruc
def validar_ruc(ruc):
    if (ruc.isdigit()== True):
        if (len(ruc)==12):
            ruc=int(ruc)
            return ruc
        else:
            input("Ingrese numero de RUC:")
    else:
        input("Ingrese numero de RUC:")

#Validar codigo
def validar_codigo(codigo):
    if (codigo.isdigit()== True):
        if (len(codigo)==6):
            codigo=(int(codigo))
            return codigo
        else:
            input("Ingrese codigo nuevamente:")
    else:
        input("Ingrese codigo nuevamente:")

def validar_letra_codigo(msg):
    if (msg.isalpha()==True):
        if (len(msg)==1):
            return msg.upper()
        else:
            print("Imgrese denuevo:")
    else:
        print("Ingrese denuevo:")

def agregar_datos(ruta_archivo,contenido,modo):
    archivo=open(ruta_archivo,modo)
    archivo.write(contenido)
    archivo.close()

def obtener_datos(ruta_archivo):
    archivo=open(ruta_archivo,"r")
    datos=archivo.read()
    archivo.close()
    return datos


def obtener_datos_lista(nombre_archivo):
    archivo=open(nombre_archivo)
    lista = archivo.readlines()
    archivo.close()
    return lista


def validar_ip(ip):
    # 1. Revisar que el nro de octetos sea 4
    data=ip.split(".")
    if ( len(data) != 4):
        return False

    # 2. Los 4 octetos deben ser enteros
    oct1 = data[0]
    oct2 = data[1]
    oct3 = data[2]
    oct4 = data[3]
    if ( oct1.isdigit() == False or oct2.isdigit() == False or
         oct3.isdigit() == False or oct4.isdigit() == False):
        return False

    # 3. Cada octeto esta entre 0 y 255
    oct1 = int(data[0])
    oct2 = int(data[1])
    oct3 = int(data[2])
    oct4 = int(data[3])
    if ( validar_rango(oct1, 0, 255) == False or
         validar_rango(oct2, 0, 255) == False or
         validar_rango(oct3, 0, 255) == False or
         validar_rango(oct4, 0, 255) == False):
        return False

    # 4. Si llego hasta aqui, es porque es un IP valido
    return True
#fin_validar

def pedir_ip(msg):
    ip_invalido=True
    while( ip_invalido == True ):
        ip=input(msg)
        ip_invalido = ( validar_ip(ip) == False)
    #fin_while
    return ip

def validar_rango(num,ri,rf):
    # 1. Es un entero positivo
    # 2. Esta dentro del rango
    if (validar_entero_positivo(num) == True):
        if (num >= ri and num <= rf):
            return True
        else:
            return False
    else:
        return False
#fin_def

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
