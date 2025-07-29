idades = [28, 42, 36, 64, 19, 29]

print(idades)

caracteristicas = ["Teo", 32, "Casado", 2341.98]

print(caracteristicas)

type(caracteristicas)

print(caracteristicas[2])

print(caracteristicas[0])

###

idades = [28, 42, 36, 64, 19, 29]

print("Soma idades:", sum(idades))

print(len(idades))
## Media

print("Media da lista: ", sum(idades) /len(idades))

## menor e maior valor

print("Menor idade:", min(idades))
print("Maior idade:", max(idades))


Teo = [
    "Teo Calvo",
    32,
    True,
    "Casado",
    ["Estagiario", "Junior", "Pleno", "Senior", "Head"],
    [1500, 4000, 4550, 6500, 10000],
    ["Ana", "Maria","Claudia"]
    ]

print(Teo[len(Teo)-1][0])

print(Teo[4][-2:])

print(Teo[5][::-1])