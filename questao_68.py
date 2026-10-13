# Questão 68 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

try:
    lucros = float(input("Lucros: "))
    acionistas = int(input("Acionistas: "))
    print("Por acionista:", lucros / acionistas)
except ZeroDivisionError:
    print("Não é possível dividir por zero")
except ValueError:
    print("Digite números válidos")
