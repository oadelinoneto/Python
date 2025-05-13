def masc_femi(txt):
    if txt == 1:
        return "Ilmo Sr."
    else:
        return "Ilma Sra."
    
nome = input().strip()
sexo = int(input())

print(masc_femi(sexo),nome) 