def maximo(x,y,z):
    maior = 0
    if x >= y and x >= z:
        return x
    if y >= x and y >= z:
        return y
    if z >= x and z >= y:
        return z 