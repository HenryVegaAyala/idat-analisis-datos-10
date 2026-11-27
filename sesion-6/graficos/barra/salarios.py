import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

archivo = Path(__file__).parent / "data"

df = pd.read_csv(archivo / "salarios.csv")

nombre = df["nombre"]
sueldo = df["sueldo"]

plt.bar(nombre, sueldo)
plt.show()