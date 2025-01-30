# Escreva um programa que leia 3 números inteiros e mostre na tela uma das seguintes opções:
# a) "Os três valores são iguais"
# b) "Há dois valores iguais e um diferente"
# c) "Os três valores são diferentes"

a = int(input('Digite um numero inteiro: '))
b = int(input('Digite um numero inteiro: '))
c = int(input('Digite um numero inteiro: '))

if a == b == c:
    print('Os tres valores são iguais')
elif a == b or a == c or b == c:
    print('Há dois valores iguais e um diferente')
else:
    print('Os três valores são diferentes')