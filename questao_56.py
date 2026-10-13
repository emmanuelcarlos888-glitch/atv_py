# Questão 56 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

graos = 1
total = 0
for casa in range(64):
    total += graos
    graos *= 2
print("Total de grãos:", total)
