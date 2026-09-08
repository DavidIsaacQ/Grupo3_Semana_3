def es_par(numero):
    return numero % 2 == 0


def mostrar_paridad(numero):
    if es_par(numero):
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")


cantidad = int(input("¿Cuántos números quieres introducir? "))

for i in range(cantidad):
    numero = int(input("Introduce un número: "))
    mostrar_paridad(numero)
