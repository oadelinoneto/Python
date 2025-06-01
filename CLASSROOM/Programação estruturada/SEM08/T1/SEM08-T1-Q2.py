def mais_recente(dia_1,mes_1,ano_1,dia_2,mes_2,ano_2):

    if ano_1 > ano_2:
        return True
    elif ano_1 < ano_2:
        return False
    
    if mes_1 > mes_2:
        return True
    elif mes_1 < mes_2:
        return False
    
    if dia_1 > dia_2:
        return True
    return False

dia_1 = int(input())
mes_1 = int(input())
ano_1 = int(input())


dia_2 = int(input())
mes_2 = int(input())
ano_2 = int(input())

if mais_recente(dia_1,mes_1,ano_1,dia_2,mes_2,ano_2):
    print(f'{dia_1}/{mes_1}/{ano_1}')
else:
    print(f'{dia_2}/{mes_2}/{ano_2}')