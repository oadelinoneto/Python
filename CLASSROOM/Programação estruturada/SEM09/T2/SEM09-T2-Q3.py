def separador_data(data):
    ano = data % 10000
    data = data // 10000
    
    mes = data % 100
    data = data // 100
    
    dia = data
    return dia, mes, ano
    
def validador_data(dia, mes, ano):
    bissexto = eh_bissexto(ano)
    
    if mes == 2:
        if bissexto == False:
            if dia > 28:
                return False
    
    if ano <= 0:
        return False
    
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 30:
            return False
         
    if mes > 12 or mes <= 0:
        return False 
        
    if dia > 31 or dia <= 0:
        return False
    
    return True
    
def eh_bissexto(ano):
    
    if ano % 4 != 0:
        return False
    
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True

data = int(input())
dia, mes, ano= separador_data(data)

if validador_data(dia, mes, ano):
    print(True)
else:
    print(False)