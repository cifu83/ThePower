'''
Crea una función 
lambda que calcule el resto de la división entre dos números dados.
'''
def resto_division(a, b):
    resto = lambda x, y: x % y
    return (resto)

a = 10
b = 3   
resultado = resto_division(a, b)(a,b)
print("El resto de la división entre", a, "y", b, "es:", resultado)
