def par_impar(num):
    if num % 2 == 0:
        return True
    else:
        return False


numero = int(input())

if par_impar(numero):
    print(numero + 5)
else:
    print(numero + 8)