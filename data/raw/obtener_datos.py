import requests
import pandas as pd

url = "https://api.apify.com/v2/key-value-stores/crearcode~latam-tech-jobs/records/latest"

response = requests.get(url)
response.raise_for_status()

data = response.json()

df = pd.json_normalize(data)

df = df.head(1000)

df.to_csv("./ofertas_laborales.csv", index=False, encoding="utf-8-sig")

print("Datos obtenidos correctamente")
print("Cantidad de ofertas:", df.shape[0])
print("Cantidad de columnas:", df.shape[1])
print(df.head())