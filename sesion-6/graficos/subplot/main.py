import matplotlib.pyplot as plt

plt.subplot(2, 2, 1)
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Gráfico 1")

plt.subplot(2, 2, 2)
plt.bar(["A", "B", "C"], [5, 7, 3])
plt.title("Gráfico 2")

plt.savefig("graficos.png", dpi=300)
plt.show()