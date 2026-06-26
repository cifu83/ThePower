'''
Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función 
map()

'''
def restar_listas(lista1, lista2):
    # Lambda reciberá dos argumentos, uno de cada lista, y devolverá la resta de ambos
    #  (x de lista1, y de lista2)
    resultado = map(lambda x, y: x - y, lista1, lista2)
    # Convertimos el objeto map en una lista real
    return list(resultado)

# Creamos las dos listas 
numeros_a = [10, 20, 30, 40]
numeros_b = [3, 5, 12, 20]
#Pasamos las listas a la función y mostramos el resultado
lista_resultado = restar_listas(numeros_a, numeros_b)
print(lista_resultado)