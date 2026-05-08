import random

def lancar_dados():
    resultado_dado1 = random.randint(1, 6)
    print(f"O resultado do dado 1 é: {resultado_dado1}")
    
    resultado_dado2 = random.randint(1, 6)
    print(f"O resultado do dado 2 é: {resultado_dado2}")
    
    return resultado_dado1 + resultado_dado2

print(f"A soma dos dados é de: {lancar_dados()}")