# Questão 49 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

alunos = {}
for i in range(5):
    nome = input("Aluno: ")
    alunos[nome] = float(input("Nota: "))
for nome, nota in alunos.items():
    print(nome, nota)
