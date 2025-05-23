pontos = 0

print('''
Q1 - Qual o animal mais pesado do mundo?
a - macaco
b - baleia azul
c - elefante      
      ''')
resposta = input().lower()

if resposta == 'a':
    print('Errado :( ')
elif resposta == 'b':
    print('Correto! :)')
    pontos += 1
elif resposta == 'c':
    print('Errado :(')
else:
    print('Você não escolheu a, b ou c :(')

print('''
Q2 - Qual é a capital do Brasil?
a - São Paulo
b - Rio de Janeiro
c - Brasília
      ''')
resposta = input().lower()

if resposta == 'a':
    print('Errado :( ')
elif resposta == 'b':
    print('Errado :( ')
elif resposta == 'c':
    print('Correto! :)')
    pontos += 1
else:
    print('Você não escolheu a, b ou c :(')

print('''
Q3 - Quanto é 5 + 3?
a - 6
b - 8
c - 10
      ''')
resposta = input().lower()

if resposta == 'a':
    print('Errado :( ')
elif resposta == 'b':
    print('Correto! :)')
    pontos += 1
elif resposta == 'c':
    print('Errado :(')
else:
    print('Você não escolheu a, b ou c :(')

print('''
Q4 - Qual é o maior planeta do sistema solar?
a - Terra
b - Júpiter
c - Marte
      ''')
resposta = input().lower()

if resposta == 'a':
    print('Errado :( ')
elif resposta == 'b':
    print('Correto! :)')
    pontos = pontos + 1 
elif resposta == 'c':
    print('Errado :(')
else:
    print('Você não escolheu a, b ou c :(')

print(f'Você acertou {pontos} perguntas!')
if pontos == 4:
    print('Muito bem!')
else:
    print('Tente novamente!')