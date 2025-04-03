import math
def éPrimo(k):
    primo = True                                                                                                  
    for i in range(2, int(math.sqrt(k))+1):
        if k % i == 0:
            primo = False
            return primo
    return primo

def maior_primo(x):
    for i in range(x,1,-1):
        if éPrimo(i) == True:
            return i

