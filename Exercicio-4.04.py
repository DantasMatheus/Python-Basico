# Escreva um programa que leia o nome de um aluno e as notas obtidas em três avaliações. A média
# final é a média aritmética das três notas e a pessoa estará aprovada se essa média for maior ou igual
# a 7.0. Mostre na tela o nome, a média e a situação que será "Aprovado" ou "Reprovado".

nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))

media = (n1 + n2 + n3) / 3

if media < 7:
    print(f'O aluno {nome} foi reprovado com {media:.1f} de media final')
else:
    print(f'O aluno {nome} foi aprovado com {media:.1f} de media final')