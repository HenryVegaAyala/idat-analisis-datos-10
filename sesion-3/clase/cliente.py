class Cliente:
    def __init__(self, nombre, apellido, saldo, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.saldo = saldo
        self.edad = edad

    def comprar(self, monto):
        if monto <= self.saldo:
            self.saldo = self.saldo - monto
            print(f"Compra realizada por {monto}.")
        else:
            print("Saldo insuficiente para realizar la compra.")

    def mostrar_saldo(self):
        print(f"Saldo actual de {self.nombre} {self.apellido}: {self.saldo}")

juan = Cliente("Juan", "Pérez", 1000, 30)
juan.mostrar_saldo()
juan.comprar(350)
juan.mostrar_saldo()
