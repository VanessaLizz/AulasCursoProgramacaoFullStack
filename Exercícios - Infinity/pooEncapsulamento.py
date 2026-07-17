class contaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"O depósito de R${valor:.2f} foi realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            print(f"O saque de R${valor:.2f} foi realizado com sucesso.")
        else:
            print(f"Saldo insuficiente para saque. Seu saldo é de R${self._saldo:.2f}")

    def exibir_saldo(self):
        print(f"Titular: {self._titular}")
        print(f"Saldo atual: R${self._saldo:.2f}")


conta = contaBancaria("Rhaenyra", 1000)

conta.exibir_saldo()
conta.depositar(500)
conta.sacar(300)
conta.exibir_saldo()

conta2 = contaBancaria("Alicent", 250)
conta2.exibir_saldo()
conta2.depositar(400)
conta2.sacar(1500)
conta2.exibir_saldo()