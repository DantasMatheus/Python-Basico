# Uma empresa comercial trabalha com 3 vendedores externos e os remunera com R$ 1200,00 fixos
# mais comissão de 6% sobre o valor total vendido no mês. Escreva um programa que leia o nome e o
# total vendido pelos 3 vendedores, calcule e exiba na tela a mensagem de saída conforme o exemplo
# a seguir. Exiba os valores numéricos com duas casas decimais.

nome_1 = input("Digite o nome do primeiro vendededor: ")
venda_1 = float(input("Digite o valor total de vendas realizadas pelo vendedor: "))
nome_2 = input("Digite o nome do segundoo vendededor: ")
venda_2 = float(input("Digite o valor total de vendas realizadas pelo vendedor: "))
nome_3 = input("Digite o nome do terceiro vendededor: ")
venda_3 = float(input("Digite o valor total de vendas realizadas pelo vendedor: "))

R1 = 1200 + (venda_1 * 0.06)
R2 = 1200 + (venda_2 * 0.06)
R3 = 1200 + (venda_3 * 0.06)

print(f"Vendedor {nome_1} vendeu R${venda_1:.2f} e faz jus a uma comissao de R${R1:.2f}")
