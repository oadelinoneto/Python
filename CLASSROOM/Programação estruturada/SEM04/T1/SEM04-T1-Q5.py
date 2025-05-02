altura = float(input())
comprimento = float(input())
largura = float(input())

area_piso = largura * comprimento
volume_sala = largura * comprimento * altura
area_das_paredes = 2 * altura * largura + 2 * altura * comprimento

print(area_piso)
print(volume_sala)
print(area_das_paredes)