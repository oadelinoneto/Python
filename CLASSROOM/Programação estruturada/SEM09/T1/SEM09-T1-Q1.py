def similaridade(n1,n2,n3):
    if (n1 == n2 and n2 == n3):
        return 'Todos os valores são iguais'
    elif (n1 != n2 and n2 != n3 and n1 != n3):
        return 'Todos os valores são diferentes'
    elif (n1 == n2 and n1 != n3) or (n1 == n3 and n1 != n2) or (n2 == n3 and n2 != n1):
        return 'Existem dois valores iguais e um diferente'

n1 = int(input())
n2 = int(input())
n3 = int(input())

print(similaridade(n1,n2,n3))