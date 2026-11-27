import matplotlib.pyplot as plt

tienda_a = [10,25,48,32,40]
tienda_b = [5,15,20,25,30]

plt.plot(tienda_a, label="Tienda A")
plt.plot(tienda_b, label="Tienda B")

plt.title("Ventas por hora", fontsize=14)
plt.xlabel("Horas")
plt.ylabel("Ventas")

plt.legend()
plt.show()