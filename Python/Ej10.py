'''
Escribe una función que reciba una lista de números y calcule su promedio.
 Si la lista está vacía, lanza una 
excepción personalizada y maneja el error adecuadamente.
'''
def calcular_promedio(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)


lista_numeros = []

try:
    resultado = calcular_promedio(lista_numeros)
except ValueError as e:
    print(f"Error de validación: {e}")
else:
    print("La media. El resultado es:", resultado)


