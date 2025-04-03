n = int(input())
soma = 0
while n != 0:
    s = n % 10 
    soma = soma + s
    n = n // 10
print(soma)   