# Questão 55 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

disciplinas = ("Matemática", "Português")
alunos = {}
quantidade = int(input("Quantidade de alunos: "))
for i in range(quantidade):
    nome = input("Nome: ")
    matematica = float(input("Matemática: "))
    portugues = float(input("Português: "))
    alunos[nome] = [matematica, portugues]
print("Disciplinas:", disciplinas)
for nome, notas in alunos.items():
    media = (notas[0] + notas[1]) / 2
    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
    print(nome, media, situacao)
