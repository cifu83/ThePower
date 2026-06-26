'''

Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con el 
carácter '#', excepto los últimos cuatro

'''

def enmascarar(cadena):
    #Convertimos la variable a cadena de texto
    cadena_str = str(cadena)
    
    #Enmascaramos todos los caracteres excepto los últimos cuatro
    if len(cadena_str) <= 4:
        return cadena_str  # Si la cadena tiene 4 o menos caracteres, no enmascaramos
    
    enmascarada = '#' * (len(cadena_str) - 4) + cadena_str[-4:]
    return enmascarada

#pedimos la cadena
cadena = input("Introduce una cadena de texto: ")
#llamamos a la función y mostramos el resultado
print("Cadena enmascarada:", enmascarar(cadena))