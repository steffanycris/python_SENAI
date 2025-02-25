# Firjan Senai Maracanã     Rio De Janeiro
# Centro de referencia em TI
# Curso : Desenvolvimento de  sistemas
# Instrutor : Sergio Damasceno Reis
# Nome do Programa : decisao2.py


'''
9) Elaborar um programa que apresente no final a soma dos valores pares existentes na faixa de 0 até 500. Utilize 
um laço que efetue a variação de 2 em 2.
'''

#Inicio
contador = 0
acum = 0

while ( contador <= 500 ):
    print( contador )
    acum = acum+contador
    contador = contador + 2

print("A soma dos valores pares existentes na faixa de 0 até 500, é: ",acum)

#Fim