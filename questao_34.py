# Questão 34 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

notas = {"Ana": 9, "Carlos": 7.5, "Pedro": 6}
nome = input("Nome: ")
if nome in notas:
    print(notas[nome])
else:
    print("Aluno não encontrado")
