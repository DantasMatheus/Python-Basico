# Escreva um programa que leia dois inteiros e mostre na tela apenas o menor dos dois. Se ambos
# forem iguais, mostre qualquer um deles.

A = int(input('Digite um numero inteiro: '))
B = int(input('Digite um numero inteiro: '))

if A < B:
    print(f'o numero {A} é menor')
elif B < A:
    print(f'o numero {B} é menor')
else:
    print(f'os numeros sao iguais e valem {A}')