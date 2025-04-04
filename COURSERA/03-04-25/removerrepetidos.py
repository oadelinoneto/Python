def remove_repetidos(n):
    lista = n
    listanova = []
    for i in lista:
        if i  not in listanova:
            listanova.append(i)
    listanova.sort()
    return listanova
            
