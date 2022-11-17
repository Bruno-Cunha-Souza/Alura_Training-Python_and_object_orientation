import forca
import adivinhacao

def game_choose():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    game = int(input("Qual jogo? "))

    if(game == 1):
        print("Jogando forca")
        forca.jogar()
    elif(game == 2):
        print("Jogando adivinhação")
        adivinhacao.play()

if(__name__ == "__main__"):
    game_choose()
