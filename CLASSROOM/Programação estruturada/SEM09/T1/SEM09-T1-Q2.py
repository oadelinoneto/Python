def operacao(n1,n2,operador):
    if operador == 1:
        return n1 + n2
    
    elif operador == 2:
        return n1 - n2
    
    elif operador == 3:
        return n1 * n2
    
    elif operador == 4:
        return n1 / n2

n1 = float(input())
n2 = float(input())
operador = int(input())

print(operacao(n1,n2,operador))