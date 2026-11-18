import numpy as np

class Estudiante:
    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = np.array(notas)

    def calcular_promedio(self):
        return np.mean(self.notas)

    def evaluar(self):
        promedio = self.calcular_promedio()

        if promedio >= 13:
            resultado = f"{self.nombre} ha aprobado con un promedio de {promedio:.2f}."
        else:
            resultado = f"{self.nombre} ha reprobado con un promedio de {promedio:.2f}."

        return resultado

pedro = Estudiante("Pedro", [12, 14, 15, 10, 13])
resultado = pedro.evaluar()
print(resultado)