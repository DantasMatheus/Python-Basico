# Quando uma pessoa ou uma empresa realiza um investimento espera-se um retorno positivo (lucro),
# embora também possa ocorrer um retorno negativo (prejuízo). Uma forma inicial de avaliar o retorno
# é conhecida com Retorno sobre Investimento (ou ROI, uma sigla em inglês). Cálculo do ROI:
# 𝑅𝑂𝐼 = 𝑅𝑒𝑐𝑒𝑖𝑡𝑎 − (𝐶𝑢𝑠𝑡𝑜𝑠 + 𝐼𝑛𝑣𝑒𝑠𝑡𝑖𝑚𝑒𝑛𝑡𝑜) . 100%
#         𝐶𝑢𝑠𝑡𝑜𝑠+𝐼𝑛𝑣𝑒𝑠𝑡𝑖𝑚𝑒𝑛𝑡𝑜
# Escreva um programa que leia 3 dados de entrada reais: Investimento, Custos e Receita, calcule o
# ROI usando a fórmula acima e exiba o resultado com uma casa decimal no formato mostrado abaixo.

investimento = float(input("Digite o valor do Investimento: "))
custos = float(input("Digite o valor dos Custos: "))
receita = float(input("Digite o valor da Receita: "))

ROI = ((receita - (custos + investimento)) / (custos+investimento)) * 100

print(f"o calculo do ROI foi: {ROI:.1f}%")
