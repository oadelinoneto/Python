def maior_elemento(n):
    maior = 0
    for i in n:
        if i >= maior:
            maior = i
    return maior
