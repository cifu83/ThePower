'''
Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en 
mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función 
filter()
'''

def mapear_letras(conjunto_caracteres):
    vistos = set()
    
    #Función de orden superior para filter()
    def es_letra_unica(caracter):
        #Filtramos: Solo nos interesan las letras del abecedario
        if not caracter.isalpha():
            return False
        
        #Filtramos: Convertimos a minúscula para evitar repetidos (ej: 'A' y 'a')
        letra_base = caracter.lower()
        if letra_base in vistos:
            return False
        
        #Si es una letra nueva, la guardamos en el set y la dejamos pasar
        vistos.add(letra_base)
        return True

    #Aplicamos el filter() para obtener solo caracteres válidos y únicos
    caracteres_filtrados = filter(es_letra_unica, conjunto_caracteres)
    
    #Construimos la lista de tuplas
    return [(c.upper(), c.lower()) for c in caracteres_filtrados]


#
#Pasamos una lista con repetidos, mayúsculas/minúsculas mezcladas, números y símbolos
entrada = ['a', 'B', '3', 'a', 'b', 'C', '$', 'A', 'z']
resultado = mapear_letras(entrada)

print(f"Entrada original: {entrada}")
print(f"Resultado final:  {resultado}")