def peso_ideal(altura,sexo):
    if sexo == 1:
        melhor = (72.7 * altura) - 58
        return (melhor)
    else:
        melhor = (62.1 * altura) - 44.7
        return (melhor)
    
altura = float(input())
sexo = int(input())

melhor_peso = peso_ideal(altura,sexo)
print(f'{melhor_peso:.2f}')