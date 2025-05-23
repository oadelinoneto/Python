def idade(atual,nascimento):
    anos = atual[2] - nascimento[2]
    
    if atual[1] < nascimento[1]:
        anos = anos - 1
    elif atual[1] == nascimento [1] and atual[0] < nascimento[0]:
        anos = anos - 1
    
    return anos


dia_atual = int(input())
mes_atual = int(input())
ano_atual = int(input())
data_atual = [dia_atual,mes_atual,ano_atual]

dia_nascimento = int(input())
mes_nascimento = int(input())
ano_nascimento = int(input())
data_nascimento = [dia_nascimento,mes_nascimento,ano_nascimento]

print(idade(data_atual,data_nascimento))