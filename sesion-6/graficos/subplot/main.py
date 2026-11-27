import matplotlib.pyplot as plt

plt.subplot(2, 2, 1)
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Gráfico 1")

plt.subplot(2, 2, 2)
plt.bar(["A", "B", "C"], [5, 7, 3])
plt.title("Gráfico 2")

plt.subplot(2, 2, 3)
plt.scatter([1, 2, 3], [1, 4, 9])
plt.title("Gráfico 3")

plt.subplot(2, 2, 4)
plt.pie([10, 20, 30], labels=["X", "Y", "Z"])
plt.title("Gráfico 4")

plt.savefig("graficos.png", dpi=300)
plt.show()