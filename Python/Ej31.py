'''
Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en 
esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se 
lanza una excepción.
'''

def buscar_nombre():
    #Pedimos los nombres al usuario
    nombres_input = input("Ingrese una lista de nombres separados por comas: ")
    #convertimos la cadena en lista
    lista_nombres = [nombre.strip() for nombre in nombres_input.split(',')]
    
    #Solicitar el nombre a buscar
    nombre_a_buscar = input("Ingrese un nombre para buscar en la lista: ").strip()
    
    #Verificar si el nombre está en la lista
    if nombre_a_buscar in lista_nombres:
        print(f"El nombre '{nombre_a_buscar}' fue encontrado en la lista.")
    else:
        raise ValueError(f"El nombre '{nombre_a_buscar}' no se encuentra en la lista.")
    
#Llamamo a la función
buscar_nombre()