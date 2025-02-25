# Firjan Senai Maracanã     Rio De Janeiro
# Centro de referencia em TI
# Curso : Desenvolvimento de  sistemas
# Instrutor : Sergio Damasceno Reis
# Nome do Programa : decisao2.py


'''
8) Desenvolver um programa que apresente todos os valores numéricos inteiros ímpares situados na faixa de 0 a 
20. Para saber se o número é ímpar, será necessário verificar essa condição com o comando if. Sendo ímpar, 
mostre-o; não sendo, passe para o próximo passo. 
'''

#Inicio
contador = 0
while ( contador <= 20 ):
    div = contador%2

    if (div==1):
        print( contador )
        
    contador = contador +1
#Fim