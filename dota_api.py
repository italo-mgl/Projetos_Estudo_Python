import requests
import pandas as pd


url = "https://api.opendota.com/api/heroes"

resp = requests.get(url)

df = pd.DataFrame(resp.json())

df.to_csv("heroes.csv", sep=";")
