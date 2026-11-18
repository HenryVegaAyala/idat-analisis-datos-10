import numpy as np

lista = [15, 20, 18, 12, 30, 25]

vector = np.array(lista)

enmascarado = (vector >= 18) & (vector < 25)

resulado = vector[enmascarado]
print(resulado)