# Questão 78 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

def calcular_media(n1, n2, n3):
    if not (0 <= n1 <= 10 and 0 <= n2 <= 10 and 0 <= n3 <= 10):
        raise ValueError("Notas devem estar entre 0 e 10")
    return (n1 + n2 + n3) / 3
try:
    a = float(input("Nota 1: "))
    b = float(input("Nota 2: "))
    c = float(input("Nota 3: "))
    media = calcular_media(a, b, c)
    print("Média:", media)
    print("Aprovado" if media >= 7 else "Reprovado")
except ValueError as erro:
    print("Erro:", erro)
