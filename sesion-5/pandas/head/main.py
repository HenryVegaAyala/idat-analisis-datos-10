import pandas as pd
from pathlib import Path

# Path(__file__) = Ayuda a obtener la ruta del archivo actual
# parent = Obtiene el directorio padre
# parent.parent = subir a un nivel

archivo = Path(__file__).parent.parent / "database" / "dataset.txt"

df = pd.read_csv(archivo)

print(df.head(10))  # Muestra las primeras 10 filas del DataFrame