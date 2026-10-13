# Questão 69 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

try:
    with open("relatorio_vendas.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print("Arquivo não encontrado")
finally:
    print("Recurso encerrado")
