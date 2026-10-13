# Questão 35 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

produtos = {}
for i in range(3):
    nome = input("Produto: ")
    produtos[nome] = int(input("Quantidade: "))
print(produtos)
