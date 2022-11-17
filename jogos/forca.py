import random


def jogar():
    
    print_star_mensagem()
    
    secret_word = charge_secret_word()
    letter_right = started_letter_right(secret_word)

    hanged = False
    hit = False
    erros = 0

    print("\n{}".format(letter_right))

    while(not hanged and not hit):

        strick = ask()

        if(strick in secret_word):
            point_letter_right(strick, letter_right, secret_word)
        else:
            erros += 1
            desenha_forca(erros)

        hanged = erros == 7
        hit = "_" not in letter_right
        print("\n{}".format(letter_right))


    if(hit):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()


#Initial game message
def print_star_mensagem():
    print("\n*********************************")
    print("** Bem vindo ao jogo da Forca! **")
    print("*********************************")

#Charge a word
def charge_secret_word():
    file = open("palavras.txt", "r")
    words = []

    for linha in file:
        linha = linha.strip()
        words.append(linha)

    file.close()

    number = random.randrange(0,len(words))
    secret_word = words[number].upper()

    return secret_word

#Draw _
def started_letter_right(word):
    return ["_" for letra in word]

#
def ask():
    strick = input("\nQual letra? ")
    strick = strick.strip().upper()
    return strick

#
def point_letter_right(strick, letter_right, secret_word):
    position = 0
    for letter in secret_word:
        if(strick == letter):
            letter_right[position] = letter
        position += 1

def imprime_mensagem_perdedor(secret_word):
    print("\nPuxa, você foi enforcado!")
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("\nParabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()