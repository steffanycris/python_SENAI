# Firjan Senai Maracanã     Rio De Janeiro
# Centro de referencia em TI
# Curso : Desenvolvimento de  sistemas
# Instrutor : Sergio Damasceno Reis
# Nome do Programa : 


'''
9) Desenvolver um programa que pergunte um número inteiro e exiba os números que são, ao mesmo tempo, 
múltiplos de 3 e 5, na sequência de 1 até o número informado pelo usuário
'''

#Inicio

n = int(input("Informe um número: "))

for cont in range (1,n+1):
    div3 = cont%3
    div5 = cont%5

    if (div3==0)and(div5==0):
        print(cont)


#Fim