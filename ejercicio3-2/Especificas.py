def menu()->str: 
    """le pregunta al usuario que opcion quiere y devuelve la opcion elegida 
    """
    print("1. ingrese 10 números enteros entre -1000 y 1000.\n2. Muestra la cantidad de números positivos y negativos.\n3. Muestra la sumatoria de los números pares.\n4. Informa el mayor de los números impares.\n5. Listar todos los números ingresados.\n6. Listar todos los números pares.\n7. Listar los números de las posiciones impares.\n8. Salir")
    
    opcion = input("ingrese el numero de la opcion preferida: ")
    return opcion

def crea_lista(cantidad:int = 10 ,elemento:int = 0)->list:
    lista = [elemento] * cantidad
    return lista

def contar_positivos(lista:list) -> int:
    contador_pos = 0
    for i in range(len(lista)):
        if lista[i] > 0 :
            contador_pos += 1
    return contador_pos

def contar_negativos(lista:list) -> int:
    contador_neg = 0
    for i in range(len(lista)):
        if lista[i] < 0 :
            contador_neg += 1
    return contador_neg


def sumatoria_pares(lista:list) -> int:
    sumatoria = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            sumatoria += lista[i]
    return sumatoria

def mayor_impar(lista:list):
    bandera = True
    for i in range(len(lista)):
        if (not lista[i] % 2 == 0) or (bandera == True):
            bandera = False
            mayor = lista[i]
    return mayor

def validacion_primera_ves(bandera:bool)->bool:
    if bandera == True:
        return True
    else:
        return False