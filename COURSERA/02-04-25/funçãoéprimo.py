def éprimo(n):    
    flag = False
    for i in range(2, n):
        if (n % i) == 0:
            flag = True
            break
    return not flag


def n_primos(n):
    contador = 0
    if n < 2:
        return contador
    
    if n == 2:
        contador = contador + 1
        return contador
        
    for i in range(2,n):
        if éprimo(i):
            contador = contador + 1
    return contador

n_primos(6)