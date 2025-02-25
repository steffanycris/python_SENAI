# Firjan Senai Maracanã     Rio De Janeiro
# Centro de referencia em TI
# Curso : Desenvolvimento de  sistemas
# Instrutor : Sergio Damasceno Reis
# Nome do Programa : 


'''
6) Desenvolver um programa que apresente o valor de uma potência de uma base qualquer elevada a um expoente 
qualquer, ou seja, de b^e, onde os valores de b e e são fornecidos pelo usuário, sem utilizar Math.pow().
'''

#Inicio
b = int(input("Informe o valor de uma base: "))
e = int(input("Informe o valor de um expoente: "))

for cont in range (0,e+1):
    acum = b
    m = acum**e

print(m)

#Fim