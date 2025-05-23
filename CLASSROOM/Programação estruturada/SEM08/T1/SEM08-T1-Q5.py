def imc(peso, altura):
    indice = peso / (altura ** 2)
    if indice < 18.5:
        return 'Abaixo do peso'
    elif indice < 25:
        return 'Peso normal'
    elif indice < 30:
        return 'Sobrepeso'
    elif indice < 35:
        return 'Obeso leve'
    elif indice < 40:
        return 'Obeso moderado'
    else:
        return 'Obeso mórbido'

peso = float(input())
altura = float(input())
indice = peso / (altura ** 2)
print(f'{indice:.2f}')
print(imc(peso, altura))