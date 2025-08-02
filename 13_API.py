import requests
ceps = ["60540121", "60415580", "60540255"]

url = "https://viacep.com.br/ws/{cep}/json/"

response = requests.get(url)
dados = response.json()

print(dados)
