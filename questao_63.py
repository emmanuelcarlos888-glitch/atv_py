# Questão 63 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

def receber():
    numeros = []
    for i in range(5):
        numeros.append(float(input("Número: ")))
    return numeros
def maior(numeros):
    return max(numeros)
def menor(numeros):
    return min(numeros)
valores = receber()
print("Maior:", maior(valores))
print("Menor:", menor(valores))
