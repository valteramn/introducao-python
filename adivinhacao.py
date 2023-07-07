print("*********************************")
print("Bem vindo ao Jogo de Adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
    print("Tentativa", rodada, "de", total_de_tentativas)
    chute = int (input("Digite o seu número: "))

    print("Você digitou " , chute)

    acertou = chute == numero_secreto #booleano
    maior = chute > numero_secreto #booleano
    menor = chute < numero_secreto #booleano

    if(acertou): 
        print("Você acertou!")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")

    rodada = rodada + 1

    print("FIM DO JOGO")


#MÉTODO 2

'''
numero_secreto = 42
chute_str = input("Digite seu número")
chute = int(chute_str)
print("Você digitou ", chute)
if(numero_secreto == chute):
    print("Você acertou")
else:
    print("Você errou")
'''
