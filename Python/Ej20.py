'''
Para una lista con elementos tipo integer y string obtén una nueva lista 
sólo con los valores int. Usa la función 
filter()

'''

def obtener_enteros(lista_mixta):
    #Usamos isinstance(elemento, int) para preguntar: Si es entero o no
    resultado = filter(lambda x: isinstance(x, int), lista_mixta)
    
    # Convertimos el resultado del filtro a una lista
    return list(resultado)

# Ejemplo de uso:
datos = [10, "Python", 42, "Código", 7, "Mentor", 100]
enteros = obtener_enteros(datos)

print(enteros)