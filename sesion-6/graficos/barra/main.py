import matplotlib.pyplot as plt

ciudades = ["Lima", "Arequipa", "Cusco", "Trujillo"]
ventas = [100, 150, 200, 300]

colores = []
for venta in ventas:
    if venta >= 150:
        colores.append("#b3fff0")
    elif venta >= 200:
        colores.append("#66ccff")
    else:
        colores.append("#ffb3cc")

plt.bar(ciudades, ventas, color=colores)

plt.title("Ventas por ciudad", fontsize=16, fontweight="bold")
plt.xlabel("Ciudades", fontsize=12)
plt.ylabel("Ventas", fontsize=12)

plt.grid(axis="y", linestyle="--", alpha=0.4)

plt.show()