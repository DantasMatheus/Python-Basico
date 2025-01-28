# Escreva um programa para exibir na tela o nome e a categoria de um lutador. O programa deve ler
# um string para o nome e um número real para o peso. Conforme o peso ocorrerá o enquadramento
# na categoria, segundo esta tabela (fictícia):

# Peso ------------------------------------- Categoria
# menor que 52 ----------------------------- invalido
# maior ou igual a 52 e menor que 65 ------- pena
# maior ou igual a 65 e menor que 72 ------- leve
# maior ou igual a 72 e menor que 79 ------- ligeiro
# maior ou igual a 79 e menor que 86 ------- meio-medio
# maior ou igual a 86 e menor que 90 ------- medio
# maior ou igual a 90 e menor que 100 ------ meio-pesado
# maior ou igual a 100 --------------------- pesado

nome = input('Digite o nome do lutador: ')
peso = float(input('Digite o peso do lutador: '))

if peso < 52:
    cat = ''
elif peso < 65:
    cat = 'Pena'
elif peso < 72:
    cat = 'Leve'
elif peso < 79:
    cat = 'Ligeiro'
elif peso < 86:
    cat = 'Meio-médio'
elif peso < 90:
    cat = 'Medio'
elif peso < 100:
    cat = 'Meio-Pesado'
else:
    cat = 'Pesado'
if cat != '':
    print(f'O lutador {nome} com o peso {peso:.3f}kg está configurado na categoria {cat}')
else:
    print(f'Peso inválido: {peso}')