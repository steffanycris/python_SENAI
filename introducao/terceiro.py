# Firjan Senai Maracanã     Rio De Janeiro
# Centro de referencia em TI
# Curso : Desenvolvimento de  sistemas
# Instrutor : Sergio Damasceno Reis
# Nome do Programa : terceiro.py


'''
Desenvolva um pequeno programa que faça a leitura de um número e 
no final escreva 'é par' se o número for par ou 'é impar' se o
múmero for impar
'''

#Inicio
numero = int(input("Escreva um número: "))


if numero % 2 == 0:
    print(f'O {numero} é par')

else:
    print( f'O {numero} é impar')

#Fim