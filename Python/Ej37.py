'''
Crea una función llamada procesar_texto que procesa un texto según la opción especificada: reemplazar_palabras , procesar_texto. contar_palabras , 
eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función 
Código a seguir:
1. Crear una función contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene que devolver un diccionario.
2. Crear una función reemplazar_palabras para remplazar una palabra por otra. Tiene que devolver el texto con el remplazo de palabras.
3. Crear una función eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra eliminada.
4. Crear la función procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un número de argumentos variable según la opción indicada.
Caso de uso:
Comprueba el funcionamiento completo de la función procesar_texto
'''

def contar_palabras(texto):
    #Pasamos a minúsculas y separamos por espacios para obtener las palabras
    palabras = texto.lower().split()
    frecuencias = {}
    
    for palabra in palabras:
        #Limpiamos signos de puntuación básicos pegados a las palabras
        palabra = palabra.strip(",.!?;:")
        if palabra:
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
            
    return frecuencias


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    #Remplazamos las palabras
    return texto.replace(palabra_original, palabra_nueva)


def eliminar_palabra(texto, palabra_a_eliminar):
    # Eliminamos la palabra, usando replace para reemplazarla por una cadena vacía
    texto_modificado = texto.replace(palabra_a_eliminar, "")
    return texto_modificado


def procesar_texto(texto, opcion, *args):
 
    match opcion:
        case 1:#"contar"
            return contar_palabras(texto)
            
        case 2:#"reemplazar"
            #
            return reemplazar_palabras(texto, *args)
            
        case 3:#"eliminar"
            return eliminar_palabra(texto, *args)
            
        case _:
            #si la opción no es válida, devolvemos un mensaje de error
            return "Opción no válida. Elige entre 1, 2 o 3."

cadena = input("Introducir texto: ")

print("\n--- Menu ---")
print("1. Contar el número de veces que aparece cada palabra.")
print("2. Reemplazar una palabra por otra.")
print("3. Eliminar una palabra del texto.")

try:
    opcion = int(input("\nElige una opción (1-3): "))
except ValueError:
    opcion = 0 


match opcion:
    case 1:
        resultado = procesar_texto(cadena, opcion)
        
    case 2:
        original = input("Palabra a reemplazar: ")
        nueva = input("Nueva palabra: ")
        resultado = procesar_texto(cadena, opcion, original, nueva)
        
    case 3:
        eliminar = input("Palabra a eliminar: ")
        resultado = procesar_texto(cadena, opcion, eliminar)
        
    case _:
        resultado = procesar_texto(cadena, opcion)

print("\n--- que nos devuelve ---")
print(resultado)