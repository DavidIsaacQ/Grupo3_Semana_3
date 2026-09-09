# Función que calcula el promedio, nota mínima y nota máxima
def calcular_promedio(notas):
    # Calculamos el promedio de todas las notas
    promedio = sum(notas) / len(notas)

    # Obtenemos la nota más baja
    nota_minima = min(notas)

    # Obtenemos la nota más alta
    nota_maxima = max(notas)

    # Retornamos los tres resultados
    return promedio, nota_minima, nota_maxima


# Función que muestra el reporte del estudiante
def mostrar_resultado(nombre, notas):
    # Llamamos a la función y guardamos los tres resultados
    promedio, minima, maxima = calcular_promedio(notas)

    # Mostramos el reporte en pantalla
    print("Reporte de notas")
    print("Estudiante:", nombre)
    print("Notas:", notas)
    print("Promedio:", promedio)
    print("Nota mínima:", minima)
    print("Nota máxima:", maxima)


# Lista de notas del estudiante
notas = [15, 18, 12, 16, 19]

# Llamamos a la función para mostrar el resultado
mostrar_resultado("Abner", notas)
