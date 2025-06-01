def diferença(n1,n2,n3):
    dif1 = abs(n2 - n1) 
    dif2 = abs(n3 - n1)

    
    if dif1 < dif2:
        return dif1
    else:
        return dif2


n1 = int(input())
n2 = int(input())
n3 = int(input())

print(diferença(n1,n2,n3))