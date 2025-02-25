# Firjan Senai Maracanã     Rio De Janeiro
# Centro de referencia em TI
# Curso : Desenvolvimento de  sistemas
# Instrutor : Sergio Damasceno Reis
# Nome do Programa : 


'''
8) Desenvolver um programa que pergunte 20 vezes o nome inteiro de uma pessoa, sexo e idade, e exiba o nome 
inteiro das pessoas que são do sexo masculino e possuem 21 anos ou mais
'''

#Inicio

for cont in range (1, 21):
    nome = input("Informe o seu nome: ")
    sexo= input("Informe o seu sexo: ")
    idade = int(input("Informe a sua idade: "))

    if (sexo=="masculino") and (idade>=21):
        print(nome,"|",sexo,"|",idade)

#Fim