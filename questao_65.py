# Questão 65 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

def calcularCubo(numero):
    return numero ** 3
def calcularDivisaoCubo(numero):
    if numero % 3 == 0:
        return calcularCubo(numero)
    return False
numero = int(input("Número: "))
print(calcularDivisaoCubo(numero))
