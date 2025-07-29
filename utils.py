def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calcula la distancia en kilómetros entre dos puntos GPS usando la fórmula de Haversine.

    Parámetros:
        lat1, lon1: Coordenadas del punto 1 (en grados decimales)
        lat2, lon2: Coordenadas del punto 2 (en grados decimales)

    Retorna:
        Distancia en kilómetros (float)
    """
    from math import radians, cos, sin, asin, sqrt

    R = 6371  # Radio de la Tierra en km

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    )
    c = 2 * asin(sqrt(a))

    return round(R * c, 3)
