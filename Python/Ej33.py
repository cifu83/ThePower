'''
Crea una función 
lambda que sume elementos correspondientes de dos listas dadas.
'''

def sumar_listas(lista1, lista2):
   return list(map(lambda x, y: x + y, lista1, lista2))


#Ejemplo de uso:
lista_a = [1, 2, 3, 4]
lista_b = [10, 20, 30, 40]

resultado = sumar_listas(lista_a, lista_b)
print(resultado)