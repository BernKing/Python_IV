import random

dinheiro = 100
jogadas = 0


def num_aleatorio():
    return random.randint(0, 1)


while dinheiro > 0 and jogadas <= 10:

    apostar = int(input("Aposta:"))

    if apostar <= dinheiro:
        dinheiro = dinheiro - apostar
        jogadas += 1
        n = num_aleatorio()
        if n == 1:
            dinheiro = dinheiro + 2 * apostar
            print("Dinheiro:", dinheiro)

        elif n == 0:
            print("Perdeste: ", dinheiro, " restante")

    else:
        print("So tens ", dinheiro, "Tenta denovo")
