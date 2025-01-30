# Escreva um programa para uma fábrica de calçados que leia o código LL de um calçado, que é um
# número inteiro com 2 dígitos. Exiba na tela a linha do calçado, conforme a tabela a seguir. Se o
# número fornecido não estiver na tabela, deve-se exibir a mensagem "Código inválido".

# LL Linha de calçados  | LL Linha de calçados
#       16 Bebê         | 49 Masculino esportivo
# 23 Infantil feminino  | 52 Feminino formal salto baixo
# 25 Infantil masculino | 53 Feminino formal salto alto
# 29 Infantil esportivo | 55 Feminino casual salto baixo
# 42 Masculino formal   | 56 Feminino casual salto alto
# 43 Masculino casual   | 59 Feminino esportivo

LL = int(input('Digite o LL de um calçado para iniciar a busca: '))

if LL == 16:
    calcado = 'Bebê'
elif LL == 23:
    calcado = 'Infantil feminino'
elif LL == 25:
    calcado = 'Infantil masculino'
elif LL == 29:
    calcado = 'Infantil esportivo'
elif LL == 42:
    calcado = 'Masculino Formal'
elif LL == 43:
    calcado = 'Masculino casual'
elif LL == 49:
    calcado = 'Masculino esportivo'
elif LL == 52:
    calcado = 'Feminino formal salto baixo '
elif LL == 53:
    calcado = 'Feminino formal salto alto'
elif LL == 55:
    calcado = 'Feminino casual salto baixo'
elif LL == 56:
    calcado = 'Feminino casual salto alto'
elif LL == 59:
    calcado = 'Feminino esportivo'
else:
    calcado = 'Invalido'

if calcado == 'Invalido':
    print('Codigo invalido')
else:
    print(f'o LL:{LL} é correspondete a linha de calçado: {calcado}')