# Función que verifica si un número es par
def es_par(numero):
    # Si el resto de dividir entre 2 es 0, el número es par
    return numero % 2 == 0


# Función que muestra si el número es par o impar
def mostrar_paridad(numero):
    # Llamamos a es_par() para verificar el número
    if es_par(numero):
        print(numero, "es par")
    else:
        print(numero, "es impar")


# Lista de números que vamos a verificar
numeros = [2, 5, 8, 11, 14]

# Recorremos cada número de la lista
for numero in numeros:
    # Mostramos si cada número es par o impar
    mostrar_paridad(numero)