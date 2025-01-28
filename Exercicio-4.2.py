# Escreva um programa que leia um número inteiro e mostre na tela se ele é divisível por 10 ou não.

num = int(input('Digite um numero inteiro e descubra se ele é divisivel por 10: '))

if num % 10 == 0:
    print(f'O numero {num} é divisivel por 10')
else:
    print(f'O numero {num} não é divisivel por 10')