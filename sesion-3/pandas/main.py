import pandas as pd
from pathlib import Path

archivo = Path(__file__).parent / "clientes.csv"
df_csv = pd.read_csv(archivo)
print(df_csv.head())

archivo_excel = Path(__file__).parent / "Codigo de becas.xlsx"
df_excel = pd.read_excel(archivo_excel)
print(df_excel.head())
