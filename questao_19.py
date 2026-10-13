# Questão 19 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

numero = int(input("Número: "))
if numero < 0:
    print("Número inválido")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print("Fatorial:", fatorial)
