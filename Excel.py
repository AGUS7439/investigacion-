import pandas as pd


df = pd.read_excel("datos.xlsx")

# Calcular el promedio de una columna
df["Promedio"] = df.mean(axis=1)

df.to_excel("resultado.xlsx", index=False)
