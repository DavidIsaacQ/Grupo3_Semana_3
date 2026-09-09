# Ejercicio 2 - Verificados de numero par o impar

def es_par(numero):
    if numero%2 == 0:
        return True
    else:
        False

def mostrar_paridad(numero):
    if es_par(numero):
        print(F"El número {numero} es par")
    else:
        print(f"El número {numero} es impar")
         
x = int(input("Ingresa un número: "))
mostrar_paridad(x)