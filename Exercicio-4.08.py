# Escreva um programa que leia um número inteiro que representa um ano. Informe se esse ano é
# bissexto ou não.
# Regra: O ano é bissexto se cumprir uma das seguintes condições:
# a) ser múltiplo de 4 e ao mesmo tempo não ser múltiplo de 100
# b) ser múltiplo de 400

ano = int(input('Digite o ano: '))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')