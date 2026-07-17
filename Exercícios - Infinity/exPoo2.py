class animal:
    def falar(self):
        print("Este animal faz um som genérico.")


class cachorro:
    def falar(self):
        print("O cachorro está latindo")
        print("Au Au")


class gato:
    def falar(self):
        print("O gato está miando.")
        print("Miau")


animal = animal()
cachorro = cachorro()
gato = gato()

animal.falar()
cachorro.falar()
gato.falar()