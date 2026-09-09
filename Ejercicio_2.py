def es_par(numero):
    return numero % 2 == 0


def mostrar_paridad(numero):
    if es_par(numero):
        print(f"El número {numero} es PAR.")
    else:
        print(f"El número {numero} es IMPAR.")


numeros = [0,3,8,15,22,25]

for n in numeros:
    mostrar_paridad(n)
                


