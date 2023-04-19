import random
import os

def jogar():
    print("---------------------------------\nBem vindo no jogo de Adivinhação!\n---------------------------------")
    
    numeroSecreto = random.randrange(0, 101) 
    totalDeTentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        totalDeTentativas = 20
    elif nivel == 2:
        totalDeTentativas = 10
    elif nivel == 3:
        totalDeTentativas = 5 
    else:
        print("[Erro] Digite uma opção valida.")
    
    for rodada in range(1, totalDeTentativas + 1):

        print("Tentativa {} de {}".format(rodada, totalDeTentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)
        print("Você digitou" , chute_str)
    
        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue
        
        if numeroSecreto == chute:
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if chute > numeroSecreto:
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif chute < numeroSecreto:
                print("Você errou! O seu chute foi menor que o número secreto.")       
            pontosPerdidos = abs(numeroSecreto - chute)
            pontos = pontos - pontosPerdidos 
            
    print("Fim de jogo.")

if(__name__ == "__main__"):
    jogar()