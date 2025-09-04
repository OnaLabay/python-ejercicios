
def analizar_finanzas(**kwargs):
    balance = sum(kwargs.values())
    return balance

balance = analizar_finanzas(sueldo= 2000, renta= -800, transporte= -150, comida= -300, freelance= 500)

print(f"El balance total es de: {balance}")