# Gera um tabuleiro novo
def tabuleiro_novo():
          
    tabuleiro = [[' ',' ',' '],
                 [' ',' ',' '], 
                 [' ',' ',' ']]
    
    return tabuleiro

# Mostra o tabuleiro               
def render(tabuleiro):
    print('')
    print('   0    1    2 ')
    y = 0
    for i in tabuleiro:
        print(y, end='')
        print(i, sep='\n')
        y += 1 
    print('')

# Recebe o movimento
def get_move():
    move = False
    while not move:
        x = int(input("What is your move's X co-ordinate?: "))
        y = int(input("What is your move's Y co-ordinate?: "))
        if x > 2 or y > 2:
            print('Movimento invalido')
        else:
            move = True
    return [x,y]

# Quem começa
def escolher_player():        
    player = int(input('Digite 1 para X e 2 para O: '))
    if player == 1:
        return 'X'
    elif player == 2:
        return 'O'

# Função que alterna entre os jogadores
def current_player(player):
    if player == 'X':
        return 'O'
    else:
        return 'X'

# Função que faz a alteração no tabuleiro e devolve          
def make_move(board, move_coords, player):
    x, y = move_coords
    board[x][y] = player
    return board    

# Determina se o movimento é válido checando se a coordenada escolhida já tem um X ou Y
def is_valid(board,move_coords):
    x,y = move_coords
    if board[x][y] == 'X' or board[x][y] == 'O':
        return False
    return True

# Checa se is_draw e get_winner é true, se forem retorna true else retorna false
def win_conditions(board,player):
    
    if get_winner(board):
        print(f'O jogador {player} venceu!')
        print(board)
        return True
    
    elif is_draw(board):
        print('O jogo empatou!')
        return True
    
    else:
        return False   
        
# Determina se é impate
def is_draw(board):
    for i in board:
        if ' ' in i:
            return False
    return True
                 
# Função que chama as funções win_
def get_winner(board):
    if win_colunas(board) or win_diagonal_esquerda_pra_direita(board) or win_linhas(board) or win_direita_pra_esquerda(board):
        return True
    else:
        return False

# Funções win_ para determinar se há combinação vitoriosa     
def win_colunas(board):
    for j in range(3):
        coluna_0 = []
        for i in range(3):
            davez = board[i][j]
            coluna_0.append(davez)

        contadorX = 0
        contadorY = 0
        for i in coluna_0:
            if i == 'X':
                contadorX += 1
            elif i == 'O':
                contadorY += 1

        if contadorX == 3 or contadorY == 3:
            return True
    return False   
     
def win_linhas(board):  
    for i in board:
        linha_0 = []
        for j in i:
            if j == 'X' or j == 'O':
                davez = j
                linha_0.append(davez)
            else:
                linha_0.append('')

        contadorX = 0
        contadorY = 0
        for i in linha_0:
            if i == 'X':
                contadorX += 1
            elif i == 'O':
                contadorY += 1

        if contadorX == 3 or contadorY == 3:
            return True
    return False

def win_diagonal_esquerda_pra_direita(board):
    diagonal_0 = []
    x = 0
    y = 0
    while x < 3 and y < 3:
        temp = board[x][y]
        if temp == 'X' or temp == 'O':
            diagonal_0.append(temp)
        else:
            diagonal_0.append('')
        x = x + 1
        y = y + 1

    contadorX = 0
    contadorY = 0
    for i in diagonal_0:
        if i == 'X':
            contadorX += 1
        elif i == 'O':
            contadorY += 1

    if contadorX == 3 or contadorY == 3:
        return True
    return False
      
def win_direita_pra_esquerda(board):
    diagonal_0 = []
    x = 0
    y = 2
    while x <= 2 and y >= 0:
        temp = board[x][y]
        if temp == 'X' or temp == 'O':
            diagonal_0.append(temp)
        else:
            diagonal_0.append('')
        x = x + 1
        y = y - 1

    contadorX = 0
    contadorY = 0
    for i in diagonal_0:
        if i == 'X':
            contadorX += 1
        if i == 'O':
            contadorY += 1
    if contadorX == 3 or contadorY == 3:
        return True
    return False

def computer_play(board):
    for x in range(0,3):  # x = 0
        for y in range(0,3): # y = 0
            jogada_teste = [x,y]
            if is_valid(board,jogada_teste):
                return [x,y]
                                
def main_ia():
    tabuleiro = tabuleiro_novo()
    player = escolher_player()
    vitoria = False
    turno_ia = False
    
    while not vitoria:
        
        while not turno_ia:
            valido = False
            
            while not valido:
                
                print('Seu turno!')
                render(tabuleiro)
                move = get_move()
                if not is_valid(tabuleiro,move):
                    print('Movimento ilegal, tente outra jogada!')
                    print('')
                else:
                    valido = True
                    
            tabuleiro = make_move(tabuleiro, move, player)
            render(tabuleiro)
            turno_ia = True
            
        venceu = win_conditions(tabuleiro,player)
        if venceu:
            vitoria = True
            break
            
        while turno_ia:
            print('Turno do computador!')
            print('---------------------')
            player = current_player(player)
            move_ia = computer_play(tabuleiro)
            tabuleiro = make_move(tabuleiro, move_ia, player)
            render(tabuleiro)
            print('---------------------')
            
            venceu = win_conditions(tabuleiro,player)
            
            if venceu:
                vitoria = True
                break

            player = current_player(player)
            turno_ia = False
                
def main():
    tabuleiro = tabuleiro_novo()
    player = escolher_player()
    vitoria = False
    
    
    while vitoria == False:
        
        valido = False
        
        while not valido:
            render(tabuleiro)
            move = get_move()
            if not is_valid(tabuleiro,move):
                print('Movimento ilegal, tente outra jogada!')
                print('')
            else:
                valido = True
                
        tabuleiro = make_move(tabuleiro, move, player)
        
        venceu = win_conditions(tabuleiro,player)
        if venceu:
            vitoria = True
                    
        else:
            player = current_player(player)
        
main()