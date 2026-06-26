'''
Crea una función que calcule el promedio de una lista de números.
'''

from Python.Ej10 import calcular_promedio


def calcular_media(lista_numeros):
    # Validamos si la lista está vacía para evitar una división entre cero (ZeroDivisionError)
    if not lista_numeros:
        return 0.0
    
    # Sumamos todos los elementos y dividimos entre el total
    return sum(lista_numeros) / len(lista_numeros)

# Ejemplo de uso:
notas = [8, 9, 10, 7, 6]
resultado = calcular_media(notas)

print(f"la media es: {resultado}")