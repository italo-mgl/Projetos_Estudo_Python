print("--"*15)
print("SEQUENCIA DE FIBONACCI")
print("--"*15)
sequencia = int(input("Quantos termos voce quer mostrar na sequencia? "))
t1 = 0
t2 = 1
print("~~"*15)
print(f"{t1} -> {t2} ->", end=" ")
contador = 3
while contador <= sequencia:
    t3 = t1 + t2
    print(f" {t3} -> ", end="")
    t1 = t2
    t2 = t3
    contador +=1
print("Finalizado")
print("~~"*15)