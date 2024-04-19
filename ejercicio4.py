def calcular_media(notas):
    media = sum(notas) / 4
    return media

def resultado_total(media):
    if media > 15:
        resultado = "Alumno con talento"
    elif 12 < media <= 15:
        resultado = "Con capacidad"
    else:
        resultado = "Debe orientarse"
    return resultado

def main():
    notas = []
    for i in range(4):
        nota = int(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)

    media_alumno = calcular_media(notas)
    resultado_alumno = resultado_total(media_alumno)

    print("La media del alumno es:", media_alumno)
    print("El resultado del alumno es:", resultado_alumno)

if __name__ == "__main__":
    main()



    