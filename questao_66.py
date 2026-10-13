# Questão 66 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

def calcular_animais():
    for coelhos in range(36):
        galinhas = 35 - coelhos
        if 4 * coelhos + 2 * galinhas == 94:
            print("Coelhos:", coelhos)
            print("Galinhas:", galinhas)
calcular_animais()
