def maior_menor(n1,n2,n3,n4,n5):
    maior = n1
    
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    if n4 > maior:
        maior = n4
    if n5 > maior:
        maior = n5
    
    menor = n1

    if menor > n2:
        menor = n2
    if menor > n3:
        menor = n3
    if menor > n4:
        menor = n4
    if menor > n5:
        menor = n5

    return  maior,menor
    



n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())


maior,menor = maior_menor(n1,n2,n3,n4,n5)

print(maior)
print(menor)