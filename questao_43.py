# Questão 43 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

matriz = [[5, 8], [3, 10]]
maior = matriz[0][0]
for linha in matriz:
    for valor in linha:
        if valor > maior:
            maior = valor
print(maior)
