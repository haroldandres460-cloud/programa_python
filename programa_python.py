"""Clasifica el nivel de compromiso de sesiones."""

matriz_sesiones = [
    ["C001", 200, 10],  # D > 180 y C > 8   -> Alto
    ["C002", 45, 5],    # D < 60            -> Bajo
    ["C003", 120, 6],   # Demás casos       -> Medio
    ["C004", 150, 2],   # C < 3             -> Bajo
    ["C005", 190, 4]    # Demás casos       -> Medio
]


def clasificar_compromiso(duracion, clics):
    """Evalúa el nivel de compromiso basándose en duración y clics."""
    if duracion > 180 and clics > 8:
        return "Alto"
    if duracion < 60 or clics < 3:
        return "Bajo"
    return "Medio"


def generar_informe(sesiones):
    """Genera las líneas de texto del informe de clasificación."""
    encabezado = f"{'ID Cliente':<12} | Clasificación Final"
    separador = "-" * len(encabezado)
    lineas = ["--- INFORME DE CLASIFICACIÓN DE SESIONES ---", encabezado, separador]

    for sesion in sesiones:
        id_cliente, duracion, clics = sesion
        clasificacion = clasificar_compromiso(duracion, clics)
        lineas.append(f"{id_cliente:<12} | {clasificacion}")

    return lineas


def imprimir_informe():
    """Imprime el informe final en pantalla."""
    for linea in generar_informe(matriz_sesiones):
        print(linea)


if __name__ == "__main__":
    imprimir_informe()
