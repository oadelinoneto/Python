numerosSegundos = int(input())
dia = numerosSegundos // 86400 # segundos para dia sem o resto
diaResto = numerosSegundos % 86400 # obtendo os segundos não convertidos para dias
horas = diaResto // 3600 # convertendo segundos restantes em horas
horaResto = diaResto % 3600 # obtendo as horas restantes da operação anterior
minutos = horaResto // 60 # transformando as horas restantes em minutos
segundos = horaResto % 60 # obtendo os segundos restantes da operação anterior 
print(f"{dia} dias,{horas} horas,{minutos} minutos e {segundos} segundos.")