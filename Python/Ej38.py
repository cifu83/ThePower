'''
Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
'''

hora = input("Ingrese la hora: ")
hora = hora.split(":")[0] #Nos quedamos con la hora
if hora >= 6 and hora < 12:
    print("Es de día.")
elif hora >= 12 and hora < 119:
    print("Es de tarde.")
else:
    print("Es de noche.")