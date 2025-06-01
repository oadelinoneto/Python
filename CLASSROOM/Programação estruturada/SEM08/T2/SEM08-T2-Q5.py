def media_conceito(n1,n2,n3,media):
    media_final = (n1 + (n2 * 2) + (n3 * 3) + media) / 7
    
    return media_final

def which_conceito(media_final):
    if media_final < 4.0:
        return ('E','Reprovado')     
    elif media_final >= 4.0 and media_final < 6.0:
        return ('D','Reprovado')
    elif media_final >= 6.0 and media_final < 7.5:
        return ('C','Aprovado')
    elif media_final >= 7.5 and media_final < 9.0:
        return ('B','Aprovado')
    else:
        return ('A','Aprovado')


matricula = input()
n1 = float(input())
n2 = float(input())
n3 = float(input())
media_exerc = float(input())

print(matricula)
media_final = media_conceito(n1,n2,n3,media_exerc)

print(f'{media_final:.2f}')

nota, conceito = which_conceito(media_final)
print(nota)
print(conceito)