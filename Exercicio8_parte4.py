# Exercicio8
# Dada uma determinada quantidade em dinheiro correspondente a um número inteiro de
# euros, determine o menor número de moedas e notas que perfaz essa quantia (considerar
# apenas os valores de 1, 2, 5, 10, 20 e 50 €).

dinheiro = int(input("Dinheiro:"))

notas_moedas = [50, 20, 10, 5, 2, 1]
notas_moedas_contador = [0, 0, 0, 0, 0, 0]


while dinheiro >= 50:
    dinheiro = dinheiro - 50
    notas_moedas_contador[0] += 1

while dinheiro >= 20:
    dinheiro = dinheiro - 20
    notas_moedas_contador[1] += 1

while dinheiro >= 10:
    dinheiro = dinheiro - 10
    notas_moedas_contador[2] += 1

while dinheiro >= 5:
    dinheiro = dinheiro - 5
    notas_moedas_contador[3] += 1

while dinheiro >= 2:
    dinheiro = dinheiro - 2
    notas_moedas_contador[4] += 1

while dinheiro >= 1:
    dinheiro = dinheiro - 1
    notas_moedas_contador[5] += 1


quantidade_notas = 0
quantidade_moedas = 0

for i in range(4):
    quantidade_notas = quantidade_notas + notas_moedas_contador[i]

for k in range(4,6):
    quantidade_moedas = quantidade_moedas + notas_moedas_contador[k]


print("Notas:", quantidade_notas, " Moedas:", quantidade_moedas)

