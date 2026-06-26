'''
Calcula la diferencia total en los valores de una lista. Usa la función 
reduce() .
'''

from functools import reduce

valores = [10, 5, 8, 3]

# Aquí no definimos una función con 'def', usamos lambda directamente
resultado = reduce(lambda x, y: x - y, valores)

print(resultado)