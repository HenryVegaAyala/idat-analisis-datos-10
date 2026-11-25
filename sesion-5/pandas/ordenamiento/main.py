import pandas as pd
from pathlib import Path

archivo = Path(__file__).parent.parent / "database" / "ventas_enero.csv"

df = pd.read_csv(archivo)

resultado = df.sort_values(["vendedor", "precio_unitario"], ascending=[True, False])

print(resultado)

resultado.to_csv("C:\\resultados\\resultado.csv", index=False)
resultado.to_excel("C:\\resultados\\resultado.xlsx", index=False)