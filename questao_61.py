# Questão 61 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

def inverter(texto):
    return texto[::-1]
textos = ["python2023", "0203programacao2023", "luz azul", "arara rara", "anotaram a data da maratona"]
for texto in textos:
    print(inverter(texto))
