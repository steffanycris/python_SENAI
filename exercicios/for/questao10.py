# Firjan Senai Maracanã     Rio De Janeiro
# Centro de referencia em TI
# Curso : Desenvolvimento de  sistemas
# Instrutor : Sergio Damasceno Reis
# Nome do Programa : 


'''
10) Desenvolver um programa que apresente o fatorial de um número informado pelo usuário.
'''

#Inicio

n = int(input("Fatorial de: ") )

result=1
for cont in range(1,n+1):
    result *= cont

print(result)

#Fim