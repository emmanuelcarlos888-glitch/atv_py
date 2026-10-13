# Questão 62 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

def perfeito(numero):
    soma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            soma += divisor
    return numero > 0 and soma == numero
numero = int(input("Número: "))
print("É perfeito?", perfeito(numero))
