def idade(dia_atual,mes_atual,ano_atual,dia_nascimento,mes_nascimento,ano_nascimento):
    idade_atual = ano_atual - ano_nascimento

    if mes_atual < mes_nascimento:
        idade_atual = idade_atual - 1
        
    elif mes_atual == mes_nascimento and dia_atual < dia_nascimento:
        idade_atual = idade_atual - 1

    return idade_atual
 

dia_atual = int(input())
mes_atual = int(input())
ano_atual = int(input())


dia_nascimento = int(input())
mes_nascimento = int(input())
ano_nascimento = int(input())


print(idade(dia_atual,mes_atual,ano_atual,dia_nascimento,mes_nascimento,ano_nascimento))