import pandas as pd
import glob
from pathlib import Path

archivos = Path(__file__).parent

# Obtener todos los archivos CSV en la carpeta "data"
buscar_archivos = glob.glob(str(archivos / "data" / "ventas_*.csv"))

print("Archivos encontrados:", len(buscar_archivos))

# Definir una variable para almacenar los DataFrames
dataframes = []

# Iterar sobre los archivos encontrados y leerlos en DataFrames
for archivo in buscar_archivos:
    print("Leyendo archivo:", archivo)
    df = pd.read_csv(archivo)

    # Agregar el DataFrame a la lista
    dataframes.append(df)

consolidado = pd.concat(dataframes, ignore_index=True)
respuesta_ordenada = consolidado.sort_values("fecha", ascending=False)

respuesta_ordenada.to_csv(archivos / "salida" / "resultado_automatizado.csv", index=False)
respuesta_ordenada.to_excel(archivos / "salida" / "resultado_automatizado.xlsx", index=False)