def dia_semana(numero):
    numero = int(numero)
    if numero == 1:
        return 'domingo'
    elif numero == 2:
        return 'segunda-feira'
    elif numero == 3:
        return 'terça-feira'
    elif numero == 4:
        return 'quarta-feira'
    elif numero == 5:
        return 'quinta-feira'
    elif numero == 6:
        return 'sexta-feira'
    elif numero == 7:
        return 'sábado'
    else:
        return 'valor inválido'

valor = input().strip()
print(dia_semana(valor))