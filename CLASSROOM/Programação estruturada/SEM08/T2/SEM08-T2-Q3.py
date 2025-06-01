def fizz_buzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FIZZBUZZ'
    elif num % 3 == 0:
        return 'FIZZ'
    elif num % 5 == 0:
        return 'BUZZ'
    else:
        return num
    
numero = int(input())
print(fizz_buzz(numero))