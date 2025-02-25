# Firjan Senai Maracanã     Rio De Janeiro
# Centro de referencia em TI
# Curso : Desenvolvimento de  sistemas
# Instrutor : Sergio Damasceno Reis
# Nome do Programa : sequencial6.py


'''
6) Desenvolver um programa que pergunte ao usuário o seu peso e sua altura. Ao final o 
programa deverá exibir na tela o valor do índice de massa corporal desta pessoa (IMC). 
Fórmula: IMC = peso / altura2
 - Obs: peso em quilos e altura em metros.
'''

#Inicio
peso = float(input("Informe o seu peso(Kg): "))
altura = float(input("Informe a sua altura(metros): "))
imc = peso/(altura*altura)

print("O O seu IMC é de: ",imc)

#Fim