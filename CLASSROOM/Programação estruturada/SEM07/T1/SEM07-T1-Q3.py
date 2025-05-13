def sinal(str):
    if str == 'v':
        return 'Siga'
    
    elif str == 'a':
        return 'Atenção'
    
    elif str == 'e':
        return 'Pare'
    
entrada = input()
entrada = entrada.lower()

print(sinal(entrada))