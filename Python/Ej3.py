'''
Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe 
devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.
'''
def filtrar_palabras(lista_palabras, palabra_objetivo):
    coincidencias = []
    
    for palabra in lista_palabras:
        # El operador 'in' comprueba si 'palabra_objetivo' es parte de 'palabra'
        if palabra_objetivo in palabra:
            coincidencias.append(palabra)
            
    return coincidencias

# Ejemplo de uso:
mis_palabras = ["girasol", "sol", "soldado", "mar", "mariposa", "submarino"]
objetivo = "sol"

resultado = filtrar_palabras(mis_palabras, objetivo)
print(resultado)