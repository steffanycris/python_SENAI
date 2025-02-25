# Firjan Senai Maracanã     Rio De Janeiro
# Centro de referencia em TI
# Curso : Desenvolvimento de  sistemas
# Instrutor : Sergio Damasceno Reis
# Nome do Programa : 


'''
5) Desenvolver um programa que apresente os resultados de uma tabela de um número qualquer. Ela deve ser 
impressa no seguinte formato: 
Considerando como exemplo o fornecimento do número 2
2 . 1 = 2
2 . 2 = 4
2 . 3 = 6
2 . 4 = 8
2 . 5 = 10
(...)
2 . 10 = 20
'''

#Inicio
cont = 1
n = int(input("Informe um número: "))

while (cont <= 10):
    print(n," .",cont,"=",n*cont)
    cont = cont+1 #é o mesmo que cont = cont+1
#Fim