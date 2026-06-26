'''
 Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes 
(nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 
90. Usa la función 
filter()
'''

# 1. Creamos la lista de diccionarios con la información de los estudiantes
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Carlos", "edad": 22, "calificacion": 88},
    {"nombre": "Sofía", "edad": 19, "calificacion": 92},
    {"nombre": "Luis", "edad": 21, "calificacion": 75},
    {"nombre": "María", "edad": 23, "calificacion": 90},
    {"nombre": "Pedro", "edad": 20, "calificacion": 84}
]

# 2. Usamos filter() junto con una función lambda
# La lambda recibe cada diccionario (estudiante) y evalúa si su calificación es >= 90
filtrado = filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes)

# 3. Convertimos el iterador resultante en una lista real
estudiantes_top = list(filtrado)


# --- Mostrar los resultados de forma limpia ---
print("Estudiantes con calificación mayor o igual a 90:")

for estudiante in estudiantes_top:
    print(f"• {estudiante['nombre']} (Edad: {estudiante['edad']}) - Nota: {estudiante['calificacion']}")