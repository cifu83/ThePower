'''
Escribe una función que tome dos parámetros:  figura  (una cadena que puede ser "rectangulo" , "circulo" o  (una cadena que puede ser "rectangulo" ,"circulo" o "triangulo" ) y datos (una tupla con los datos necesarios para calcular el área de la figura).

'''

import math

def calcular_area(figura, datos):
    # Pasamos a minúsculas para evitar problemas con "Rectángulo" o "RECTANGULO"
    figura_limpia = figura.lower()
    
    match figura_limpia:
        case "rectangulo":
            # Desempaquetamos la tupla: esperamos (base, altura)
            base, altura = datos
            return base * altura
            
        case "circulo":
            # El círculo solo necesita el radio, así que extraemos el único elemento
            radio = datos[0]
            return math.pi * (radio ** 2)
            
        case "triangulo":
            # Desempaquetamos la tupla: esperamos (base, altura)
            base, altura = datos
            return (base * altura) / 2
            
        case _:
            return "Figura no reconocida. Elige 'rectangulo', 'circulo' o 'triangulo'."
        
#Probar un Rectángulo base = 5, altura = 7
datos_rectangulo = (5, 10)
area_r = calcular_area("rectangulo", datos_rectangulo)
print(f"Área del rectángulo: {area_r}") 


#Círculo radio = 3
datos_circulo = (3,) 
area_c = calcular_area("circulo", datos_circulo)
print(f"Área del círculo: {area_c:.2f}") 

#Triángulo base = 4, altura = 6
datos_triangulo = (4, 6)
area_t = calcular_area("triangulo", datos_triangulo)
print(f"Área del triángulo: {area_t}")
