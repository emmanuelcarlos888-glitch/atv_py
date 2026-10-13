# Questão 40 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

import random
sorteado = random.randint(1, 10)
while True:
    palpite = int(input("Palpite: "))
    if palpite == sorteado:
        print("Acertou!")
        break
    elif palpite < sorteado:
        print("É maior")
    else:
        print("É menor")
