dados_teo = {
    "Nome": "Teo",
    "Sobrenome": "Calvo",
    "Filhos": True,
    "Formação": ["Estatística", "Bigdata Datascience"],
    "Cargos": [
        {"nome": "ds jr.", "empresa": "tapps"},
        {"nome": "ds pl.", "empresa": "aps"},
        {"nome": "ds sr.", "empresa": "sas"},
        {"nome": "ds Head.", "empresa": "via varejo"},
    ]
}

print(dados_teo["Cargos"][-1]["empresa"])

## Adicionando novos dados

dados_teo["estado civil"] = "Casado"

print(dados_teo)

### Descobrindo quais são as chave


# print(dados_teo.keys())

# print(dados_teo.values())

# print("Itens:", dados_teo.items())

# contador = 0
# for i in dados_teo:
#     if i == "Filhos":
#         break

#     contador += 1

# print("O a chave Filho está na posição:", contador)

for i in dados_teo:
    print(i,"->", dados_teo[i])

for chave in dados_teo:
    print(chave, "->",dados_teo[chave])


for chave, valor  in dados_teo.items():
    print(chave,"->", valor)