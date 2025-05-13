def tipo(str):
    if str in 'aeiou':
        return 'vogal'
    
    elif str.isalpha() and str not in 'aeiou':
        return 'consoante'
    
    elif str.isnumeric():
        return 'número'
    
    elif not str.isalpha() and not str.isnumeric():
        return 'símbolo'
    
entrada = input()
entrada = entrada.lower()
print(tipo(entrada))
