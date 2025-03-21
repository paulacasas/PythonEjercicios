class TarjetaCredito:
    def __init__(self, numeroTarjeta, saldoPendiente):
        self.numeroTarjeta = numeroTarjeta
        self.saldoPendiente = saldoPendiente

    @staticmethod
    def validarTarjeta(numero):
        # Algoritmo de Luhn para validar el número de la tarjeta
        tarjetaLista = list(numero)
        tarjetaLista.reverse()
        tarjetaInt = list(map(int, tarjetaLista))

        for i in range(1, len(tarjetaInt), 2):
            tarjetaInt[i] *= 2
            if tarjetaInt[i] > 9:
                tarjetaInt[i] -= 9

        suma = sum(tarjetaInt)

        if suma % 10 == 0:
            return True
        else:
            print("ERROR: Tarjeta inválida")
            return False

    def consultarSaldoPendiente(self):
        return self.saldoPendiente

    def pagar(self, cantidad):
        if cantidad <= self.saldoPendiente:
            self.saldoPendiente -= cantidad
            print(f"Pago realizado. Nuevo saldo pendiente: {self.saldoPendiente}")
        else:
            print("ERROR: Saldo insuficiente en la tarjeta")


class CuentaBancaria:
    def __init__(self, saldo, titular, tarjeta):
        self.__saldo = saldo
        self.__titular = titular
        self.tarjeta = tarjeta

    def depositar(self, cantidad):
        if TarjetaCredito.validarTarjeta(self.tarjeta.numeroTarjeta):
            self.__saldo += cantidad
            print(f"Depósito realizado. Nuevo saldo: {self.__saldo}")
        else:
            print("ERROR: La tarjeta no es válida. No se puede realizar el depósito")

    def retirar(self, cantidad):
        if TarjetaCredito.validarTarjeta(self.tarjeta.numeroTarjeta):
            if cantidad <= self.__saldo:
                self.__saldo -= cantidad
                print(f"Retiro realizado. Nuevo saldo: {self.__saldo}")
            else:
                print("ERROR: Fondos insuficientes en la cuenta")
        else:
            print("ERROR: La tarjeta no es válida. No se puede realizar el retiro")

    def consultarSaldo(self):
        if TarjetaCredito.validarTarjeta(self.tarjeta.numeroTarjeta):
            print(f"Saldo actual de la cuenta: {self.__saldo}")
        else:
            print("ERROR: La tarjeta no es válida. No se puede consultar el saldo")

    def consultarTitular(self):
        if TarjetaCredito.validarTarjeta(self.tarjeta.numeroTarjeta):
            print(f"Titular de la cuenta: {self.__titular}")
        else:
            print("ERROR: La tarjeta no es válida. No se puede consultar el titular")

    def realizarPagoTarjeta(self, cantidad):
        if TarjetaCredito.validarTarjeta(self.tarjeta.numeroTarjeta):
            if cantidad <= self.__saldo:
                self.__saldo -= cantidad
                self.tarjeta.pagar(cantidad)
            else:
                print("ERROR: Fondos insuficientes en la cuenta para realizar el pago")
        else:
            print("ERROR: La tarjeta no es válida. No se puede realizar el pago")


# Ejemplo de uso
tarjeta = TarjetaCredito("4539148803436467", 1000)  # Número de tarjeta válido y saldo pendiente inicial
cuenta = CuentaBancaria(5000, "Juan Perez", tarjeta)

cuenta.consultarSaldo()
cuenta.consultarTitular()

# Realizando operaciones
cuenta.depositar(2000)
cuenta.retirar(1000)
cuenta.realizarPagoTarjeta(500)

# Consultar saldo pendiente de la tarjeta después del pago
print("Saldo pendiente en la tarjeta después del pago:", tarjeta.consultarSaldoPendiente())
