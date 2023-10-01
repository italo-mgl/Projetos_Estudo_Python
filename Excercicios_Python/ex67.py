while True:
    n = int(input("Quer ver a tabuada de qual valor ?"))
    print("-" * 30)
    for c in range (1, 11):
        if n >= 0:
            print(f"{n} x {c} = {n * c}")
            c += 1
        else:
            print("Muito obrigado por usar a tabuada!!")
            break
    print("-" * 30)