distancia = int(input())
velocidade = int(input())
tempo = distancia / velocidade # em hora
dias = tempo // 24 # sem resto
o_resto = tempo % 24
dias = int(dias)
o_resto = int(o_resto)
print (f'{dias} dias e {o_resto} horas')