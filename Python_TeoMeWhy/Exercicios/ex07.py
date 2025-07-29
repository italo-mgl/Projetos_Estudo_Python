idades = []

while True:
    idade = input("Entre com a idade:")

    if idade == "":
        break
    idades.append(int(idade))

print(idades)

print("A média é:", sum(idades)/len(idades))

print("O Valor máx é:", max(idades))

print("O valor minimo é:", min(idades))

print("Quantidade de valores é: ", len(idades))