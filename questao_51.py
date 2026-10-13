# Questão 51 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

temperaturas = []
for dia in range(5):
    temperaturas.append(float(input("Temperatura: ")))
media = sum(temperaturas) / 5
print("Temperaturas:", temperaturas)
print("Média:", media)
if 18 <= media <= 28:
    print("Faixa ideal")
else:
    print("Fora da faixa ideal")
