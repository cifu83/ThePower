'''
Crea una función 
lambda que  sume 3 a cada número de una lista dada
'''

def sumar_tres(lista_numeros):
    #Usamos map() para aplicar la función lambda a cada elemento de la lista
    return list(map(lambda x: x + 3, lista_numeros))

numeros = [1, 2, 3, 4, 5]
resultado = sumar_tres(numeros)

print("Lista con 3 sumado a cada elemento:", resultado)