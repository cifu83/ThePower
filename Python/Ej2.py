'''
Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map()
'''

numeros = [1, 2, 3, 4, 5]
resultado = map(lambda x: x * 2, numeros)

print(list(resultado))