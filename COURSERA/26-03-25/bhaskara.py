import math
a = float(input())
b = float(input())
c = float(input())
delta = b**2-4*a*c

if delta < 0:
    print("esta equação não possui raízes reais")
    
elif delta == 0:
    x = - b + (math.sqrt(delta)) / 2 * a
    print(f"a raiz desta equação é {x}") 
    
elif delta > 0:
    x = - b + (math.sqrt(delta)) / 2 * a 
    y = - b - (math.sqrt(delta)) / 2 * a
    if y > x:
        print(f"as raízes da equação são {x} e {y}")
    else:
        print(f"as raízes da equação são {y} e {x}")
