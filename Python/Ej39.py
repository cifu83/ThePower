'''
Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 
Las reglas de calificación son:
1. 0 - 69 insuficiente
2. 70 - 79 bien
3. 80 - 89 muy bien
4. 90 - 100 excelente
'''


def obtener_calificacion_case(clasificacion):
    match clasificacion:
        # Usamos 'case _ if' para definir condiciones de rango
        case _ if 0 <= clasificacion <= 69:
            return "Insuficiente"
        case _ if 70 <= clasificacion <= 79:
            return "Bien"
        case _ if 80 <= clasificacion <= 89:
            return "Muy bien"
        case _ if 90 <= clasificacion <= 100:
            return "Excelente"
        case _:
            return "Nota fuera de rango"

def obtener_calificacion_if(clasificacion):
    if 0 <= clasificacion <= 69:
        return "Insuficiente"
    elif 70 <= clasificacion <= 79:
        return "Bien"
    elif 80 <= clasificacion <= 89:
        return "Muy bien"
    elif 90 <= clasificacion <= 100:
        return "Excelente"
    else:
        return "Nota fuera de rango"
clasificacion = int(input("Ingrese la calificación del alumno (0-100): "))
print(f"Tu calificación es: {obtener_calificacion_case(clasificacion)}")



