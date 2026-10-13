# Questão 47 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

matriz = [[1, -2, 3], [-4, 5, 6]]
contador = 0
for linha in matriz:
    for valor in linha:
        if valor > 0:
            contador += 1
print(contador)
