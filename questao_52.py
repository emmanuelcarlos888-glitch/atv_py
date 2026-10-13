# Questão 52 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

medicamentos = {}
for i in range(5):
    nome = input("Medicamento: ")
    medicamentos[nome] = int(input("Quantidade: "))
consulta = input("Consultar: ")
if consulta in medicamentos:
    print(medicamentos[consulta])
else:
    print("Não encontrado")
