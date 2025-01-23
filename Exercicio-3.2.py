# Escreva um programa que leia um texto e mostre na tela o texto e a quantidade de
# caracteres que ele contém, usando a seguinte mensagem:
# "O texto {AquiColoqueOTexto} contém {Quantidade} caracteres"
# Faça de dois modos: com o metodo .format() e com f-string
# DICA: Use a função len()

#Objetos
texto = input("Digite um texto: ")
qtde = len(texto)

#Metodo .format()
print("O texto {0} contem {1} caracteres".format(texto, qtde))

#Metodo f-string
print(f"O texto {texto} contem {qtde} caracteres")
