import pandas as pd
from pathlib import Path

archivo = Path(__file__).parent.parent / "database" / "dataset.txt"

df = pd.read_csv(archivo)

print(df.info())