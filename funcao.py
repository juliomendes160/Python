# 1. O que são funções e por que utilizá-las?

# Funções que já utilizamos anteriormente...

"""
    print() # - Imprimi uma mensagem (int, float, str) mp console (terminal, cmd)
    input # - Retorna um dado informado pelo usuário (entrada padrão) e pode receber uma string
    len() # - Recebe uma lista e retorna o tamanho dessa lista
    max() # - Retorna o maior valor de uma lista
"""

# 2. Criação de Funções

# Função inicial

def saudacao():
    print('Seja bem vinda(o)!')
    print('Olá, é um prazer ter você fazendo parte desse curso!')

saudacao()
saudacao()
saudacao()

# Função com parâmetros

def saudacao(nome, curso):
    print(f'Seja bem vinda(o)!, {nome}!')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao('Walisson', 'Python')
saudacao('Aline', 'JavaScript')

# Função com parâmetro default

def saudacao(nome, curso='Python'):
    print(f'Seja bem vinda(o)!, {nome}!')
    print(f'Olá, é um prazer ter fazendo parte desse curso de {curso}!')

saudacao('Walisson', 'C++')

# Funções com retorno

def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 2)

def calculadora(num1, num2, operacao='+'):
    if operacao == '(+)':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2

resultado = calculadora(10, 20)

print(resultado)
    

