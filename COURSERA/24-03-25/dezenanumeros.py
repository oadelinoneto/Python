numero = int(input("Digite um número inteiro: "))
numerosemunidade = numero // 10 # retirando a casa da unidade, de forma que a anterior casa da dezena vira unidade // ex 1757 // 10 = 175 (o resto é eliminado)
dezena = numerosemunidade % 10 # dividindo por 10 novamente, dessa vez obtendo só o resto // ex : 175 % 10 = 5
print(f"O dígito das dezenas é {dezena}")