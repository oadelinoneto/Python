caractere = str(input())
caractere = caractere.lower()

if caractere.isalpha() or caractere in 'aeiou' or caractere.isdigit():
    print(True)
else:
    print(False)