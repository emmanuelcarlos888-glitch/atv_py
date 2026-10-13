# Questão 71 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

class SaldoInsuficienteError(Exception):
    pass
def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente")
    return saldo - valor
try:
    print("Novo saldo:", sacar(1000, float(input("Saque: "))))
except SaldoInsuficienteError as erro:
    print(erro)
