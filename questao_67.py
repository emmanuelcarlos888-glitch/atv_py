# Questão 67 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

while True:
    try:
        idade = int(input("Idade: "))
        if idade < 0:
            raise ValueError("Idade negativa")
        print("Idade válida:", idade)
        break
    except ValueError:
        print("Informe uma idade válida")
