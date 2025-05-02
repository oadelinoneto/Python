caractere = str(input())
caractere = caractere.lower()

if caractere.isalpha() and caractere not in 'aeiou':
    print(True)
else:
    print(False)