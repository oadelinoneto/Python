def signo(d, m):
    if m == 3 and d >= 21 or m == 4 and d <= 19:
        return 'Áries'
    elif m == 4 and d >= 20 or m == 5 and d <= 20:
        return 'Touro'
    elif m == 5 and d >= 21 or m == 6 and d <= 21:
        return 'Gêmeos'
    elif m == 6 and d >= 22 or m == 7 and d <= 22:
        return 'Câncer'
    elif m == 7 and d >= 23 or m == 8 and d <= 22:
        return 'Leão'
    elif m == 8 and d >= 23 or m == 9 and d <= 22:
        return 'Virgem'
    elif m == 9 and d >= 23 or m == 10 and d <= 22:
        return 'Libra'
    elif m == 10 and d >= 23 or m == 11 and d <= 21:
        return 'Escorpião'
    elif m == 11 and d >= 22 or m == 12 and d <= 21:
        return 'Sagitário'
    elif m == 12 and d >= 22 or m == 1 and d <= 19:
        return 'Capricórnio'
    elif m == 1 and d >= 20 or m == 2 and d <= 18:
        return 'Aquário'
    elif m == 2 and d >= 19 or m == 3 and d <= 20:
        return 'Peixes'

dia = int(input())
mes = int(input())
print(signo(dia,mes))