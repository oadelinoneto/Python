def mais_recente(data1,data2):
    if data1[2] > data2[2]:
        return True
    elif data1[2] < data2[2]:
        return False
    
    if data1[1] > data2[1]:
        return True
    elif data1[1] < data2[1]:
        return False
    
    if data1[0] > data2[0]:
        return True
    return False

dia_1 = int(input())
mes_1 = int(input())
ano_1 = int(input())
data_1 = [dia_1,mes_1,ano_1]

dia_2 = int(input())
mes_2 = int(input())
ano_2 = int(input())
data_2 = [dia_2,mes_2,ano_2]

if mais_recente(data_1,data_2):
    print(f'{dia_1}/{mes_1}/{ano_1}')
else:
    print(f'{dia_2}/{mes_2}/{ano_2}')