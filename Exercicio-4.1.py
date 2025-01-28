# Classificação indicativa é um conceito que se aplica à faixa etária para a qual uma obra audiovisual
# se recomenda ou não. Suponha que um filme em cartaz no cinema tenha a Classificação de 16 anos.
# Escreva um programa que leia a idade de uma pessoa e mostre se está de acordo ou não com a
# classificação.

clas = int(input('Digite a classificação etária do filme: '))
idade = int(input('Digite a idade: '))

if idade < clas:
    print('Sua idade é abaixo da classificação etária do filme')
else:
    print('Pode assistir seu filme sem preocupações')