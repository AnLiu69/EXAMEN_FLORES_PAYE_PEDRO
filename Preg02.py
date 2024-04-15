def suma_n_primeros_numeros(n):
    """
    Calcula la suma de los n primeros números naturales.
    :param n: Número de términos a sumar.
    :return: La suma total.
    """
    if n < 0:
        return "El número debe ser positivo."
    suma = (n * (n + 1)) // 2
    return f"La suma de los {n} primeros números es: **{suma}**."

# Ejemplo de uso
n = int(input("Ingresa un número entero positivo: "))
print(suma_n_primeros_numeros(n))