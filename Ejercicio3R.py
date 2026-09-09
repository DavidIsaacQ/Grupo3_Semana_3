# Ejercicio 3 - Calculadora de promedio con lista

def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    minima = min(notas)
    maxima = max(notas)
    return [promedio, minima, maxima]

def mostrar_resultado(nombre, notas):
    resultados = calcular_promedio(notas)

    print()
    print(f"Reporte del estudiante: {nombre}")
    print(f"El promedio es: {resultados[0]}")
    print(f"La nota minima es: {resultados[1]}")
    print(f"La nota maxima es: {resultados[2]}")


name = input("Ingresa el nombre del estudiante: ")
n = int(input("Cuantas notas ingresaras?: "))

lista_notas = []

for i in range(1, n + 1):
    nota = float(input(f"Ingresa la nota {i}: "))
    lista_notas.append(nota)

mostrar_resultado(name, lista_notas)
