

nome = input("Introduza o nome:")


ultimo = nome.rfind(" ")
nome_batismo = nome[:ultimo]
sobrenome = nome[ultimo+1:]

print(sobrenome + ", " + nome_batismo)