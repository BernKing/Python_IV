# Exercicio9

# Considere o seguinte jogo entre dois jogadores: O jogador A pensa num número entre 1
# e 100. O jogador B tem n tentativas para descobrir esse número. Em cada tentativa o
# jogador A deve dizer se o número que o jogador B disse é o correto ou se é maior ou
# menor do que o número pensado. Escreva um programa que implemente este jogo sendo
# o computador o jogador A.

while True:
    num_a = int(input("Introduza o numero A"))

    if 1 <= num_a <= 100:
        break


while True:
    num_b = int(input("Introduza o numero B"))

    if num_b < num_a:
        print("Numero abaixo")

    if num_b > num_a:
        print("numero acima")

    elif num_b == num_a:
        print("Acertaste o numero")
        break