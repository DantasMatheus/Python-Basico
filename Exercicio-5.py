# Escreva um programa que leia um número real e mostre na tela os valores de 25%, 50%, 75% do
# valor lido usando o formato com 3 casas decimais mostrado abaixo:
# Adote o valor 136.7

val = float(input("Digite um numero real: "))

R1 = 0.25 * val
R2 = 0.50 * val
R3 = 0.75 * val

print("25% -> {:.3f}".format(R1), "50% -> {:.3f}".format(R2), "75% -> {:.3f}".format(R3), sep=' - ')

