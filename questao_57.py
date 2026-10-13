# Questão 57 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

def contar(texto, caractere):
    quantidade = 0
    for letra in texto:
        if letra == caractere:
            quantidade += 1
    return quantidade
texto = input("Texto: ")
caractere = input("Caractere: ")
print(contar(texto, caractere))
