import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    palavra_secreta = carrega_palavra()
    letras_acertadas = ["_" for letra in palavra_secreta]
    print(letras_acertadas)
    
    # variaveis de controle
    enforcou = False
    acertou = False
    tentativas = 0
    
    while(not enforcou and not acertou):
        chute = input("Qual letra?")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:            
                if(chute == letra):
                    letras_acertadas[index] = letra
                index +=1
            print(letras_acertadas)
        else:
            tentativas +=1
            print(f"Errado --- Tentativas restantes: {6-tentativas}")
            
        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas
    if(acertou):
        print(f"VOCE GANHOU --- {palavra_secreta}")
    else:
        print(f"VOCE PERDEU --- {palavra_secreta}")    
    print("Fim do Jogo")
    
def carrega_palavra():    
    arquivo_palavras = open("palavras.txt","r")
    lista_palavras = []
    for linha in arquivo_palavras:
        linha = linha.strip()
        lista_palavras.append(linha)
    arquivo_palavras.close()
    
    numero_palavra = random.randrange(0, len(lista_palavras))
    
    palavra_secreta = lista_palavras[numero_palavra].upper()
    return palavra_secreta

if(__name__ == "__main__"):
    jogar()