import pandas as pd

df = pd.read_csv("data/raw/ofertas_laborales.csv")

print("Dimensiones originales:", df.shape)

print("\nInformación del dataset:")
print(df.info())

print("\nValores nulos por columna:")
print(df.isnull().sum())

print("\nCantidad de filas duplicadas:")
print(df.duplicated().sum())

df = df.drop_duplicates()

df.to_csv("data/processed/ofertas_laborales_limpias.csv", index=False, encoding="utf-8-sig")

print("\nDimensiones finales:", df.shape)
print("Dataset limpio exportado correctamente.")