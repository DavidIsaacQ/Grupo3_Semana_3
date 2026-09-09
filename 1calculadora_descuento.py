# Función que calcula el precio final después de aplicar un descuento
def calcular_descuento(precio, porcentaje):
    # Calculamos cuánto dinero se descontará
    descuento = precio * (porcentaje / 100)

    # Restamos el descuento al precio original
    precio_final = precio - descuento

    # Retornamos el precio después del descuento
    return precio_final


# Datos de ejemplo
precio = 100
porcentaje = 20

# Llamamos a la función para obtener el precio final
precio_final = calcular_descuento(precio, porcentaje)

# Calculamos cuánto dinero se ahorró
ahorro = precio - precio_final

# Mostramos los resultados
print("Precio original:", precio)
print("Porcentaje de descuento:", porcentaje, "%")
print("Ahorro obtenido:", ahorro)
print("Precio final:", precio_final)