def operacoes_com_resto(numero):
    operacao = numero % 5
    
    if operacao == 0:
        return (9 * numero) + 7
    
    elif operacao == 1:
        if numero % 2 == 0:
            return 'par'
        else:
            return 'ímpar'
        
    elif operacao == 2:
        return (5 * numero ** 2) - (3 * numero) + 42
    
    elif operacao == 3:
        return numero // 10
    
    elif operacao == 4:
        return numero ** 2


numero = int(input())

print(operacoes_com_resto(numero))