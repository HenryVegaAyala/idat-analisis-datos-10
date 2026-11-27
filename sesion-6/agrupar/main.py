import pandas as pd
from pathlib import Path

archivo = Path(__file__).parent / "data"

clientes = pd.read_csv(archivo / "clientes.csv")
facturacion = pd.read_csv(archivo / "facturacion.csv")

resultado = pd.merge(
    clientes,
    facturacion,
    on="id_cliente",
    how="inner"
)

agrupador = resultado.groupby("pais")["monto_total"].sum()
#print(agrupador)

agrupador = resultado.groupby("pais")["monto_total"].agg(
    ["sum", "mean", "count"]
)
#print(agrupador)

agrupador = resultado.groupby("pais").agg(
    cantidad=("id_cliente", "count")
).reset_index()

print(agrupador)