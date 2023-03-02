# Exercicio 10
#  Implemente o exercício anterior fazendo com que o computador faça de jogador B.
import random

while True:
    num_a = int(input("Introduza o numero A"))

    if 1 <= num_a <= 100:
        break


while True:

    num_b = random.randint(1,100)

    if num_b < num_a:
        print("Numero abaixo")

    if num_b > num_a:
        print("numero acima")

    elif num_b == num_a:
        print("Acertaste o numero")
        break