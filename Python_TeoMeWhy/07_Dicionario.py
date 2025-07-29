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

### Descobrindo quais são as chaves


print(dados_teo.keys())