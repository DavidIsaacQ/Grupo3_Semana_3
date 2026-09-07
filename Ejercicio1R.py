# Ejercicio 1 - Calculadora de descuento

def calcular_descuento(precio, porcentaje):
    descuento = precio * (porcentaje/100)
    precio_final = precio - descuento
    
    return precio_final

precio1 = float(input("Cuanto es el precio original?: "))
desc = float(input("Cuanto porcentaje es el descuento?: "))

precio_con_descuento = calcular_descuento(precio1, desc)

ahorro = precio1 - precio_con_descuento

print(f"El precio es de {precio1}, aplicando el descuento sería {precio_con_descuento}. El ahorro es de {ahorro}")