def maior_menor(lista):
    maior = lista[0]
    for n in lista:
        if n >= maior:
            maior = n
    
    menor = lista[0]
    for n in lista:
        if n <= menor:
            menor = n
            
    return maior,menor
        



n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
numeros = [n1,n2,n3,n4,n5]

maior,menor = maior_menor(numeros)
print(maior)
print(menor)