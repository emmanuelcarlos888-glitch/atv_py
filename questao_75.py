# Questão 75 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

def conectar():
    raise ConnectionError("Falha simulada")
def tentar_conexao():
    for tentativa in range(1, 4):
        try:
            conectar()
            print("Conectado")
            return
        except ConnectionError:
            print("Falha na tentativa", tentativa)
    print("Não foi possível conectar")
tentar_conexao()
