# Nas eleições municipais os municípios com 200 mil eleitores ou mais tem segundo turno caso o
# primeiro colocado não tenha mais do que 50% dos votos. Escreva um programa que leia o nome do
# município, a quantidade de eleitores e a quantidade de votos do candidato mais votado e informe se
# haverá segundo turno ou não.

municipio = input("Digite o nome do municipio: ")
eleitores = int(input("Digite a quantidade de eleitores: "))
votos = int(input("Digite a quantidade de votos do candidato mais votado: "))
metade = eleitores//2

if eleitores >= 200000:
    if votos < metade:
        print(f'Nesse município haverá segundo turno')
    else:
       print('Nesse município não haverá segundo turno')
else:
    print('Nesse município não haverá segundo turno')