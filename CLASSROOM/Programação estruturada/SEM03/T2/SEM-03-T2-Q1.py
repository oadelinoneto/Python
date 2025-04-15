import math
PI = 3.141592

try:
    raio = float(input())
except:
    raio = 0.0
    
comprimento = 2 * PI * raio
area_circulo = PI * raio**2
area_esfera = 4 * PI * raio**2
volume_esfera = (4 / 3) * PI * raio**3

print(f'{comprimento:.6f}')
print(f'{area_circulo:.6f}')
print(f'{area_esfera:.6f}')
print(f'{volume_esfera:.6f}')