# Questão 73 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

precos = ["100", "250", "abc", "80"]
for preco in precos:
    try:
        valor = float(preco)
    except ValueError:
        print("Preço inválido:", preco)
    else:
        print("Com desconto:", valor * 0.90)
