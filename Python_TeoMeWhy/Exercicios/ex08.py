fruta = input("Entre com o nome da fruta:")

frutas = {
    "Pera": "R$1,50",
    "Goiaba": "R$2,15",
    "Abacaxi": "R$1,50",
    "Jaca": "R$1,50",
    "Laranja": "R$1,50",
    "Limão": "R$1,50",
    "Maçã": "R$1,50",
    "Banana": "R$1,50",
    "Uva": "R$1,50",
}

if fruta in frutas:
    print(frutas[fruta])
else:
    print("Entre com um valor válido!!")