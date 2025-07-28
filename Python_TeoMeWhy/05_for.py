nome = "Italo"

for i in nome:
    print(i)


#%%

numero = 1
max_numero = 10

for i in range(1,max_numero+1):
    print(numero, "X", i,"=", max_numero*i)
# %%

for i in range(4,101):
    if i % 4 == 0:
        print(i)
#%%
soma = 0
qtde_entradas = 4

for i in range(qtde_entradas):
    altura = input("Entre com a altura: ")
    altura =float(altura)
    soma += altura

print("Soma das alturas", soma)

#%%

nome = [31,231,54,2,3,1,53,2,1,312,231,123,]

for i in nome:
    print(i)