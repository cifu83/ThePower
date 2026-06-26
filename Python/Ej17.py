'''
Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, [5,7,2] 
corresponde al número quinientos setenta y dos [572]. Usa la función reduce()
'''
from functools import reduce

def convertir_a_numero(lista_digitos):
    #Usamos reduce() para combinar los dígitos en un solo número
    return reduce(lambda x, y: x * 10 + y, lista_digitos)
digitos = [4, 7, 2, 5]
resultado = convertir_a_numero(digitos)
print(f"Lista de dígitos: {digitos}")
print(f"Número correspondiente: {resultado}")
