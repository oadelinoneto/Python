import math

raio = int(input())
comprimento = 2 * (math.pi) * raio
area_circulo = (math.pi) * raio**2
area_esfera = 4 * (math.pi) * raio**2
volume_esfera = (4 / 3) * (math.pi) * raio**3

arredonda1 = round(comprimento,6)
arredonda2 = round(area_circulo,6)
arredonda3 = round(area_esfera,6)
arredonda4 = round(volume_esfera,6)

print(arredonda1)
print(arredonda2)
print(arredonda3)
print(arredonda4)