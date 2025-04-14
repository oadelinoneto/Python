
# Armazene os dados numa lista de dicionários

# Cada aluno deve ter: nome, idade, curso
# {'nome':'X','idade':'X','curso':'X'}

# CRUD DE TERMINAL COM AS FUNÇÕES CREATE, READ, UPDATE E DELETE
# 1 - Cadastrar aluno
# 2 - Listar alunos          Nesse formato
# 3 - Remover aluno
# 4 - Sair
# Funcionalidades:

# ARMAZENAMENTO 


# FUNÇÃO RECEBE A LISTA TOTAL DE ALUNOS E PRINTA TODOS 
def render(banco):
    for aluno in banco:
        print('-------------')
        for key,value in aluno.items():
            print(f'{key} = {value}')
        print('-------------')
        
# CADASTRAR NOVO ALUNO
def update_aluno(banco):
    nome = str(input('Digite o nome do aluno: '))
    idade = int(input('Digite a idade do aluno: '))
    curso = str(input('Digite o curso do aluno: '))
    novo_aluno = {'nome':nome,'idade':idade,'curso':curso}
    atualizado = banco.append(novo_aluno)
    return atualizado

# LISTAR ALUNOS MAS APENAS O NOME
def lista_alunos(banco):
    for i,aluno in enumerate(banco):
        print(f"{aluno['nome']}, ID = {i}")

# PESQUISAR ALUNO POR NOME
def pesquisar_alunos(banco):
    x = str(input('Digite o nome do aluno a pesquisar: '))
    for aluno in banco:
        if aluno['nome'] == x:
            print (f'Aluno {x} encontrando')
            return None
        
    print (f'Aluno {x} não encontrado.')
    return None

# REMOVER ALUNO
def remover_alunos(banco):
    lista_alunos(banco)
    aluno_removido_id = int(input('Digite o ID do aluno a ser removido!'))
    banco.pop(aluno_removido_id)
    return None

# MAIN
def main():
    rodando = True
    alunos = []    
    while rodando:
        
        print('Seja bem vindo ao CRUD de teste de Adelino!')
        print('1 - Cadastrar aluno')
        print('2 - Listar alunos')
        print('3 - Remover aluno')
        print('4 - Sair')
        
        escolha = int(input())
        if escolha == 1:
            update_aluno(alunos)
            render(alunos)
        elif escolha == 2:
            render(alunos)
        elif escolha == 3:
            remover_alunos(alunos)
        elif escolha == 4:
            rodando == False
            break
            
    print('Tenha um bom dia!')
            
                
main()


# implementar checks para input validos e casos onde alunos tem nome igual