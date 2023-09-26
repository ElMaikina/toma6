def calcular_probabilidades(cartas_mesa, cartas_en_mano):
    todas_las_cartas = set(range(1, 105))
    cartas_conocidas = set(cartas_mesa + cartas_en_mano)

    # Calcular las cartas desconocidas (que no están en la mesa ni en la mano)
    cartas_desconocidas = todas_las_cartas - cartas_conocidas

    # Calcular la probabilidad de que cada carta desconocida esté presente en las manos de otros jugadores
    probabilidad_cartas = {}
    for carta in cartas_desconocidas:
        probabilidad = sum(1 for mano in cartas_en_mano if mano == carta) / len(cartas_en_mano)
        probabilidad_cartas[carta] = probabilidad

    # Seleccionar la carta con la menor probabilidad
    mejor_carta = min(probabilidad_cartas, key=probabilidad_cartas.get)

    return mejor_carta

# Ejemplo de uso
cartas_mesa = [4, 1, 104, 69]
cartas_en_mano = [2, 3, 45, 50]
mejor_carta = calcular_probabilidades(cartas_mesa, cartas_en_mano)
print("La mejor carta para jugar es:", mejor_carta)

