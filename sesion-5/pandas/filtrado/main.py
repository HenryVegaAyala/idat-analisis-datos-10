import pandas as pd
from pathlib import Path

archivo = Path(__file__).parent.parent / "database" / "dataset.txt"

df = pd.read_csv(archivo)

resultado = df[
    (df["Store ID"] == 8095) & 
    (df["Total Price"] >= 100)
    ]

print(resultado)