costo_4h = 6
costo_adic = 2
total = None
horas = int(input("Horas: "))

if horas <= 4:
    total = costo_4h 
    print("Importe a pagar = S/.", total)
else:
    horas_adic = horas - 4
    total = costo_4h + (horas_adic * costo_adic)
    print("Importe a pagar = S/.", total)

