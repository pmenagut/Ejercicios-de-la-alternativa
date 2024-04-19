def descuento_total(niños):

    if niños == 2:
        descuento = 0.10 #10% de descuento
    elif niños == 3:
        descuento = 0.15 #15% de descuento
    elif niños == 4:
        descuento = 0.18 #18% de descuento
    elif niños >= 5:
        descuento = 0.18 + 0.01*(niños - 4) #18% + 1% * (niño que va por encima de 4) de descuento
    else:
        descuento = 0 #no hay descuento

    return descuento

#ejemplo
niños = 6
descuento_familia = descuento_total(niños)

print("El descuento que se aplicara es:", descuento_familia)