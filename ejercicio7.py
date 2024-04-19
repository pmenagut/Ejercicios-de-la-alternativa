def viaje_total(alumnos):

    #coste del trayecto
    if alumnos <= 25:
        coste_trayecto = 67.30
    else:
        coste_trayecto = 61.00

    #coste de la comida por dia
    coste_comida = 3.50

    #coste del alojamiento por dia
    if alumnos <= 30:
        coste_alojamiento = 4.75
    elif 31 <= alumnos <= 35:
        coste_alojamiento = 4.00
    else:
        coste_alojamiento = 3.50

    precio_alumno = coste_trayecto + coste_comida + coste_alojamiento
    precio_global = precio_alumno * alumnos

    return precio_alumno, precio_global

#ejemplo
alumnos = 40
precio_alumno, precio_global = viaje_total(alumnos)
print("El costo por alumno es:", precio_alumno, "€")
print("El costo total del viaje es:", precio_global, "€")