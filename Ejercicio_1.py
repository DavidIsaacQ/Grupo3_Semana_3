def calcular_descuento(precio,porcentaje):
     descuento=precio * (porcentaje/100)
     precio_final= precio-descuento

     return precio_final



ahorro = 124-calcular_descuento(124,8)

print(f"Se esta ahorrando {ahorro:.2f} soles. ")





