# Questão 74 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

def consultar_produto(codigo):
    produtos = {1: "Notebook", 2: "Mouse"}
    try:
        return 200, produtos[codigo]
    except KeyError:
        return 404, "Produto não encontrado"
    except Exception:
        return 500, "Erro interno"
try:
    codigo = int(input("ID: "))
    print(consultar_produto(codigo))
except ValueError:
    print(400, "ID inválido")
