def celsius_fahrenheit(c):
    fahrenheit = (c * ( 9 / 5 ) ) + 32 
    return fahrenheit

celsius = float(input())
convertido = celsius_fahrenheit(celsius)

print(f'{convertido:.2f}')