def preço_total(p1,p2):
    return (p1 * 3) + (p2 * 2)

preço1 = float(input())
preço2 = float(input())
preço_final = preço_total(preço1,preço2)

print(f'{preço_final:.2f}')