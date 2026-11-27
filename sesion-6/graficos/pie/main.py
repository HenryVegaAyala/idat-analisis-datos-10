import matplotlib.pyplot as plt

canales = ["Canal 1", "Canal 2", "Canal 3", "Canal 4"]
ventas = [100, 150, 200, 300]

plt.pie(ventas, labels=canales, autopct="%1.2f%%")
plt.show()