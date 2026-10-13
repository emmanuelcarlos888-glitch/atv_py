# Questão 72 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

def parse_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        raise ValueError("CPF deve ter 11 dígitos")
    return cpf
def main():
    try:
        print(parse_cpf(input("CPF: ")))
    except ValueError as erro:
        print(erro)
main()
