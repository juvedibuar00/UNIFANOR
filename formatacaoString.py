# Uso de format() e f-string, para crear un string con un valor de variable
# Uso de la función format() para crear un string con un valor de variable
# Uso de f-string para crear un string con un valor de variable
#
nome = 'Guilherme'
idade = 25
print(f'Seu nome é {nome} e você tem {idade} anos')
print('Seu nome é {} e você tem {} anos'.format(nome, idade))
print('Seu nome é {0} e você tem {1} anos'.format(nome, idade))
print('Seu nome é {1} e você tem {0} anos'.format(idade, nome))
print('Seu nome é {nome} e você tem {idade} anos'.format(nome='Guilherme', idade=25))
