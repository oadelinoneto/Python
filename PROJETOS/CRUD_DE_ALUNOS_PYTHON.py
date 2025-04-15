
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
def create_aluno(banco):

    nome = str(input('Digite o nome do aluno: '))
    for aluno in banco:
        if aluno['nome'] == nome:
            print('Esse aluno já está cadastrado')
            return 

        
                             
    idade = int(input('Digite a idade do aluno: '))
    curso = str(input('Digite o curso do aluno: '))
    novo_aluno = {'nome':nome,'idade':idade,'curso':curso}
    
    atualizado = banco.append(novo_aluno)

    print(f"Aluno {novo_aluno['nome']} cadastrado com sucesso")
    
    return atualizado


# LISTAR ALUNOS MAS APENAS O NOME
def lista_alunos(banco):
    for i,aluno in enumerate(banco):
        print(f"{aluno['nome']}, ID = {i}")

# PESQUISAR ALUNO POR NOME
def pesquisar_alunos(banco):
    x = str(input('Digite o nome do aluno a pesquisar: '))
    print('------------')
    
    for aluno in banco:
        
        if aluno['nome'] == x:
            print (f'Aluno {x} encontrando')
            print('--------DADOS-------')
            print(f"nome = {aluno['nome']}")
            print(f"idade = {aluno['idade']}")
            print(f"curso = {aluno['curso']}")
            
            return None
        
    print (f'Aluno {x} não encontrado.')
    return None

# REMOVER ALUNO
def remover_alunos(banco):
    lista_alunos(banco)
    aluno_removido_id = int(input('Digite o ID do aluno a ser removido!'))
    banco.pop(aluno_removido_id)
    return None


#ATUALIZAR DADOS
def update_aluno(banco):
    lista_alunos(banco)
    id = int(input('Digite o ID do aluno a ser alterado: '))
    
    banco[id]['nome'] = str(input('Digite o novo nome: '))
    banco[id]['idade'] = str(input('Digite a nova idade: '))
    banco[id]['curso'] = str(input('Digite o novo curso: '))
    print(f'Aluno ID {id} atualizado!')    
    
    return None

# MAIN
def main():
    rodando = True
    alunos = []    
    while rodando:
        print('-------------------') 
        print('Seja bem vindo ao CRUD de teste de Adelino!')
        print('1 - Cadastrar aluno')
        print('2 - Listar dados alunos')
        print('3 - Remover aluno')
        print('4 - Pesquisar aluno')
        print('5 - Atualizar dados')
        print('6 - Sair')
        print('-----------------')
        
        escolha_valida = True
        
        while escolha_valida :
            try:
                escolha = int(input())
                escolha_valida = False
            except ValueError:
                print('Valor inválido, escolha uma opção válida')
        
            
                
            
        if escolha == 1:
            create_aluno(alunos)

        elif escolha == 2:
            render(alunos)
        elif escolha == 3:
            remover_alunos(alunos)
        elif escolha == 4:
            pesquisar_alunos(alunos)
        elif escolha ==5:
            update_aluno(alunos)
        elif escolha == 6:
            rodando = False
            
    print('Tenha um bom dia!')
            
   

                
main()


# implementar checks para input validos e casos onde alunos tem nome igual