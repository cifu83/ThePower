'''
Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico 
o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje 
indicando si la división fue exitosa o no.

'''


try:
    #Pedimoe el dividendo
    dividendo = input("Ingrese el dividendo: ")
    #Pedimos el divisor
    divisor = input("Ingrese el divisor: ")
    #hacecmos la division
    resultado = float(dividendo) / float(divisor)
#Validamos que la division no sea por 0
except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")
else:
    print("La división se pudo hacer. El resultado es:", resultado)

