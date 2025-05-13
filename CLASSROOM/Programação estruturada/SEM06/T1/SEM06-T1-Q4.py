def maior(n1,n2,n3,n4,n5):
    lista = [n1,n2,n3,n4,n5]
    variavel = n1
    for n in lista:
        if n >= variavel:
            variavel = n
    return variavel
    
def menor(n1,n2,n3,n4,n5):
    lista = [n1,n2,n3,n4,n5]
    variavel_menor = n1
    for n in lista:
        if n <= variavel_menor:
            variavel_menor = n
    return variavel_menor

def media(n1,n2,n3,n4,n5):
    return (n1+n2+n3+n4+n5) / 5
    

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())   
n5 = int(input())

maior_numero = maior(n1,n2,n3,n4,n5)
menor_menor = menor(n1,n2,n3,n4,n5)
media_numero = media(n1,n2,n3,n4,n5)

print(maior_numero)
print(menor_menor)
print(media_numero)