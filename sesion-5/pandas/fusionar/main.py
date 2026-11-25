import pandas as pd
from pathlib import Path

archivos_encontrados = Path(__file__).parent / "data"

ventas = pd.read_csv(archivos_encontrados / "clientes.csv")
facturas = pd.read_csv(archivos_encontrados / "facturacion.csv")
producto = pd.read_csv(archivos_encontrados / "producto.csv")

resultado = pd.merge(ventas, facturas, on="id_cliente", how="inner")
resultado = pd.merge(resultado, producto, on="id_factura", how="inner")

resultado["key"] = resultado["id_cliente"] + "-" + resultado["id_factura"]

resultado = resultado[resultado["key"] == "C001-F001"]

print(resultado.head(5))