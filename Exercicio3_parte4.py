# Exericio 3
# O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem
# do distribuidor e dos impostos (aplicados sobre o custo de fábrica). Supondo que a
# percentagem do distribuidor seja de 12% e os impostos de 45%, implemente um algoritmo
# que leia o custo de fábrica do carro e imprima o custo ao consumidor final.


custo_fabrica = int(input("Insira o custo de fabrica:"))

custo_consumidor = ((custo_fabrica * 0.12) + (custo_fabrica * 0.45 ) + custo_fabrica)

print(custo_consumidor)