# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas.

c = n  = 0
while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        c += 1
        break
    c +=1

print(f"voce tentou {c} vezes.")
