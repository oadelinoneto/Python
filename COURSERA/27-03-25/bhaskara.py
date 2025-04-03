import math
a = int(input())
b = int(input())
c = int(input())
delta = b**2-4*a*c
if delta < 0:
    print("esta equação não possui raízes reais")
    quit()

x = (-b + math.sqrt(delta)) / (2 * a)
y = (-b - math.sqrt(delta)) / (2 * a)

if x == y:
    print(f"a raiz desta equação é {x}")
else:
    if x > y:
        print(f"as raízes da equação são {x} e {y}")
    else:
        print(f"as raízes da equação são {y} e {x}")
