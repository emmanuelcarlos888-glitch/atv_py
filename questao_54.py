# Questão 54 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

vagas = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
ocupadas = 0
livres = 0
for linha in vagas:
    for vaga in linha:
        if vaga == 1:
            ocupadas += 1
        else:
            livres += 1
print("Ocupadas:", ocupadas)
print("Livres:", livres)
