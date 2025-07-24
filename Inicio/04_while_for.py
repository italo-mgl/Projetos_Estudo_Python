numero = 2
count = 1

while count <= 2:
    print(numero, "X", count, "=", numero * count)
    count += 1
print("Acabou!")

divisor = 4
contagem = 4

while contagem <= 10:
    if contagem % divisor == 0:
        print(contagem, " é divisível por ", divisor)
    contagem += 1
print("Esses são todos os números divisíveis por", divisor,".")


soma = 0
qtde_entradas = 1

while qtde_entradas <= 4:
    altura = input("Entre com a altura:")
    altura = float(altura)
    soma += altura
    qtde_entradas += 1

print("Soma das alturas:", soma)


##
soma = 0
while True:
    valor = input("Digite um valor para que eu realize a soma:")

    if valor == "":
        break

    soma += float(valor)

print("A soma dos seus valores é:", soma)

