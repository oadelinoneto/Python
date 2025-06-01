def preço_frutas(morango, maça):
    
    if morango > 5:
        preço_morango = 2.2 * morango
    else:
        preço_morango = 2.5 * morango
    
    if maça > 5:
        preço_maça = 1.5 * maça
    else:
        preço_maça = 1.8 * maça
        
    peso_total = morango + maça
    valor_total = preço_morango + preço_maça
    
    if valor_total > 25 or peso_total > 8:
        desconto = valor_total / 10
        valor_total = valor_total - desconto
        return valor_total
    
    else:
        return valor_total
    
        
        
    

morango = float(input())
maça = float(input())

valor = preço_frutas(morango, maça)
print(f'{valor:.2f}')