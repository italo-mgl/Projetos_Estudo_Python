A = 1 
B = 5

C = A
A = B
B = C

print(A)
print(B)

A, B = B,A 

print(A)
print(B)


dados = {"nome": "Itin", "Sobrenome": "negones"}

for i, j in dados.items():
    print(i, "->", j)


a, b, *resto = 1,2,3,45,51,12,2,31,31,23,54,13
print(a,b,resto)