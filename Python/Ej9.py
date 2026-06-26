'''
Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista 
excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", 
"Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función 
filter()    
'''


def filtrar_mascotas_permitidas(lista_mascotas):
    #Definimos la lista de mascotas prohibidas. Convertimos los nombres a minúsculas para facilitar la comparación.
    prohibidas = ["mapache", "tigre", "serpiente pitón", "cocodrilo", "oso"]
    
     #Evaluamos con filter, tambien pasando las mascotas a minúsculas para comparar con la lista de prohibidas.
    resultado = filter(lambda mascota: mascota.lower() not in prohibidas, lista_mascotas)
    
    #Devolvemos el resultado como una lista.
    return list(resultado)


mis_mascotas = ["Perro", "Mapache", "Gato", "Oso", "Canario", "Tigre"]
mascotas_legales = filtrar_mascotas_permitidas(mis_mascotas)

print(mascotas_legales)