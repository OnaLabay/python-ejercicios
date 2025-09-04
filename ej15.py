def calcular_promedio(*args):
    suma = sum(args)
    promedio = suma / len(args)
    return promedio

resultado = calcular_promedio(85, 90, 78, 92)

print(f"El promedio es: {resultado}")