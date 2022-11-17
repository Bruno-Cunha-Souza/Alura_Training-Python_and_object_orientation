import random

def play():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    secret_number = random.randrange(1,101)
    total_attempts = 0
    points = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_attempts = 20
    elif(nivel == 2):
        total_attempts = 10
    else:
        total_attempts = 5

    for round in range(1, total_attempts + 1):
        print("Tentativa {} de {}".format(round, total_attempts))

        strick_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , strick_str)
        strick = int(strick_str)

        if(strick < 1 or strick > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        hit = strick == secret_number
        more   = strick > secret_number
        smaller   = strick < secret_number

        if( hit ):
            print("Você acertou e fez {} pontos!".format(points))
            break
        else:
            if(more):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(smaller):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(secret_number - strick)
            points = points - pontos_perdidos

    print("Fim do jogo")

if(__name__ == "__main__"):
    play()
