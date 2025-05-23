def digitos_par(numero):
    loops = len(str(numero))
    lista = []
    
    for num in range(loops):
        num = numero % 10
        lista.append(num)
        numero = numero // 10
    
    contador = 0
    
    for num in lista:
        if num % 2 == 0:
            contador = contador + 1
            
    return contador 

numero = int(input())
print(digitos_par(numero))