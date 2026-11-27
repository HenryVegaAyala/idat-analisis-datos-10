import matplotlib.pyplot as plt

edades = [18, 22, 25, 30, 35, 40, 45, 50, 55, 60]

plt.hist(edades, bins=5, edgecolor="black", color="#66ccff")
plt.show()