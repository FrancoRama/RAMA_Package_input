from Array_Generales import *
#MAIN#
# Menú - Arrays -  Funciones
# Actividades

# Realizar un menú de opciones en donde el usuario pueda realizar las siguientes operaciones:
#8 Salir
# Notas:
# Solo se podrá ingresar a las opciones b a g, siempre y cuando el usuario haya ingresado los datos solicitados.
# Todas las opciones deberán ser programadas en funciones: habrá funciones específicas (por ejemplo para determinar si un número es positivo o negativo) y funciones de nivel general (por ejemplo una función que liste los números pares). Tener en cuenta las características de la programación funcional.
# Las funciones específicas deberán estar en el módulo “Especificas.py”, mientras que las generales en el módulo “Array_Generales.py”. Todos estos módulos deben estar integrados en el paquete Package_Arrays.
# Utilizar las funciones input del paquete Package_Input.
# Consejo: Primero realizar el desarrollo de las funciones y probarlas. Luego, armar los módulos y paquetes.
###################### ######################## ######################### ########################### ######################## ###########
bandera = False
while True:
    opcion = menu()
    match opcion:
        case "1":
#1 Pedir el ingreso de 10 números enteros entre -1000 y 1000. 
                ingreso = igreso_numeros()
                bandera = True
        case "2":
#2 Mostrar la cantidad de números positivos y negativos.
            if validacion_primera_ves(bandera) :
                mostrar_pos_neg(ingreso)
            else:
                print("primero tiene que ingresar numeros")
        case "3":
#3 Mostrar la sumatoria de los números pares.
            if validacion_primera_ves(bandera) :
                mostra_sumatoria_pares(ingreso)
            else:
                print("primero tiene que ingresar numeros")
        case "4":
#4 Informar el mayor de los números impares.
            if validacion_primera_ves(bandera) :
                ifor_mayor_impar(ingreso)
            else:
                print("primero tiene que ingresar numeros")
        case "5":
#5 Listar todos los números ingresados.
            if validacion_primera_ves(bandera) :
                listado_de_ingresados(ingreso)
            else:
                print("primero tiene que ingresar numeros")
        case "6":
#6 Listar todos los números pares.
            if validacion_primera_ves(bandera) :
                listado_pares(ingreso)
            else:
                print("primero tiene que ingresar numeros")
        case "7":
#7 Listar los números de las posiciones impares.  
            listado_impares(ingreso)
        case "8":
            break

#falta validaciones