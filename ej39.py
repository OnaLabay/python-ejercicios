
precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

def simular_mercado(precios, operaciones):
    beneficio_total = 0
    accion_abierta = None 
    
    for op, dia in operaciones:
        precio = precios[dia]
        if op == "compra":
            accion_abierta = precio
        elif op == "venta":
            if accion_abierta is not None:
                beneficio_total += precio - accion_abierta
                accion_abierta = None
            else:
                print(f"Error: venta en día {dia} sin acción comprada.")
    
    return beneficio_total

resultado = simular_mercado(precios_diarios, operaciones)
print(f"Beneficio/Pérdida total: {resultado}")