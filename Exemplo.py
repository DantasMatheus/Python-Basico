#exemplo 1
print("--------------Teste de objetos Python----------------------")
quantidade = 3
precouni = 36.2
total = quantidade * precouni
msg = 'Total ='
print(msg, "{:.2f}".format(total))


#exemplo 2: Operadores Lógicos
print("-------------------Operadores Logicos------------------")

A = 14
B = 5
C = A + B
print("Soma:", C)
C = A - B
print("Subtracao:", C)
C = A * B
print("Multiplicacao:", C)
C = A / B
print("Divisao:", C)
C = A // B
print("Divisao inteira:", C)
C = A % B
print("Resto da divisão(modulo):", C)
C = -A
print("Menos unário de A:", C)
C = -B
print("Menos unário de B:", C)
C = A ** B
print("Potenciacao:", C)

#exemplo 3: Biblioteca math
#funcao sqrt que calcula raiz quadrada

from math import sqrt
print("------------------------Teste biblioteca math-------------------")
X = 49
R = sqrt(X)
print("A raiz quadrada e:",R)
