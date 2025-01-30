# No comércio, o conceito de Margem Bruta é uma porcentagem que é aplicada ao preço de custo
# para se obter o preço de venda. Uma loja tem como política comercial aplicar uma margem bruta de
# 45% quando o preço de custo de um produto é menor ou igual a R$ 100,00. Se o produto custa mais
# que isso a margem bruta é de 35%. Escreva um programa que leia o preço de custo do produto e
# mostre na tela qual o seu preço de venda, com duas casas decimais.

# 45% se caso o preço de custo for <= 100
# 35% se caso o preço de custo for >=100

precoCusto = float(input('Digite o preço de custo do produto: '))

if precoCusto <= 100:
    precoVenda = precoCusto + (precoCusto * 0.45)
    print(f'Preço de venda do produto será de {precoVenda:.2f}')
else:
    precoVenda = precoCusto + (precoCusto * 0.35)
    print(f'Preço de venda do produto será de {precoVenda:.2f}')
