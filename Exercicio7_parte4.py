# Exercicio7

# Dados dois valores inteiros (a e b) efetue a sua troca. Escreva os valores de a e b antes e
# depois da troca.

valores = []
inver_valores = []

for i in range(2):
    temp = int(input("Insira valor"))
    valores.append(temp)


valores[0],valores[1] = valores[1],valores[0]



print(valores)

