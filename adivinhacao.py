import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação.")
    print("********************************.")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 13
    elif (nivel == 2):
        total_de_tentativas = 8
    elif (nivel == 3):
        total_de_tentativas = 4

    for rodada in range(1, total_de_tentativas + 1):
        print("tentativa: {} de {}". format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100.")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou!!!")
            break
        else:
            if (maior):
                print("Você errouu! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errouu! O seu chute foi menor que o número secreto")

    print("Fim de jogo")


if (__name__ == "__main__"):
    jogar()
