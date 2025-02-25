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
contpar = 0
contimpar = 0
valor = 0
par = 0
impar = 0
b = 0


print("Bem-vindo(a) ao controle de vendas!")
print("Adicione o valor da venda ao contador, caso queira encerrar o programa, digite fim")


while (valor != -1):


    valor = int(input("Valor da venda: "))
    
    if b == 0:
        maior = valor
        menor = valor
        b += 1
    
    if valor == -1:
        break

    if (valor > maior):
        maior = valor

    if(valor<maior):
        menor = valor


    if (valor%2==0):

        contpar = contpar + 1

        par = par + valor

        mediapar = par/contpar


    else:
        contimpar = contimpar + 1

        impar = impar + valor

        mediaimpar = impar/contimpar


    cont = cont + 1

    acum = acum + valor

    media = acum / cont


    

print("Total arrecadado:",acum)
print(f"Média geral das vendas realizadas:{media}")
print("A média dos valores das vendas pares:",mediapar)
print("A média dos valores das vendas ímpares:",mediaimpar)
print("A quantidade total de vendas realizadas:",cont)
print("O valor da venda mais alta:",maior)
print("O valor da venda mais baixa:",menor)



    
