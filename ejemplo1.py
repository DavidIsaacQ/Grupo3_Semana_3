def calcular_descuento(precio, porcentaje):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final


# Uso
precio = float(input("Precio Original: "))
porcentaje = float(input("El Descuento: "))

precio_final = calcular_descuento(precio, porcentaje)
ahorro = precio - precio_final

print(f"Precio original: ${precio}")
print(f"Descuento: {porcentaje}%")
print(f"Ahorraste: ${ahorro}")
print(f"Precio final: ${precio_final}")
