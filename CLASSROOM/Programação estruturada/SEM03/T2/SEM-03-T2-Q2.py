try:
    preço = float(input())
except:
    preço = 0.0
    
preço_desconto = preço * 0.90
print(f'{preço_desconto:.2f}')