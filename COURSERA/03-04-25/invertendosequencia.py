n = 1
lista = []
while n != 0:
    n = int(input('Digite um número:'))
    if n != 0:
        lista.append(n)
    else:
        break
    
for i in lista[::-1]:
    print(i)   