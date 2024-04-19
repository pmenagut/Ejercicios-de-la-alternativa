def prima_anual(accidentes, distancia, antigüedad):
    prima_antigüedad = 200
    coste_km = 0.01
    prima_distancia = 400

    if antigüedad < 4:
        prima_antigüedad = 0.00
    else:
        prima_antigüedad = 200 + 20 * (antigüedad - 4)

    prima_distancia = min(coste_km * distancia, prima_distancia)

    suma_prima = prima_antigüedad + prima_distancia

    if accidentes == 1:
        prima = 0.50 * suma_prima
    elif accidentes == 2:
        prima = 0.33 * suma_prima
    elif accidentes == 3:
        prima = 0.25 * suma_prima
    elif accidentes > 3:
        prima = 0
    else:
        prima = suma_prima / (accidentes + 1)
    
    return prima

#ejemplo
accidentes = 2
distancia = 15000
antigüedad = 5
prima = prima_anual(accidentes, distancia, antigüedad)
print("La prima anual del conductor es:", prima, "€")

    