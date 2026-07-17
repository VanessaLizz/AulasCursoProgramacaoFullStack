class veiculo:
    def movimentar(self):
        print("O veículo está em movimento.")


class carro(veiculo):
    def movimentar(self):
        print("O carro está sendo dirigido.")


class moto(veiculo):
    def movimentar(self):
        print("A moto está sendo acelerada.")


veiculo = veiculo()
carro = carro()
moto = moto()

veiculo.movimentar()
carro.movimentar()
moto.movimentar()