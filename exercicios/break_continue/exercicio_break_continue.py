# Elaborar um software que pergunte ao usuário um número de 1 a 20. 
# Este número deverá ser comparado com um número oculto definido pelo desenvolvedor já salvo no código, e 
# informar se o usuário acertou ou se errou. 
# Se errou, o software deve dar a dica se número oculto é menor ou maior que o inserido. 
# O usuário tem 5 tentativas para acertar o número oculto. O software deve informar em qual tentativa o usuário está. 
# Se o usuário não acertar nenhuma das 5 tentativas, deverá surgir uma mensagem informando que o teste de 
# adivinhação se encerrou e também apresentar o número oculto.
# Quando o usuário acertar o número oculto, o software deverá encerrar as tentativas, mesmo que ainda não esteja na 
# última.
# Se o usuário informar um número que não esteja no intervalo de 1 a 20, o software deve avisar que o número 
# inserido é inválido e passar para a próxima tentativa imediatamente.

cont=0

print("-------------------- Adivinhe o número secreto! --------------------")
print("-------------------- Você inicia com 5 tentativas --------------------")


while(True):

    n = int(input("Informe um número: "))

    if(n>=1 and n<=20):
        
        cont += 1

        if( n==4):

            print("•Parabéns, você acertou!")
            break

        if(cont == 5):
            print ("•Acabaram as suas tentativas!")
            print ("•Número secreto: 4")
            break

            
        else:
            if(n<4):
                print("Você errou! Tente novamente: ")
                print("•DICA: o número é MAIOR")
                print("Tentativas restantes:",5-cont)
                continue
            else:
                print("Você errou! Tente novamente. ")
                print("•DICA: o número é MENOR")
                print("Tentativas restantes:",5-cont)
                continue


    else:
        cont+=1
        print("•O número deve estar no intervalo de 1 a 20, tente novamente")
        print("Tentativas restantes:",5-cont)

        continue
        

        

        

