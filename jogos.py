import forca
import adivinhacao
print("*********************************")
print("******Escolha o Jogo*************")
print("*********************************")


print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual o Jogo?"))

if(jogo == 1):
    #forca
    forca.jogar()
elif(jogo == 2):
    #adivinhacao
    adivinhacao.jogar()