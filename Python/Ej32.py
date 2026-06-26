'''
Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y 
devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona 
no trabaja aquí.
'''

def buscar_puesto(nombre_completo, lista_empleados):
    #Quitamos espacios y pasamos a minusculas
    nombre_buscado = nombre_completo.strip().lower()
    
    #Recorremos la lista de empleados uno por uno
    for empleado in lista_empleados:
        #Comparamos el nombre del empleado actual (también normalizado)
        if empleado["nombre"].strip().lower() == nombre_buscado:
            return empleado["puesto"]  # ¡Encontrado! Devolvemos su puesto inmediatamente
            
    #Si el bucle termina y no encontró nada, ejecutamos esta línea
    return f"La persona '{nombre_completo}' no trabaja aquí."


plantilla_empresa = [
    {"nombre": "Chicho Terremoto", "puesto": "Base"},
    {"nombre": "Oliver atom", "puesto": "Portero"},
    {"nombre": "Ash", "puesto": "Entrenador"},
]

# El empleado SÍ existe (y lo escribimos con variaciones de mayúsculas)
resultado1 = buscar_puesto("chicho terremoto", plantilla_empresa)
print(f"Resultado 1: {resultado1}")


#El empleado NO existe
resultado2 = buscar_puesto("Juan Sin miedo", plantilla_empresa)
print(f"Resultado 2: {resultado2}")
