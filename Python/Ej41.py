'''
En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el 
monto final de una compra en una tienda en línea, después de aplicar un descuento. El programa debe hacer lo 
siguiente:
1. Solicita al usuario que ingrese el precio original de un artículo.
2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor a cero). Por ejemplo, descuento de 15€. 
5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu programa de Python.
'''

try:
    # 1. Solicita el precio original
    precio_original = float(input("Introduce el precio original del artículo (€): "))
    
    # 2. Pregunta si tiene un cupón (limpiamos espacios y pasamos a minúsculas)
    tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

    # 6. Uso de estructuras if, elif y else
    if tiene_cupon == "sí" or tiene_cupon == "si":
        # 3. Solicita el valor del cupón de descuento
        descuento = float(input("Introduce el valor del cupón de descuento (€): "))
        
        # 4. Aplica el descuento si el valor es válido (mayor a cero)
        if descuento > 0:
            # max(0, ...) evita que el precio sea negativo si el descuento es enorme
            precio_final = max(0.0, precio_original - descuento)
            print(f"\n ¡Cupón válido aplicado! Se han descontado {descuento}€.")
        else:
            precio_final = precio_original
            print("\n El valor del cupón debe ser mayor a cero. No se aplicó descuento.")
            
    elif tiene_cupon == "no":
        precio_final = precio_original
        print("\nNo se ha aplicado ningún cupón de descuento.")
        
    else:
        precio_final = precio_original
        print("\n Respuesta no válida (debes responder 'sí' o 'no'). Se mantiene el precio original.")

    # 5. Muestra el precio final de la compra
    print(f"El monto final de tu compra es: {precio_final:.2f}€")

except ValueError:
    print("\n Error: Por favor, introduce un número válido para los precios.")