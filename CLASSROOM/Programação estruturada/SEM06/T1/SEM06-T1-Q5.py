def descontado(valor):
    valor_desconto = valor - (valor *(9/100))
    prestacao_5 = valor / 5 
    valor_auemnto = valor + (valor * (17/100))
    aumento_10 = valor_auemnto / 10   
    return valor_desconto,prestacao_5,aumento_10

compra = float(input())
valor_desconto,prestacao_5,aumento_10 = descontado(compra)

print(f'{valor_desconto:.2f}')
print(f'{prestacao_5:.2f}')
print(f'{aumento_10:.2f}')