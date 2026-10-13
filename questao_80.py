# Questão 80 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

class ProdutoInvalidoError(Exception):
    pass
class ValorInvalidoError(Exception):
    pass
class QuantidadeInvalidaError(Exception):
    pass

def registrar_venda(produto, preco, quantidade):
    if produto.strip() == "":
        raise ProdutoInvalidoError("Produto vazio")
    if preco <= 0:
        raise ValorInvalidoError("Preço deve ser positivo")
    if type(quantidade) != int or quantidade <= 0:
        raise QuantidadeInvalidaError("Quantidade inválida")
    return {"produto": produto, "preco": preco,
            "quantidade": quantidade, "total": preco * quantidade}

def salvar_linha(nome_arquivo, texto):
    try:
        with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
            arquivo.write(texto + "\n")
    except OSError as erro:
        print("Erro ao escrever arquivo:", erro)

def gerar_relatorio(vendas):
    if len(vendas) == 0:
        print("Nenhuma venda válida")
        return
    faturamento = 0
    quantidades = {}
    for venda in vendas:
        faturamento += venda["total"]
        nome = venda["produto"]
        if nome in quantidades:
            quantidades[nome] += venda["quantidade"]
        else:
            quantidades[nome] = venda["quantidade"]
    mais_vendido = max(quantidades, key=quantidades.get)
    print("Quantidade de vendas:", len(vendas))
    print("Produto mais vendido:", mais_vendido)
    print("Faturamento: R$", round(faturamento, 2))
    print("Ticket médio: R$", round(faturamento / len(vendas), 2))

vendas = []
while True:
    produto = input("Produto (fim para encerrar): ")
    if produto.lower() == "fim":
        break
    try:
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        venda = registrar_venda(produto, preco, quantidade)
    except (ProdutoInvalidoError, ValorInvalidoError,
            QuantidadeInvalidaError, ValueError) as erro:
        print("Erro:", erro)
        salvar_linha("log_erros.txt", str(erro))
    else:
        vendas.append(venda)
        salvar_linha("vendas.txt", str(venda))
        print("Venda registrada")
    finally:
        print("Tentativa de cadastro finalizada")
gerar_relatorio(vendas)
