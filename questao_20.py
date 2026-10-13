# Questão 20 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

soma = 0
while True:
    valor = float(input("Valor (0 encerra): "))
    if valor == 0:
        break
    soma += valor
print("Soma:", soma)
