import pandas as pd
from pathlib import Path

archivo = Path(__file__).parent.parent / "database" / "dataset.txt"

df = pd.read_csv(archivo)

print(df["Total Price"].head(5)) # Solo obtener 1 columna

print(df[["Total Price", "Base Price"]].head(5)) # Obtener varias columnas