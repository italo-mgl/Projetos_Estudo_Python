
numero_sorteio = 7
numero_usuario = int(input("Entre com um valor: "))
contador = 1
while numero_sorteio != numero_usuario and contador < 3:
    if numero_usuario > numero_sorteio:
        print("Numero acima do valor, tente novamente.")
    else:
        print("Numero muito baixo. Tente novamente.")
    numero_usuario = int(input("Entre com um valor: "))
    contador += 1
if numero_sorteio == numero_usuario:
    print("Parabéns! Você acertou o numero premiado.")
else:
    print("Suas tentativas acabaram. O número premiado era", numero_sorteio)


#######

numero_sorteio = 7

for i in range(3):
    
    numero_usuario = int(input("Entre com um numero: "))
    if not 1 <= numero_usuario <-= 15:
        continue

    if numero_sorteio == numero_usuario:
        print("Parabéns, voce se garantiu e acertou o numero!!")
        break

    elif numero_usuario > numero_sorteio:
        print("Numero muito alto. Tente novamente com um menor!")

    else:
        print("Numero Muito baixo, tente com um numero maior!!")

else:
    print("Suas tentativas acabaram!!")