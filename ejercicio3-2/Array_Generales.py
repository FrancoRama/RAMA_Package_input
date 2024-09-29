from Especificas import *
from Input import get_int


# Pedir el ingreso de 10 números enteros entre -1000 y 1000. 

def igreso_numeros()->list:
    
    mensaje = "ingrese un numero"
    mensaje_ERROR = "ERROR ingrese otra vez un entero"
    contador = 0
    numeros = crea_lista()
    
    while contador < 10 :
        ingreso = get_int(mensaje,mensaje_ERROR,-1000,1000,3)
        numeros[contador] = ingreso
        contador += 1
    return numeros

############################################################

#Mostrar la cantidad de números positivos y negativos.


def mostrar_pos_neg(lista:list):
    positivos = contar_positivos(lista)
    negativos = contar_negativos(lista)
    print(f"la cantidad de positivos son: {positivos}")
    print(f"la cantidad de negativos son: {negativos}")

def mostra_sumatoria_pares(lista:list):
    sumatoria = sumatoria_pares(lista)
    print(f"la suma de los pares es: {sumatoria}")

def ifor_mayor_impar(lista:list):
    mayor = mayor_impar(lista)
    print(f"el mayor impar es: {mayor}")

def listado_de_ingresados(lista:list):
    for i in range(len(lista)):
        print(f"{i+1}. {lista[i]}")

def listado_pares(lista:list):
    numeracion = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            numeracion += 1
            print(f"{numeracion}. {lista[i]}")

def listado_impares(lista:list):
    numeracion = 0
    for i in range(len(lista)):
        if not lista[i] % 2 == 0:
            numeracion += 1
            print(f"{numeracion}. {lista[i]}")
