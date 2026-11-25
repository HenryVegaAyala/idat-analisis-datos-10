import pandas as pd
from pathlib import Path

archivo = Path(__file__).parent.parent / "database" / "ventas_enero.csv"

df = pd.read_csv(archivo)

df["precio_total"] = df["cantidad"] * df["precio_unitario"]
df["valoracion"] = 5

print(df.head(2))

df.rename(columns={"valoracion": "calificacion"}, inplace=True)

print(df.head(2))