'''
Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función 
map()

'''
def convertir_tuplas_a_strings(lista_tuplas):
    #Usamos lambda para tomar cada tupla 't' y formatearla como un string
    resultado = map(lambda t: f"Nombre: {t[0]}, Edad: {t[1]}", lista_tuplas)
    
    #Convertimos el objeto map en una lista final
    return list(resultado)

#Ejemplo de uso:
datos = [("Ana", 25), ("Carlos", 30), ("Elena", 22)]
lista_strings = convertir_tuplas_a_strings(datos)

print(lista_strings)