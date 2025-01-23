# Escreva um programa que leia três números reais em objetos denominados A, B e C. O programa
# deve calcular e mostrar na tela os resultados das fórmulas a seguir, usando 3 casas decimais.
# Adote A = 22.65 B = -39.1 C = 18.115

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

R1 = A + B + C
R2 = A * B * C
R3 = 2*(A + B) - C
R4 = (A + B + C) / 3
R5 = ((2*B) + (3*C)) / (5*A)
R6 = A**2 + B**2

print("O valor da primeira operação é: {:.3f}".format(R1))
print("O valor da Segunda operação é: {:.3f}".format(R2))
print("O valor da terceira operação é: {:.3f}".format(R3))
print("O valor da quarta operação é: {:.3f}".format(R4))
print("O valor da quinta operação é: {:.3f}".format(R5))
print("O valor da sexta operação é: {:.3f}".format(R6))
