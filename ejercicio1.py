def sucesor(dia):

    tabla_dias = {1: "Lunes", 2: "Martes", 3: "Miercoles", 4: "Jueves", 5: "Viernes", 6: "Sabado", 0: "Domingo"}

    if not 0<= dia <= 6:
        raise ValueError("El numero de j debe ser entre el 0 y 6")
   

    resultado = (dia + 1) % 7
    return tabla_dias[resultado]

#ejemplo
print(sucesor(0))
