# Questão 39 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

import random
sorteado = random.randint(1, 10)
palpite = int(input("Palpite: "))
if palpite == sorteado:
    print("Acertou!")
else:
    print("Errou! Era", sorteado)
