# #Crea una función es_par(numero) que retorne True si el número 
# es par o False si es impar. Luego crea otra 
# función mostrar_paridad(numero) (sin return) que use la primera 
# función e imprima el resultado en pantalla 
# con un mensaje

def es_par(numero):
    return numero % 2 == 0

def mostrar_paridad (numero):
    resultado = es_par(numero)
    if resultado:
        print (f"el numero {numero} es par, resultado = {resultado}")
    else:
        print (f"El numero {numero} es impar, resultado =  {resultado}")

mostrar_paridad (4)


