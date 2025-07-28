# idade = 18

# if idade > 70:
#     print("Cuidado com a bebida, voce ta velho")

# elif idade >= 18:
#     print("Voce ja pode beber")

# elif idade>= 17:
#     print("Voce AINDA não pode beber mas está perto")

# else:
#     print("Voce não pode bebe")

texto = """
    Voce deseja:
    (1) - Garrfa de agua R$ 1,50
    (2) - Garrafa com agua mineral R$ 2,50
    Digite seu numero:
"""
opcao = input(texto)

valor_item = 0

if opcao == "1":
    valor_item = 1.5
elif opcao == "2":
    valor_item == 2.5

if valor_item == 0:
    print("Por gentileza, digite o codigo correto.")
else:
    qtde = input("Quantas garrafas?")
    qtde = int(qtde)
    valor_total = valor_item *qtde
    print("Sua conta deu: R$", valor_total)
    