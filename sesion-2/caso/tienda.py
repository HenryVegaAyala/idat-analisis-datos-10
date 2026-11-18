productos = ["Mouse", "Teclado", "Monitor"]
stock = [50,20,100]

# Primer paso saber cual es el stock maximo
maximo_stock = max(stock)
print(f"El stock maximo es: {maximo_stock}")

# Segundo paso saber cual es el indice
indice_maximo = stock.index(maximo_stock)
print(f"El indice del stock maximo es: {indice_maximo}")

# Tercer paso saber cual es el producto con mayor stock
producto = productos[indice_maximo]
print(f"El producto con mayor stock es: {producto}")