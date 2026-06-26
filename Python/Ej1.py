'''
Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias 
de cada letra en la cadena. Los espacios no deben ser considerados.
'''

#El usuario introduce una cadena de texto
cadena = input("Introduce una cadena de texto: ")

#definimos el diccionario para almacenar las frecuencias de cada letra
frecuencias = {}

#Remplazamos los espacios por nada para no contarlos y lo pasamos todo a minúsculas
cadena = cadena.replace(" ", "").lower()

for caracter in cadena:
 #Recorremos la cadena de caracter y vamos contando 
    if caracter in frecuencias:
        frecuencias[caracter] += 1
    else:
        frecuencias[caracter] = 1
        
print(frecuencias)