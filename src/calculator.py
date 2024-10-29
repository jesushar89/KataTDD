class NoSePuedeCalcular(Exception):
    pass

def media(elementos):
    if not elementos:
        raise NoSePuedeCalcular("La lista está vacía, no se puede calcular el promedio.")
    if any(not isinstance(i, (int, float)) for i in elementos):
        raise TypeError("Todos los elementos deben ser números.")
    return sum(elementos) / len(elementos)

def desviacion_estandar(elementos):
    if not elementos:
        raise NoSePuedeCalcular("La lista está vacía, no se puede calcular la desviación estándar.")
    if any(not isinstance(i, (int, float)) for i in elementos):
        raise TypeError("Todos los elementos deben ser números.")
    if len(elementos) == 1:
        return 0
    promedio = media(elementos)
    varianza = sum((x - promedio) ** 2 for x in elementos) / len(elementos)
    return varianza ** 0.5
