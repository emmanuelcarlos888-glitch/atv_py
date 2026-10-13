# Questão 77 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

def realizar_saque(saldo, valor_saque):
    if valor_saque <= 0:
        raise ValueError("Saque deve ser positivo")
    if valor_saque > saldo:
        raise ValueError("Saldo insuficiente")
    return saldo - valor_saque
try:
    saque = float(input("Valor do saque: "))
    print("Novo saldo:", realizar_saque(1000, saque))
except ValueError as erro:
    print("Erro:", erro)
