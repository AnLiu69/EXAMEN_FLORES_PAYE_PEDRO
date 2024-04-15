def calcular_porcentaje(cantidad):
    
    
    if cantidad <= 0:
        return "La cantidad debe ser mayor que 0."
    elif cantidad <= 1000:
        porcentaje = 5
    elif cantidad <= 1500:
        porcentaje = 7
    elif cantidad <= 2000:
        porcentaje = 8
    elif cantidad <= 5000:
        porcentaje = 10
    else:
        porcentaje = 15

    resultado = cantidad * porcentaje / 100
    return f"El {porcentaje}% de {cantidad} es: **{resultado:.2f}**."

try:
    cantidad_ingresada = float(input("Ingresa una cantidad: "))
    print(calcular_porcentaje(cantidad_ingresada))
except ValueError:
    print("Ingresa un número válido.")