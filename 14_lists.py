x = []

for i in range(1, 101):
    x.append(i)

print(x)

y = [i for i in range(1,101)]

print(y)


def par_ou_nao(x):
    return x % 2 == 0

z = [par_ou_nao(i) for i in range(1,101)]

print(z)


w = [i for i in range(1,101) if par_ou_nao(i)]