def quadrado_retangulo(base,altura):
    if base == altura:
        return True
    
    else:
        return False
    
base = int(input())
altura = int(input())

if quadrado_retangulo(base,altura):
    print('QUADRADO')
else:
    perimetro = (base * 2 ) + (altura * 2)
    area = base * altura
    print(f'{perimetro} - {area}')
    