def classificacao(p1, p2, p3, p4, p5):
    contador = 0
    
    if p1 == 's':
        contador = contador + 1
    if p2 == 's':
        contador = contador + 1
    if p3 == 's':
        contador = contador + 1
    if p4 == 's':
        contador = contador + 1
    if p5 == 's':
        contador = contador + 1
        
    return contador
    
    
p1 = input().strip().lower()
p2 = input().strip().lower()
p3 = input().strip().lower()
p4 = input().strip().lower()
p5 = input().strip().lower()

suspeita = classificacao(p1, p2, p3, p4, p5)

if suspeita == 5:
    print('Assassino')
elif suspeita == 3 or suspeita == 4:
    print('Cúmplice')
elif suspeita == 2:
    print('Suspeito')
else:
    print('Inocente')   