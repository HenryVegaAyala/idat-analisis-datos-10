import pandas as pd
from pathlib import Path

archivo = Path(__file__).parent.parent.parent / "database" / "ventas_enero.csv"

df = pd.read_csv(archivo)

resultado = df[
    (df["precio_unitario"] > 1000) & (df["vendedor"] == "Ana")
    ]

print(resultado)