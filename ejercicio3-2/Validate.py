

def validate_number(numero:str):
    if numero.isalpha():
        return False
    else:
        return True

def validate_length(longitud: int,minimo:int,maximo:int):
    if longitud < minimo or longitud > maximo:
        return True
    else:
        return False
