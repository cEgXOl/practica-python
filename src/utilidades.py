def calcular_importe(unidades, precio_unitario, descuento_pct=0):
    bruto = unidades * precio_unitario
    return round(bruto * (1 - descuento_pct / 100), 2)

def clasificar_ticket(importe):
    if importe < 100:
        return "Bajo"
    elif importe < 400:
        return "Medio"
    return "Alto"
