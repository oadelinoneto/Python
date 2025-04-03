def usuario_escolhe_jogada(n,m):
    vez_jogador = True
     
    while vez_jogador:
        tirar = int(input('Quantas peças você vai tirar?'))
        if tirar > n or tirar >m or tirar <1:
            print('Oops! Jogada inválida! Tente de novo.')
        else:
            vez_jogador = False
            return tirar
    return tirar

def computador_escolhe_jogada(n,m):
    remover = 1
    if n == m:
        return m
    while remover != m:
        if (n - remover) % (m + 1) == 0:
            return remover
        else:
            remover = remover + 1
    return m

def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    
    computador = False
    
    if n % ( m + 1 ) == 0:
        print('Você começa!')
    else:
        print('Computador começa!')
        computador = True
        
        
    while n > 0:
        if computador == True:
            print(f'Agora restam {n} peças no tabuleiro.')
            tirarPC = computador_escolhe_jogada(n,m)
            n = n - tirarPC
            
            if tirarPC == 1:
                print('')
                print('O computador tirou uma peça.')
                if n == 0:
                    break
                
            else:
                print('')
                print(f'O computador tirou {tirarPC} peças.')
                if n == 0:
                    break
        computador = False
                
        if computador == False:
            print(f'Agora restam {n} peças no tabuleiro.')
            tirarUSUARIO = usuario_escolhe_jogada(n,m)
            n = n - tirarUSUARIO
            
            if tirarUSUARIO == 1:
                print('')
                print('Você tirou uma peça.')
                if n == 0:
                    break
                
            else:
                print('')
                print(f'Você tirou {tirarUSUARIO} peças.')
                if n == 0:
                    break
                
        computador = True       
    print('Fim do jogo! O computador ganhou!')

def campeonato():
    rodada = 1
    while rodada <= 3:
        print(f'**** Rodada {rodada} ****')
        partida()
        rodada += 1
    print('**** Final do campeonato! ****')
    print('')
    print('Placar: Você 0 X 3 Computador') 

print('Bem-vindo ao jogo do NIM! Escolha:')
print('') 
print('1 - para jogar uma partida isolada')
print('2 - para jogar um campeonato')
tipoDePartida = int(input())
if tipoDePartida == 1:
    partida()
elif tipoDePartida == 2:
    campeonato()       