import random
import os

os.system("cls||clear")
def jogar():
    print("--------------------------------\n--Bem vindo no jogo da forca!--\n--------------------------------")

    arquivo = open("palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()
    
    numero = random.randrange(0, len(palavras))
    palavraSecreta = palavras[numero].upper()
    letrasAcertadas = ["_" for letra in palavraSecreta] #essa linha faz a mesma função das linhas comentadas abaixo:
    
    #letrasAcertadas = []
    #for letra in palavraSecreta:
    #    letrasAcertadas.append("_")
    
    enforcou = False
    naoAcertou = False
    erros = 0
    
    print("\n", letrasAcertadas)
    
    while not enforcou and not naoAcertou:
        chute = input("\nQual letra? ")
        chute = chute.strip().upper()
        
        if chute in palavraSecreta :
            index = 0       
            for letra in palavraSecreta:
                if chute == letra:
                    letrasAcertadas[index] = letra
                index += 1
        else:
            erros += 1
        enforcou = erros == 6
        naoAcertou = "_" not in letrasAcertadas
        print("\n", letrasAcertadas)
        
    if naoAcertou:
        os.system("cls||clear")
        print("\n", "Você ganhou!!!")
    else:
        os.system("cls||clear")
        print("\n", "Você perdeu!!!")
        
    print("\n", "Fim de jogo.")

if(__name__ == "__main__"):
    jogar()