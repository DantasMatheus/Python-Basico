# Em Albalândia mulheres e homens podem servir o exército do país. O serviço é opcional e é muito
# comum que as pessoas se apresentem para o serviço em algum momento da vida. Existe uma única
# restrição para ingresso que é a idade da pessoa: para mulheres a idade aceita é entre 21 e 34 anos;
# para homens a idade aceita é entre 18 e 39 anos. Escreva um programa que leia três dados de
# entrada: nome da pessoa, idade e sexo e informe se a pessoa será aceita ou não para o serviço.
# Para o sexo deve ser lido apenas 1 caractere que pode ser 'f' ou 'F' para feminino e 'm' ou 'M'
# para masculino, qualquer coisa diferente deve ser informado como inválido.

# mulheres entre 21 e 34 anos
# homens entre 18 e 39 anos

nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
sexo = input('Digite o sexo(para feminino use f ou F e para masculino use m ou M): ')

if sexo == 'f' or sexo == 'F':
    if 21 < idade < 34:
        print(f'{nome} de idade {idade} e sexo {sexo} foi aceita para o serviço militar')
    else:
        print(f'{nome} de idade {idade} e sexo {sexo} foi recusado para o serviço militar')
elif sexo == 'm' or sexo == 'M':
    if 18 < idade < 34:
        print(f'{nome} de idade {idade} e sexo {sexo} foi aceita para o serviço militar')
    else:
        print(f'{nome} de idade {idade} e sexo {sexo} foi recusado para o serviço militar')
else:
    print('Sexo inválido')