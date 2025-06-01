def soma_condicional(num, soma):
    if num > 0:
        soma += num % 10
        num = num // 10
    return num, soma

    


def soma_num(num):
    soma = 0

    num , soma = soma_condicional(num, soma)
        
    num , soma = soma_condicional(num, soma)

    num , soma = soma_condicional(num, soma)
    
    num , soma = soma_condicional(num, soma)

    num , soma = soma_condicional(num, soma)
    
    num , soma = soma_condicional(num, soma)

    
        
    return soma



numero = int(input())

if numero <= 0 or numero >= 100000:
    print(-1)
else:
    print(soma_num(numero))