# Hay 6 pilares en POO: Abstracción, Herencia, Encapsulamiento, Polimorfismo, Acoplamiento y Cohesión

# En este proyecto, se aplicarán todos esos pilares creando una Cuenta Bancaria


from abc import ABC, abstractmethod


# Pilar 1: Abstracción / Pilar 5 y 6 en las propias estructuras de las clases: Acoplamiento y Cohesión

class Cliente:

    def __init__(self, titular,numero_de_cuenta):

        self.titular = titular

        self.numero_de_cuenta = numero_de_cuenta

    def __str__(self):

        return f"Cliente: {self.titular} con número de cuenta {self.numero_de_cuenta}"


class Cuenta(ABC, Cliente):

    def __init__(self, titular, numero_de_cuenta, saldo):

        super().__init__(titular, numero_de_cuenta)
        self.__saldo = saldo

    @abstractmethod
    def depositar(self, cantidad):

        pass


    @abstractmethod
    def retirar(self, cantidad):

        pass

    @property
    def saldo(self):

        return self.__saldo

    @saldo.setter
    def saldo(self, cantidad):

        if cantidad < 0:

            print("No puedes tener saldo negativo")

        else:

            self.__saldo = cantidad


# Heredamos de class Cuenta
class CuentaBancaria(Cuenta):
    def __init__(self, titular, numero_de_cuenta, saldo):
        super().__init__(titular, numero_de_cuenta, saldo)
        self.gestor_transacciones = GestorTransacciones(self)  # Pilar 5: Acoplamiento

    def depositar(self, cantidad):
        self.gestor_transacciones.depositar(cantidad)

    def retirar(self, cantidad):
        self.gestor_transacciones.retirar(cantidad)



class CuentaAhorros(Cuenta):

    def depositar(self, cantidad):

        cantidad += self.__saldo + (cantidad * 0.03) / 365


    def retirar(self, cantidad):

        if cantidad <= self.__saldo:

            self.__saldo -= cantidad

        else:

            print("[!] No tienes saldo suficiente. Deposita más dinero o presta dinero del banco para seguir haciendo operaciones.")






# Pilar 4: Polimorfismo

class GestorTransacciones:
    def __init__(self, cuenta):
        self.cuenta = cuenta

    def depositar(self, cantidad):
        if cantidad > 0:
            self.cuenta.saldo += cantidad
            print(f"Depósito exitoso. Saldo actual: {self.cuenta.saldo}€")
        else:
            print("Cantidad inválida.")

    def retirar(self, cantidad):
        if cantidad > self.cuenta.saldo:
            print("[!] Fondos insuficientes.")
        else:
            self.cuenta.saldo -= cantidad
            print(f"Retiro exitoso. Saldo actual: {self.cuenta.saldo}€")




# Ejemplo de Uso
cliente1 = CuentaBancaria("Juan Pérez", "123-456-789", 1000)
print(cliente1)  # Muestra información del cliente

cliente1.depositar(500)  # Depósito con polimorfismo
cliente1.retirar(200)  # Retiro con polimorfismo
