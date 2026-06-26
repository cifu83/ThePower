'''
Concatena una lista de palabras.Usa la función reduce() .
'''

from functools import reduce

palabras = ["Python", "es", "increíblemente", "potente"]

# Aquí no definimos una función con 'def', usamos lambda directamente
resultado = reduce(lambda x, y: x + " " + y, palabras)

print(resultado)