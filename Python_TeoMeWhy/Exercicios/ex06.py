lista = [1,1,1,3,3,2,4,65,2,1,3,2,2,2,4,4,4,4,4,6,6,7,8,8,7,4,2,4,6,9,0,0,0,2]

numero = int(input("Escolhe um numero: "))

contador = 0

for i in lista:
    if i == numero:
        contador +=1

print(f"O numero {numero} aparece {contador}x na lista!2")