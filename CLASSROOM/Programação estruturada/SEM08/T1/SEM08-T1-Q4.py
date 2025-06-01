def maior_que_media(n, media):
    if n > media:
        return True
    else:
        return False
    
    
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

media = (n1 + n2 + n3 + n4 + n5) / 5
print(f'{media:.2f}')
if maior_que_media(n1,media):
    print(n1)
    
if maior_que_media(n2,media):
    print(n2)
    
if maior_que_media(n3,media):
    print(n3)
    
if maior_que_media(n4,media):
    print(n4)
    
if maior_que_media(n5,media):
    print(n5)    