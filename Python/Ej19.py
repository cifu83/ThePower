'''
Crea una función lambda que filtre los números impares de una lista dada.
'''
#Definimos la funcion impar
def filtrar_impares(lista):
    #un numero es impar si el resto de su division por 2 es diferente de 0 
    return list(filter(lambda x: x % 2 != 0, lista))

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = filtrar_impares(lista_numeros)
print("Números impares:", impares)
