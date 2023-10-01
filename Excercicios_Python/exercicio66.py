# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999
# No final, mostre quantos números foram digitados e qual foi a soma entre elas.

c = n = s = 0
while True:
    n = int(input("Digite um numero: "))
    if n == 999:
        c += 1
        break
    s += n
    c +=1

print(f"A soma dos numerod digitados foi de {s} e voce tentou {c} vezes.")
