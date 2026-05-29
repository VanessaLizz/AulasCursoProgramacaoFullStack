def maior_numero(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
resultado = maior_numero(50, 45, 17)
print(f"O maior número entre 50, 45 e 17 é: {resultado}")