def convertir_a_dolares(soles, tipo_cambio=3.75):
    dolares = soles / tipo_cambio
    return dolares


# Posicionales
posicional_correcto = convertir_a_dolares(1000, 3.75)
posicional_incorrecto = convertir_a_dolares(3.75, 1000)

print(posicional_correcto)
print(posicional_incorrecto)

# Valor por defecto

valor_por_defecto = convertir_a_dolares(1000)
valor_por_defecto_cambiado = convertir_a_dolares(1000, 3.90)

print(valor_por_defecto)
print(valor_por_defecto_cambiado)

# Nombrados
valor_nombrado = convertir_a_dolares(soles=1000, tipo_cambio=3.75)
valor_nombrado_otro = convertir_a_dolares(tipo_cambio=3.75, soles=1000)

print(valor_nombrado)
print(valor_nombrado_otro)