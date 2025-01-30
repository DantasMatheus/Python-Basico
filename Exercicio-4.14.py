# Em um determinado momento do dia a cotação de compra das moedas estrangeiras é a seguinte:
# Dólar: US$ 1.00 = R$ 4.89 - Euro: € 1.00 = R$ 5.26 - Libra Esterlina: £ 1.00 = R$ 6.17
# Escreva um programa que leia o tipo (D, E ou L maiúsculo) e o valor de moeda estrangeira que se
# quer comprar e calcule o valor em reais necessários.

D = 4.89
E = 5.26
L = 6.17

moeda = input('Digite a moeda que deseja comprar sendo D para Dolar, E para Euro e L para Libra Esterlina: ')
qtdeMoeda = float(input('Digite o quanto da moeda escolhido que você deseja comprar: '))

if moeda == 'D':
    valorReais = qtdeMoeda * D
    print(f'Serão necessários R$ {valorReais:.2f} para comprar US$ {qtdeMoeda:.2f}')
elif moeda == 'E':
    valorReais = qtdeMoeda * E
    print(f'Serão necessários R$ {valorReais:.2f} para comprar € {qtdeMoeda:.2f}')
elif moeda == 'L':
    valorReais = qtdeMoeda * L
    print(f'Serão necessários R$ {valorReais:.2f} para comprar £ {qtdeMoeda:.2f}')
else:
    print(f'Moeda {moeda} inválida!')