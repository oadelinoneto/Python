largura = int(input())
altura = int(input())

savelargura = largura

while altura > 0:
    largura = savelargura
    while largura !=0:
        print('#',end='')
        largura = largura - 1
    else:
        print()
        
    altura = altura - 1            