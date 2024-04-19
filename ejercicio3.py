def descuento(precio):

    if precio < 100.00:
        resultado = 0.00 #no hay descuento
    elif precio < 500:
        resultado = precio * 0.05 #5% de descuento
    else:
        resultado = precio * 0.08 #8% de descuento

    return resultado

#ejemplo
precio_producto = 700.00
descuento = descuento(precio_producto)
print("El precio es:", descuento)
