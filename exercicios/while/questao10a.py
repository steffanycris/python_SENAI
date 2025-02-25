# Firjan Senai Maracanã     Rio De Janeiro
# Centro de referencia em TI
# Curso : Desenvolvimento de  sistemas
# Instrutor : Sergio Damasceno Reis
# Nome do Programa : 


'''
10) Desenvolver um programa que apresente as potências de 3 variando de 0 a 15. Deve ser considerado que 
qualquer número elevado a zero é 1, e elevado a 1 é ele próprio. A apresentação deve observar a seguinte 
exibição na tela:
3 elevado à 0 = 1
3 elevado à 1 = 3
3 elevado à 2 = 9
(...)
3 elevado à 15 = 14348907
OBS: Tente fazer em uma classe utilizando Math.pow() e em outra classe sem utilizar Math.pow() 
'''

#Inicio

cont = 0

while (cont <= 15):
    print(f"3 elevado à {cont} = {pow(3,cont)}")
    cont = cont+1 #é o mesmo que cont = cont+1

#Fim