import pandas as pd
from pathlib import Path

archivo = Path(__file__).parent / "database"

df_enero = pd.read_csv(archivo / "ventas_enero.csv")
df_febrero = pd.read_csv(archivo / "ventas_febrero.csv")

resultado = pd.concat([df_enero, df_febrero], ignore_index=True)

resultado.to_csv(archivo / "resultado.csv", index=False)