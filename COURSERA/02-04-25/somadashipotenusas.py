def hipotenusatrue(h):
    for i in range(1,h): 
        for j in range(1,h): # j 
            if i**2 + j**2 == h**2: # testa combinações que dão o numero h^2
                return True # retorna true se a combinação for valida
    return False
    
def soma_hipotenusas(h):
    contador = 0
    for i in range (1, h+1): #  
        if  hipotenusatrue(i) == True: # se a combinação for uma soma de cateto válida soma a hipotenusa
            contador = contador + i
    return contador

