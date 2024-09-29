from Validate import *


def get_int(mensaje:str,mensaje_error:str,minimo:int,maximo:int,reintentos:int)-> int|None:
    #  En donde:
    # mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
    print(mensaje)
    n_ingresasdo = input()
    
    intentos = 0
    while  validate_number(n_ingresasdo) == False:
        if intentos == (reintentos):
            # reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.
            # En caso de que la función no haya podido conseguir un número válido, la misma retorna None.
            print(None)
        print(mensaje_error)
        intentos += 1
        n_ingresasdo = input()
    n_ingresasdo = int(n_ingresasdo)
    while (n_ingresasdo < minimo or n_ingresasdo > maximo):
    # mínimo: valor mínimo admitido (inclusive)
    # máximo: valor máximo admitido (inclusive)
        # mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
        if intentos == (reintentos):
            # reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.
            # En caso de que la función no haya podido conseguir un número válido, la misma retorna None.
            return None
        print(mensaje_error)
        intentos += 1
        n_ingresasdo = int(input())
    return n_ingresasdo

def get_float(mensaje:str,mensaje_error:str,minimo:int,maximo:int,reintentos:int)-> int|None:
    #  En donde:
    # mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
    print(mensaje)
    n_ingresasdo = input()
    
    intentos = 0
    while validate_number(n_ingresasdo) == False:
        if intentos == (reintentos):
            # reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.
            # En caso de que la función no haya podido conseguir un número válido, la misma retorna None.
            print(None)
        print(mensaje_error)
        intentos += 1
        n_ingresasdo = input()
    n_ingresasdo = float((n_ingresasdo))
    while (n_ingresasdo < minimo or n_ingresasdo > maximo):
    # mínimo: valor mínimo admitido (inclusive)
    # máximo: valor máximo admitido (inclusive)
        # mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
        if intentos == (reintentos):
            # reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.
            # En caso de que la función no haya podido conseguir un número válido, la misma retorna None.
            print(None)
        print(mensaje_error)
        intentos += 1
        n_ingresasdo = float(input())
    return n_ingresasdo

def get_string(longitud:int,minimo:int=4,maximo:int=10,mensaje_error:str="error")->str|None:
    while validate_length(longitud,minimo,maximo) == True:
        print(mensaje_error)
        longitud = int(input())


