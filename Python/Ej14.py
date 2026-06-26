'''

Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la 
función filter()

'''

def filtrar_por_letra(lista_palabras, letra_inicial):
    #Pasamos la letra a minuscula
    letra_buscada = letra_inicial.lower()
    
    #Filtramos la lista de palabras pasando a minuscula cada palabra y comparando con la letra buscada
    palabras_filtradas = filter(lambda palabra: palabra.lower().startswith(letra_buscada), lista_palabras)
    
    #Devolvemos el resultado como una lista
    return list(palabras_filtradas)



animales = ["Perro", "gato", "Panda", "loro", "Pantera", "Elefante", "pájaro", "perezoso", "Tigre", "Cocodrilo"]
letra = "p"

resultado = filtrar_por_letra(animales, letra)

print(f"Lista original: {animales}")
print(f"Palabras que empiezan con '{letra}': {resultado}")