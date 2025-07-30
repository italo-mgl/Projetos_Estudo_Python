dados = {}

while True:
    frase = input("Entre com uma frase: ")
    if frase == "":
        break

    if frase not in dados:
        dados[frase]= 1
    else:
        dados[frase] += 1


for i, j in dados.items():
    print(i,"->", j)