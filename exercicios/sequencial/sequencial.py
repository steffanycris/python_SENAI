# Firjan Senai Maracanã     Rio De Janeiro
# Centro de referencia em TI
# Curso : Desenvolvimento de  sistemas
# Instrutor : Sergio Damasceno Reis
# Nome do Programa : sequencial.py


'''
1) Desenvolver um programa que pergunte ao usuário o seu nome completo e a sua idade. Em seguida, o programa 
deve apresentar os dados anteriormente informados. 
'''

#Inicio
nome = input("Informe o seu nome completo: ")
nasc = int(input("Informe o seu ano de nascimento: "))
idade = 2025 - nasc

print("Nome completo: ",nome)
print("Nascimento: ",nasc)
print("Idade: ",idade)
#Fim