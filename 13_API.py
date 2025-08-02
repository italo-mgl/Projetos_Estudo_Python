import requests
import json
from tqdm import tqdm
import pandas as pd


ceps = ["60540121", "60415580", "60540255"]

url = "https://viacep.com.br/ws/{cep}/json/"

dados = []

for i in tqdm(ceps):
    response = requests.get(url.format(cep=i))
    if response.status_code == 200:
        dados.append(response.json())


dataset = pd.DataFrame(dados)
dataset.to_csv("ceps.csv", sep=";" )

with open("ceps.json", "w", encoding='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)


