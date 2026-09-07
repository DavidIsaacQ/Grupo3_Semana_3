# #Escribe una función llamada calcular_descuento(precio, porcentaje)
#  que reciba el precio original de 
# un producto y el porcentaje de descuento, 
# y retorne el precio final después del descuento. Luego 
# muestra el ahorro obtenido

def calcular_descuento (precio, porcentaje):
    descuento = precio*(porcentaje/100)
    precio_final = precio - descuento
    print (f"Usted ahorro {descuento}")
    return precio_final


prec_con_dscto = calcular_descuento (100, 20)
print (f"Precio con descuento = {prec_con_dscto}")
