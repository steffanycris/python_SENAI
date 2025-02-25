# Firjan Senai Maracanã     Rio De Janeiro
# Centro de referencia em TI
# Curso : Desenvolvimento de  sistemas
# Instrutor : Sergio Damasceno Reis
# Nome do Programa : 


'''
3) Desenvolver um programa que apresente os resultados de uma tabuada de um número qualquer informado 
pelo usuário
'''

#Inicio

n = int(input("Informe um número: "))

for cont in range(1,11):
    print(n,".",cont,"=",n*cont)
    
#Fim