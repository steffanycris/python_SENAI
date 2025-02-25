# Firjan Senai Maracanã     Rio De Janeiro
# Centro de referencia em TI
# Curso : Desenvolvimento de  sistemas
# Instrutor : Sergio Damasceno Reis
# Nome do Programa : 


'''
4) Desenvolver um programa que apresente o valor da soma dos cem primeiros números inteiros (1 + 2 + 3 + 4 + ... 
+ 97 + 98 + 99 + 100). 
'''

#Inicio
acum = 0
cont = 1

while (cont <= 100):
    acum += cont #é o mesmo que acum = cont+acum
    cont = cont + 1

print("A soma de todos os números de 1 até 100 é: ",acum)

#Fim