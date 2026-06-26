'''
Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. 
Usa la función map ()
'''

def longitud_de_palabras(frase):
    #Separamos la frase en palabras usando split()
    palabras = frase.split()
    
    # Usamos map() para aplicar len a cada palabra y lo convertimos a lista
    return list(map(len, palabras))



texto = "Por que todo junto se escribe separado y sepadado todo junto"
resultado = longitud_de_palabras(texto)

print(f"Frase original: '{texto}'")
print(f"Longitud de cada palabra: {resultado}")