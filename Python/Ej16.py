'''
 Escribe una función que tome una cadena de texto y un número entero n como parámetros y 
 devuelva una lista de 
todas las palabras que sean más largas que n. Usa la función filter()
'''

def filtrar_palabras_largas(cadena, n):
    #Separamos la cadena en palabras usando split()
    palabras = cadena.split()
    
    #Usamos filter() para filtrar las palabras que tengan longitud mayor a n
    palabras_filtradas = filter(lambda palabra: len(palabra) > n, palabras)
    
    #Devolvemos el resultado como una lista
    return list(palabras_filtradas)

texto = "El rápido zorro marrón salta sobre el perro perezoso"
n = 4   
palabras_largas = filtrar_palabras_largas(texto, n)
print(f"Palabras más largas que {n} caracteres:", palabras_largas)