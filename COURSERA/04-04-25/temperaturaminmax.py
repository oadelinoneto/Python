def temperaturaminman(n):
    print(f'A temperatura minima é {minima(n)}')
    print(f'A temperatura maxima é {maxima(n)}')

def minima(n):
    minimo = n[0]
    for i in n:
        if i <= minimo:
            minimo = i
    return minimo

def maxima(n):
    maxima = n[0]
    for i in n:
        if i >= maxima:
            maxima = i
    return maxima