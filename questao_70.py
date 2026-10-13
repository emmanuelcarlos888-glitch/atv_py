# Questão 70 - Laboratório de Programação (ADS, 2º período)
# Execute este arquivo individualmente com Python.

def permissao(perfis, perfil, indice):
    try:
        return perfis[perfil][indice]
    except (KeyError, IndexError):
        return "acesso_restrito"
perfis = {"admin": ["ler", "editar"], "usuario": ["ler"]}
print(permissao(perfis, "usuario", 2))
