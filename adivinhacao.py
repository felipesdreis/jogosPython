import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = round(random.randrange(1,51))
    total_tentativas = 0
    pontos = 1000


    print("Qual nivel de dificuldade?")
    print("(1) Facil (2) Medio (3) Dificil")

    nivel = int(input("Define o nivel: "))
    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas +1):
        print("Tentativa {} de {}".format(rodada, total_tentativas))
        chute = input("Digite o seu numero 1-50: ")
        print("Voce digitou", chute)
        chute_int = int(chute)

        if(chute_int < 1 or chute_int > 50):
            print("Voce deve digitar entre 1 e 50")
            continue

        acertou = chute_int == numero_secreto
        maior = chute_int > numero_secreto
        menor = chute_int < numero_secreto

        if (acertou):
            print("Voce Acertou e fez {} pontos :)".format(pontos))
            break
        else:
            if(maior):
                print("Seu Chute foi Maior")
            elif(menor):
                print("Seu Chute Foi Menor")
            pontos_perdidos = abs(numero_secreto - chute_int)
            pontos = pontos - pontos_perdidos

    print("O Numero Secreto era:", numero_secreto)
    print("Fim do Jogo")

if(__name__ == "__main__"):
    jogar()
