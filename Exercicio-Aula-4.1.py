# Escreva um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar. Lembrando
# que para saber a paridade de um inteiro é preciso calcular o resto da sua divisão por 2. Se o resto for
# 0 o número é par, se o resto for 1 o número é ímpar.

num = int(input('Digite um numero inteiro: '))

if num % 2 == 0:
    print(f'O número {num} é par')
else:
    print(f'O número {num} é impar')