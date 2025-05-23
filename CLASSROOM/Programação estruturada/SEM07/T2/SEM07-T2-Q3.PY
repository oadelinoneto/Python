def digitos_impar(numero):
    loops = len(str(numero))
    lista = []
    
    for num in range(loops):
        num = numero % 10
        lista.append(num)
        numero = numero // 10
    
    contador = 0
    
    for num in lista:
        if num % 2 != 0:
            contador = contador + 1
            
    return contador 

numero = int(input())
impares = digitos_impar(numero)

if impares == 0:
    print('Nenhum dígito é ímpar.')
elif impares == 1:
    print('Apenas um dígito é ímpar.')
elif impares == 2:
    print('Os dois dígitos são ímpares.')
