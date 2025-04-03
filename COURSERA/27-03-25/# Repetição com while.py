# Repetição com while
n = int(input())
resultado = "não"
while n != 0:
    ultimo1 = n % 10
    novonumero = n // 10
    ultimo2 = novonumero % 10
    n = novonumero
    
    if ultimo2 == ultimo1:
        resultado = "sim"
        break
    else:
        resultado = "não"
print(resultado)    
