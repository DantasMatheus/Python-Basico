# Escreva um programa que leia um número inteiro que representa uma quantidade de tempo em
# segundos. Calcule e mostre na tela a quantidade de horas, minutos e segundos.

segundos = int(input("Digite os segundos: "))

horas = segundos//3600
segundos %= 3600

minutos = segundos//60
segundos %= 60

print(f" {horas} hora(s), {minutos} minuto(s), {segundos} segundo(s)")
