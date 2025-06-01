# separa o numero em centena, dezena e unidade
def separador_numero(numero):
    unidade = numero % 10
    
    numero = numero // 10
    dezena = numero % 10
    
    numero = numero // 10
    centena = numero % 10
    
    return centena, dezena, unidade

#recebe um numero em int e devolve um str do numero em extenso 
def num_para_texto(num):
    if num == 0:
        return 'zero'
    elif num == 1:
        return 'um'
    elif num == 2:
        return 'duas'
    elif num == 3:
        return 'três'
    elif num == 4:
        return 'quatro'
    elif num == 5:
        return 'cinco'
    elif num == 6:
        return 'seis'
    elif num == 7:
        return 'sete'
    elif num == 8:
        return 'oito'
    elif num == 9:
        return 'nove'
    
# checa se o valores são 1 ou diferente de 1 e organiza na suas devidas frases
def numero_extenso(centena, dezena, unidade):
    
    if unidade == 1:
        print_unidades = 'uma unidade'
    else:
        print_unidades = f'{num_para_texto(unidade)} unidades'
        
    if dezena == 1:
        print_dezenas = 'uma dezena'
    else:
        print_dezenas = f'{num_para_texto(dezena)} dezenas'    
    
    if centena == 1:
        print_centenas = 'uma centena'
    else:
        print_centenas = f'{num_para_texto(centena)} centenas'
    
    return print_centenas, print_dezenas, print_unidades

# checa se os valores são zero e retorna a frase organizada em um str
def formatador_de_zeros(centena, dezena, unidade, p_centena, p_dezenas, p_unidades):
    
    if centena == 0 and dezena == 0 and unidade >= 1:
        return (f'{p_unidades}.')
    
    if centena == 0 and dezena >= 1 and unidade == 0:
        return (f'{p_dezenas}.')
    
    if centena >= 1 and dezena == 0 and unidade == 0:
        return (f'{p_centena}.')
    
    if centena == 0 and dezena >= 1 and unidade >= 1:
        return (f'{p_dezenas} e {p_unidades}.')
    
    if centena >= 1 and dezena == 0 and unidade >= 1:
        return (f'{p_centena} e {p_unidades}.')
    
    if centena >= 1 and dezena >= 1 and unidade == 0:
        return (f'{p_centena} e {p_dezenas}.')
    
    if centena >= 1 and dezena >= 1 and unidade >= 1:
        return f'{p_centena}, {p_dezenas} e {p_unidades}.'
    
numero = int(input())

centena, dezena, unidade = separador_numero(numero)
p_centena, p_dezenas, p_unidades = numero_extenso(centena, dezena, unidade)
print(formatador_de_zeros(centena, dezena, unidade, p_centena, p_dezenas, p_unidades))