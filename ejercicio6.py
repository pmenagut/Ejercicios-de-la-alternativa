def descuento_total(microprocesadores, cliente):

    if 10000 <= microprocesadores <= 20000:
        descuento = 0.10 #10% de descuento
    elif 20001 <= microprocesadores <= 40000:
        descuento = 0.15 #15% de descuento
    else:
        descuento = 0.20 #20% de descuento

    if cliente == "COMMAQ":
        descuento -= 0.02 #quitar 2% rspecto al descuento estandar
    elif cliente == "BEL":
        descuento += 0.01 #aumenta 1% resoecto al descuento estandar

    return descuento

#ejemplo
microprocesadores = 45000
cliente = "COMMAQ"
descuento_cliente = descuento_total(microprocesadores, cliente)
print("El porcentaje de descuento para el cliente es:", descuento_cliente)