# #Escribe una función calcular_promedio(notas) que reciba una lista 
# de notas y retorne el promedio, la nota mínima y la nota máxima. 
# Además crea una función mostrar_resultado(nombre, notas) sin retorno
# que muestre 
# un reporte formateado

def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    nota_minima = min(notas)
    nota_maxima = max (notas)
    return promedio , nota_minima, nota_maxima

def mostrar_resultado(nombre, notas):
    prom, min, max = calcular_promedio(notas)
    print(f"Estudiante: {nombre}")
    print(f"Promedio: {prom:.2f}")
    print(f"Nota Minima: {min}")
    print(f"Nota Maxima: {max}")            

mostrar_resultado("Maria", [11,7,18,13])
mostrar_resultado("Rodolfo", [13,11,16,14])