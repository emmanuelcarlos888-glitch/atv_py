# Questão 79 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

def cadastrar_produto(nome, preco, quantidade):
    if nome.strip() == "":
        raise ValueError("Nome vazio")
    if preco <= 0:
        raise ValueError("Preço inválido")
    if quantidade < 0:
        raise ValueError("Quantidade negativa")
    return "Produto cadastrado com sucesso"
try:
    nome = input("Produto: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))
    print(cadastrar_produto(nome, preco, quantidade))
except ValueError as erro:
    print("Erro:", erro)
