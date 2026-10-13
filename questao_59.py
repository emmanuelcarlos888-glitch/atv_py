# Questão 59 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

def comparar(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    return max(a, b)
a = int(input("Primeiro: "))
b = int(input("Segundo: "))
print(comparar(a, b))
