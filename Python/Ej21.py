'''
Crea una función que calcule el cubo de un número dado mediante una función 
lambda
'''

def calcular_cubo(numero):
    # Usamos una función lambda para calcular el cubo del número
    cubo = (lambda x: x ** 3)(numero)
    
    return cubo

numero = int(input("Ingrese un número para calcular su cubo: "))
cubo_resultado = calcular_cubo(numero)
print(f"El cubo de {numero} es: {cubo_resultado}")
