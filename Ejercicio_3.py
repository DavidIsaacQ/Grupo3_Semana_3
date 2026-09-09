def calcular_promedio(notas):
    return sum(notas) / len(notas), min(notas), max(notas)

def mostrar_resultado(nombre, notas):
    prom,mn,mx = calcular_promedio(notas)
    print(f"Estudiante: {nombre}")
    print(f"Promedio: {prom:.2f}")
    print(f"Nota Minima: {mn}")
    print(f"Nota Maxima: {mx}")            

mostrar_resultado("David", [13,14,11,15])
    