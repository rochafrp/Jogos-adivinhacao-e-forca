import forca
import adivinhacao

print("-------------------------------\n------Escolha o seu jogo:-----\n-------------------------------")
print("\n(1) Forca (2) Adivinhação")

jogo = int(input("\nQual jogo? "))

if jogo == 1:
    print("Jogando forca")
    forca.jogar()
elif jogo == 2:
    print("Jogando adivinhação")
    adivinhacao.jogar()