def clasificar_numeros(a,b):
    suma = a + b
    producto = a * b
    numeros_clasificados = [producto, a, suma, b]
    return sorted(numeros_clasificados)


#ejemplo
a = -15
b = 6
resultado = clasificar_numeros(a,b) 
print(resultado)