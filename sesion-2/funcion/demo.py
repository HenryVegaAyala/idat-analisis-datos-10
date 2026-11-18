def calcular_sueldo(cantidad_horas, tarifa_hora):
    sueldo_total = cantidad_horas * tarifa_hora

    if sueldo_total > 1000:
        print("El sueldo es mayor a 1000, aplicando descuento del 9%")
        sueldo_total = sueldo_total - (sueldo_total * 0.9)  # Aplicar un descuento del 9% si el sueldo es mayor a 1000
    else:
        print("El sueldo es menor o igual a 1000, aplicando descuento del 5%")
        sueldo_total = sueldo_total - (sueldo_total * 0.05)  # Aplicar un descuento del 5% si el sueldo es menor o igual a 1000

    if cantidad_horas >= 80:
        print("Se trabajaron 80 horas o más, aplicando aumento del 20%")
        return sueldo_total * 1.2  # Aplicar un aumento del 20% si se trabajaron 80 horas o más

    return sueldo_total


colaborador_1 = calcular_sueldo(90, 15)  # Trabajó 90 horas a una tarifa de 15
print(f"El sueldo del colaborador 1 es: {colaborador_1}")