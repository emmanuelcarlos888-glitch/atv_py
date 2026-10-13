# Questão 64 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

def somar(a, b, c):
    soma = a + b + c
    if soma > 21 and 11 in (a, b, c):
        soma -= 10
    if soma > 21:
        return -1
    return soma
a = int(input("A (1 a 11): "))
b = int(input("B (1 a 11): "))
c = int(input("C (1 a 11): "))
if 1 <= a <= 11 and 1 <= b <= 11 and 1 <= c <= 11:
    print(somar(a, b, c))
else:
    print("Entrada fora da faixa")
