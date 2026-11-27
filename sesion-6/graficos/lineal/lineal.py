import matplotlib.pyplot as plt

ventas = [10,25,48,32,40]
horas = [1,2,3,4,5]

plt.plot(horas, ventas)

plt.title("Ventas por hora", fontsize=14, color="blue")
plt.xlabel("Horas")
plt.ylabel("Ventas")

# Mostrar valores en cada punto
for x, y in zip(horas, ventas):
    plt.text(x, y + 1, str(y), ha="center", va="bottom")

plt.grid()
plt.tight_layout()

plt.show()