'''
Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras 
pero en diferente orden.
'''

def son_anagramas(palabra1, palabra2):
    #Limpiamos ambos textos: quitamos espacios y pasamos a minúsculas
    p1 = palabra1.replace(" ", "").lower()
    p2 = palabra2.replace(" ", "").lower()
    
    #Ordenamos las letras de cada palabra y las comparamos
    return sorted(p1) == sorted(p2)

#Ejemplos:
print(son_anagramas("Roma", "Amor"))
print(son_anagramas("Desganado", "Asignado"))
print(son_anagramas("Raza", "Zara"))