'''
Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por 
defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual 
que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver 
una tupla que contenga la media y el estado.

'''
def evaluar_rendimiento(lista_numeros, nota_aprobado=5):
    #Clasico de la informatica validar que la lista no este vacia, para evitar division por 0
    if not lista_numeros:
        return (0.0, "suspenso")
    
    #Calculamos la media aritmética
    media = sum(lista_numeros) / len(lista_numeros)
    
    #Determinamos el estado según la nota de corte
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
        
    # 4. Devolvemos la tupla (media, estado)
    return (media, estado)

mis_notas = [4, 6, 5, 5]
resultado = evaluar_rendimiento(mis_notas)

print(resultado)