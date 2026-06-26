'''
Dada una lista numérica, obtén el producto total de los valores de dicha lista.
Usa la función reduce() .
'''

def producto_total(producto_total):
    from functools import reduce
    return reduce(lambda x, y: x * y, producto_total)


producto_total = [1, 2, 3, 4, 5]    
print("El producto total de la lista es:", producto_total(producto_total))