'''
Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
'''

def buscar_duplicado(lista):
    #Creamos un conjunto vacío para registrar los elementos que vamos viendo
    elementos_vistos = set()
    
    for elemento in lista:
        #Si el elemento ya existe en el conjunto, es el primer duplicado
        if elemento in elementos_vistos:
            return elemento
        
        #Si no estaba, lo añadimos al conjunto y seguimos buscando
        elementos_vistos.add(elemento)
        
    #Si el bucle termina y no encontró nada, devolvemos None
    return None


#Lista con un duplicado
numeros = [1, 2, 3, 4, 3, 2, 5]
print(f"Primer duplicado: {buscar_duplicado(numeros)}")