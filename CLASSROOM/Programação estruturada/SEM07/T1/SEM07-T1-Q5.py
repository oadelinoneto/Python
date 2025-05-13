def media(n1,n2,n3):
    
    media = (n1+n2+n3) / 3
    
    if n3 > 8:
        media = media + 1
    
    if media <= 10:
        return media
    else:
        return 10
    

nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

print(media(nota1,nota2,nota3))