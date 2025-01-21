# Escreva um programa que leia os nomes de três pessoas de uma família: mãe, pai e criança.
# O programa deve exibir na tela a mensagem.
# "Os adultos {mãe} e {pai} são os responsáveis por {criança}"
# Faça de dois modos: com o metodo .format() e com f-string

# Objetos
mae = input('Digite o nome da mae: ')
pai = input('Digite o nome do pai: ')
crianca = input('Digite o nome da crianca: ')

# Metodo .format()
print("Os adultos {0} e {1} sao os responsaveis por {2}".format(mae, pai, crianca))

# Metodo f-string
print(f"Os adultos {mae} e {pai} sao os responsaveis por {crianca}")