def conversao(s):
    minutos = s // 60
    segundos_restantes = s % 60 
    horas = minutos // 60 
    minutos_restantes = minutos % 60 
    return horas,minutos_restantes,segundos_restantes


segundos = int(input())
horas, minutos_restantes, segundos_restantes = conversao(segundos)
print(f'{horas}:{minutos_restantes}:{segundos_restantes}')