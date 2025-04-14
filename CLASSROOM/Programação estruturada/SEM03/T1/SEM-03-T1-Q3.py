doces_produzidos = int(input())
pacotes_disponiveis = int(input())
doce_caixa = doces_produzidos // pacotes_disponiveis

if doce_caixa < 1: # não dá pra ter menos de 1 doce por caixa 
    pass
else:
    print (doce_caixa)