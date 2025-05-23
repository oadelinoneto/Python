def maior_que_media(lista):
    media = sum(lista) / 5
    
    maiores = []
    for n in lista:
        if n > media:
            maiores.append(n)
    return maiores


n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
numeros = [n1,n2,n3,n4,n5]

media = sum(numeros) / 5
print(f'{media:.2f}')

maiores = maior_que_media(numeros)
for n in maiores:
    print (f'{n:.2f}')