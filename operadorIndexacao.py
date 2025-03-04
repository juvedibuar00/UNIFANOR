# Operadores de indexação
# Os operadores de indexação são usados para acessar elementos em uma sequência, como uma string, lista ou tupla.
# O operador de indexação é o símbolo de colchete [].
# O operador de indexação é usado para acessar um elemento em uma sequência, especificando sua posição.
# O índice de um elemento em uma sequência começa em 0.
# Exemplo de uso do operador de indexação: my_list = [1, 2, 3], my_list[0] retorna 1.
print("-----------------Outros operadores-----------------")
nome = 'Guilherme'
# nome é variável do tipo string, que recebe o valor 'Guilherme'.
print(nome[0]) # imprime 'G'
# [0] é o índice do primeiro elemento da sequência.
print(nome[-1]) # imprime 'E'
# [-1] é o índice do último elemento da sequência.
print(nome[1:3]) # imprime 'ui'
# [1:3] é o índice dos elementos da posição 1 até a posição 3.
print(nome[1:]) # imprime 'uilherme'
# O índice 1: significa que estamos acessando os elementos da posição 1 até o final da sequência.
print(nome[:3]) # imprime 'Gui'
# O índice :3 significa que estamos acessando os elementos do início da sequência até a posição 3.
print(nome[:]) # imprime 'Guilherme'
# O índice : significa que estamos acessando todos os elementos da sequência.
print(nome[1:6:2]) # imprime 'uil'  # imprime 'Gie'
# O índice 1:6:2 significa que estamos acessando os elementos da posição 1 até a posição 6, com um passo de 2.
print(nome[1::2]) # imprime 'uilhe'
# 1::2 significa que estamos acessando os elementos da posição 1 até o final da sequência, com um passo de 2.
print(nome[::2]) # imprime 'Gulherme'
# ::2 significa que estamos acessando os elementos do início da sequência até o final, com um passo de 2.
print(nome[::-1]) # imprime 'emrehliuG'
# -1 significa que estamos acessando os elementos da sequência em ordem inversa.
print(nome[::-2]) # imprime 'erhig'
# -2 significa que estamos acessando os elementos da sequência em ordem inversa, com um passo de 2.


print("-----------------Fim operadores.py-----------------")
