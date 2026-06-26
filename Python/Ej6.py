'''
Escribe una función que calcule el factorial de un número de manera recursiva.
'''

def factorial_recusivo(numero):
#Vemos si el numero es 0, porque el factorial de 0 es 1
    if numero == 0 :
        return 1
    #Si no es 0, tendremos que llamar a la funcion recusivamente restando 1 hasta llegar a 0
    else:
    #Inicializamos a 1. 
        resultado = 1
        #Hacemos un bucle desde 1 hasta el numero que queremos calcular el factorial
        for i in range(1, numero + 1):
            resultado = resultado * i  #
        
    return resultado

# Ejemplo de uso:
numero_factorial = 4
print(factorial_recusivo(numero_factorial))