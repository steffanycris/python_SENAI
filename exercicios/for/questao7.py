# Firjan Senai Maracanã     Rio De Janeiro
# Centro de referencia em TI
# Curso : Desenvolvimento de  sistemas
# Instrutor : Sergio Damasceno Reis
# Nome do Programa : 


'''
7) Desenvolver um programa que apresente no final a soma dos valores pares existentes na faixa de 3 até 21 
'''

#Inicio

acum = 0

for cont in range (3,22):
    div = cont%2

    if(div==0):
        acum +=cont

print("A soma de todos os valores pares de 3 a 21 é:",acum)

#Fim