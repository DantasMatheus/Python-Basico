# Escreva um programa que leia 3 números inteiros e mostre na tela se eles formam um triângulo ou
# não. Caso formem um triângulo informe o tipo de triângulo (equilátero, isósceles ou escaleno).
# Regra: Para três números formarem um triângulo precisa ocorrer que:
# a) os três números precisam ser maiores que zero;
# b) a soma dos dois menores valores deve ser maior que o terceiro.

a = int(input('Digite um numero inteiro: '))
b = int(input('Digite um numero inteiro: '))
c = int(input('Digite um numero inteiro: '))

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c

somamenores = 0
if a != maior:
    somamenores += a
if b != maior:
    somamenores += b
if c != maior:
    somamenores += c

if a > 0 and b > 0 and c > 0 and somamenores > maior:
    if a == b == c:
        print('triangulo Equilatero')
    elif a == b != c or a !=b == c or a == c != b:
        print('Triangulo isosceles')
    else:
        print('Triangulo escaleno')
else:
    print(f'nao foi possivel formar um triangulo com os numeros {a}, {b} e {c}')
