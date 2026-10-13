# Questão 50 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

alunos = {}
for i in range(5):
    nome = input("Aluno: ")
    alunos[nome] = float(input("Nota: "))
media = sum(alunos.values()) / 5
print("Média da turma:", media)
for nome, nota in alunos.items():
    if nota >= 7:
        print("Aprovado:", nome)
