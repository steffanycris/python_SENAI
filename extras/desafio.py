"""
Uma pequena loja deseja acompanhar suas vendas diárias para entender melhor o desempenho 
do negócio. Para isso, foi solicitado um programa que registre as vendas de diferentes produtos 
e forneça um resumo ao final do expediente.
O programa deve permitir que o operador da loja insira, repetidamente, os valores das vendas 
realizadas ao longo do dia. Cada venda corresponde ao valor total de um pedido. No entanto, 
algumas regras devem ser observadas durante o registro:

• Apenas valores positivos podem ser inseridos, pois não existem vendas negativas. Caso 
um valor inválido seja informado, o sistema deve solicitar um novo valor.

• O sistema deve acompanhar e exibir, ao final do expediente:

▪ O total arrecadado no dia.

▪ A média geral das vendas realizadas.

▪ A média dos valores das vendas pares e ímpares separadamente.

▪ A quantidade total de vendas realizadas.

▪ O valor da venda mais alta e da venda mais baixa.

• Durante a inserção dos valores, o sistema deve apresentar os números de forma 
organizada e separada para facilitar a visualização.

O programa deve funcionar continuamente até que o operador indique o fim do expediente. O 
formato de exibição dos dados deve ser amigável e organizado
"""

#inicio

cont = 0
acum = 0
cont_par = 0
cont_impar = 0
valor = 0
par = 0
impar = 0
# b = 0 maior ou menor
maior = 0
menor = 10000

print("Bem-vindo(a) ao controle de vendas!")
print("Adicione o valor da venda ao contador, caso queira encerrar o programa, digite -1")


while (valor != -1):


    valor = int(input("Valor da venda: "))
    
    if (valor ==0 or valor<-1):
        print("Apenas valores POSITIVOS podem ser inseridos, pois não existem vendas negativas.")
        print("Tente novamente ou encerre o programa(-1):")
        continue
        

    # if b == 0: outra forma de fazer
    #     maior = valor
    #     menor = valor
    #     b += 1
    
    if valor == -1:
        print("--- fim do expediente ---")
        break

    if (valor > maior): #maior venda
        maior = valor

    if(valor<menor): #menor venda
        menor = valor


    if (valor%2==0): #verificação de número par

        cont_par = cont_par + 1 #cont para os números pares

        par = par + valor #acum para os números pares

        media_par = par/cont_par #média dos números pares


    else: #verificação de número ímpar
        cont_impar = cont_impar + 1 #cont para os números impares

        impar = impar + valor #acum para os números impares

        media_impar = impar/cont_impar #média dos números pares


    cont = cont + 1 #cont de vendas

    acum = acum + valor #acum do total arrecadado

    media = acum / cont #média geral


    

print("•Total arrecadado: R$",acum)
print(f"•Média geral das vendas realizadas:{media}")
print("•A média dos valores das vendas pares:",media_par)
print("•A média dos valores das vendas ímpares:",media_impar)
print("•A quantidade total de vendas realizadas:",cont)
print("•O valor da venda mais alta:",maior)
print("•O valor da venda mais baixa:",menor)

#fim

    
