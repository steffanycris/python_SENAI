# Firjan Senai Maracanã     Rio De Janeiro
# Centro de referencia em TI
# Curso : Desenvolvimento de  sistemas
# Instrutor : Sergio Damasceno Reis
# Nome do Programa : decisao.py


'''
1) Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número é par ou 
é ímpar. 
'''

#Inicio
numero = int(input("Escreva um número: "))


if numero % 2 == 0:
    print(f'O {numero} é par')

else:
    print( f'O {numero} é impar')
#Fim