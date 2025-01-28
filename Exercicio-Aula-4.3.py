# Altere o programa anterior de modo que ele continue exibindo o menor dos dois valores lidos. Porém,
# quando forem iguais o programa deve exibir o valor junto com o texto "Os dois números são iguais".

A = int(input('Digite um numero inteiro: '))
B = int(input('Digite um numero inteiro: '))

if A == B:
    print(f'os números sao iguais e valem {A}')
else:
    if A < B:
        print(f'o numero {A} é menor')
    else:
        print(f'o numero {B} é menor')