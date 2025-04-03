Vou te ajudar a aprender como criar e manipular repositórios usando Git através da linha de comando e Git Bash. Vamos começar com os conceitos básicos e avançar para comandos mais específicos.

# Configuração inicial do Git

Antes de começar a usar o Git, você precisa configurá-lo:

```bash
# Configurar seu nome
git config --global user.name "Seu Nome"

# Configurar seu email
git config --global user.email "seu.email@exemplo.com"
```

# Criando um novo repositório

```bash
# Criar uma nova pasta para seu projeto
mkdir meu-projeto
cd meu-projeto

# Inicializar o repositório Git
git init
```

# Comandos básicos do Git

## Verificando o status

```bash
# Verificar o status atual do repositório
git status
```

## Adicionando arquivos ao stage

```bash
# Adicionar um arquivo específico
git add arquivo.txt

# Adicionar todos os arquivos
git add .
```

## Fazendo commits

```bash
# Fazer commit com mensagem
git commit -m "Mensagem descritiva do commit"
```

## Visualizando histórico

```bash
# Ver histórico de commits
git log

# Visualização mais compacta
git log --oneline
```

## Trabalhando com branches

```bash
# Criar uma nova branch
git branch nova-funcionalidade

# Mudar para uma branch
git checkout nova-funcionalidade

# Criar e mudar para uma nova branch (atalho)
git checkout -b outra-funcionalidade
```

## Mesclando branches

```bash
# Voltar para a branch principal
git checkout main

# Mesclar a branch com a principal
git merge nova-funcionalidade
```

# Trabalhando com repositórios remotos

## Conectando a um repositório remoto

```bash
# Adicionar um repositório remoto
git remote add origin https://github.com/usuario/repositorio.git
```

## Enviando e baixando alterações

```bash
# Enviar alterações para o repositório remoto
git push origin main

# Baixar alterações do repositório remoto
git pull origin main
```

## Clonando um repositório existente

```bash
# Clonar um repositório
git clone https://github.com/usuario/repositorio.git
```

# Comandos úteis adicionais

```bash
# Verificar diferenças entre arquivos
git diff

# Remover arquivos do stage
git reset arquivo.txt

# Desfazer o último commit mantendo as alterações
git reset --soft HEAD~1

# Reverter um arquivo para o estado anterior
git checkout -- arquivo.txt

# Visualizar branches
git branch

# Excluir uma branch
git branch -d nome-da-branch
```

# Fluxo de trabalho típico

1. `git pull` - Atualize seu repositório local
2. Faça mudanças nos arquivos
3. `git status` - Verifique quais arquivos foram modificados
4. `git add .` - Adicione as mudanças ao stage
5. `git commit -m "Descrição"` - Faça commit das mudanças
6. `git push` - Envie as mudanças para o repositório remoto

Quer que eu explique algum desses comandos com mais detalhes ou gostaria de aprender mais sobre algum aspecto específico do Git?