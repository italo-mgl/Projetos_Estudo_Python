# Construa um programa que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado.
# Caso o usuário acerte, dê os parabéns.



import random

def get_input():
    while True:
        try:
            numero_usuario = int(input("Entre com um numero: "))

        except ValueError as erro:
            print("Valor inválido, tente novamente!")
            continue

        if 1 <= numero_usuario <= 15:
            return numero_usuario

        print("Valor inválido! O valor deve ser entre 1 e 15.")

def check_numerbs(sorteio, usuario):

    if sorteio == usuario:
        print("Parabéns, voce se garantiu e acertou o numero!!")
        return True

    elif usuario > sorteio:
        print("Numero muito alto. Tente novamente com um menor!")

    else:
        print("Numero Muito baixo, tente com um numero maior!!")

numero_sorteio = random.randint(1,15)

for i in range(3):

    numero_usuario = get_input()

    if check_numerbs(sorteio=numero_sorteio, usuario=numero_usuario):
        break

else:
    print("Suas tentativas acabaram!!")