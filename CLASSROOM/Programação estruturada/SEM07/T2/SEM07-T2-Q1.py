def contar_caracteres_conjuge(nome,conjuge):
    return len(nome) + len(conjuge)
def contar_caracteres_nome(nome):
    return len(nome)

nome = input().strip()
casado = int(input())

if casado == 1:
    conjuge = input().strip()
    print(contar_caracteres_conjuge(nome,conjuge))
else:
    print(contar_caracteres_nome(nome))