largura = int(input())
altura = int(input())

savelargura = largura
savealtura = altura

while altura > 0:
    
    if altura == savealtura or altura == 1: # primeira ou ultima linha
        largura = savelargura
        while largura != 0:
            print('#',end='')
            largura = largura - 1

            
    else:
        largura = savelargura # todo o resto
        while largura != 0:
            if largura == savelargura or largura == 1: # primeiro ou ultimo caractere 
                print('#', end='')
                largura = largura - 1
            else:
                print(' ',end='') # todo os resto dos caracteres 
                largura = largura - 1
                
    print()
    altura = altura - 1
    