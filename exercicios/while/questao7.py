# Firjan Senai Maracanã     Rio De Janeiro
# Centro de referencia em TI
# Curso : Desenvolvimento de  sistemas
# Instrutor : Sergio Damasceno Reis
# Nome do Programa : decisao2.py


'''
7) Desenvolver um programa que apresente todos os números divisíveis por 4 que sejam menores que 200. Para 
saber se o número é divisível por 4 será necessário verificar a lógica desta condição com o comando if. Sendo 
divisível, mostre-o; não sendo, passe para o próximo passo. A variável que controla o contador deve ser iniciada 
com valor 1.
'''

#Inicio

contador = 1
while ( contador < 200 ):
    div = contador%4

    if (div==0):
        print( contador )
        
    contador = contador +1


#Fim