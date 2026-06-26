'''
Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta 
corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y 
agregar dinero al saldo.
Código a seguir:
1. Inicializar un usuario con su nombre, saldo y si tiene o no cuenta corriente mediante 
2. Implementar el método True y False .
retirar_dinero para retirar dinero del saldo del usuario. Lanzará un error en caso de no 
poder hacerse.
3. Implementar el método transferir_dinero para realizar una transferencia desde otro usuario al usuario actual. 
Lanzará un error en caso de no poder hacerse.
4. Implementar el método agregar_dinero para agregar dinero al saldo del usuario.
Caso de uso:
1. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
2. Agregar 20 unidades de saldo de "Bob".
3. Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
4. Retirar 50 unidades de saldo a "Alicia".
'''

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if not self.cuenta_corriente:
            raise Exception(f"{self.nombre} no tiene cuenta corriente.")
        if cantidad > self.saldo:
            raise Exception(f"Saldo insuficiente. Saldo actual: {self.saldo}")
        self.saldo -= cantidad
        print(f"{self.nombre} retiró {cantidad}. Saldo actual: {self.saldo}")

    def transferir_dinero(self, otro_usuario, cantidad):
        if not otro_usuario.cuenta_corriente:
            raise Exception(f"{otro_usuario.nombre} no tiene cuenta corriente.")
        if cantidad > otro_usuario.saldo:
            raise Exception(f"Saldo insuficiente en la cuenta de {otro_usuario.nombre}.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        print(f"{otro_usuario.nombre} transfirió {cantidad} a {self.nombre}. "
              f"Saldo {otro_usuario.nombre}: {otro_usuario.saldo} | "
              f"Saldo {self.nombre}: {self.saldo}")

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad
        print(f"Se agregaron {cantidad} a {self.nombre}. Saldo actual: {self.saldo}")

alicia = UsuarioBanco("Alicia", 100, True)
bob    = UsuarioBanco("Bob",    50,  True)

bob.agregar_dinero(20)


alicia.transferir_dinero(bob, 80)
