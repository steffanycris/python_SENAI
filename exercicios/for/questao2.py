# Firjan Senai Maracanã     Rio De Janeiro
# Centro de referencia em TI
# Curso : Desenvolvimento de  sistemas
# Instrutor : Sergio Damasceno Reis
# Nome do Programa : 


'''
2) Desenvolver um programa que apresente o total da soma de n números inteiros do número 1 até n, onde n é um 
valor informado pelo usuário. 
'''

#Inicio
acum = 0
n = int(input("Informe um número: "))

for cont in range (1,n+1): 
    acum = acum+cont

print("A soma dos valores de 1 a",n,"é:",acum)

#Fim