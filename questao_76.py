# Questão 76 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

import traceback
def processar(dados):
    for dado in dados:
        try:
            print(float(dado) * 2)
        except (TypeError, ValueError):
            print("Falha no dado:", dado)
            traceback.print_exc()
processar(["10", "abc", None, "5"])
