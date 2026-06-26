'''
Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un 
valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones 
adecuadamente.
'''

class EdadFueraDeRango(Exception):
    """Excepción lanzada cuando la edad no está entre 0 y 120."""
    pass


def solicitar_edad():
    while True:
        try:
            # Pedimos el dato al usuario
            entrada = input("Por favor, introduce tu edad: ")
            edad = int(entrada) 
            
            #Validamos la edad
            if edad < 0 or edad > 120:
                raise EdadFueraDeRango("La edad debe ser un número entre 0 y 120 años.")
            #Si la edad es valida, la retornamos
            return edad
            
        except ValueError:
            #Validamos si el usuario introdujo un valor no numérico entero
            print("Error: Debes introducir un número entero válido.\n")
            
        except EdadFueraDeRango as error_rango:
            # Captura si introdujo un número fuera del rango
            print(f"Error: {error_rango}\n")



edad_final = solicitar_edad()

print(f"Edad correcta: {edad_final} años.")