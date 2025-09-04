
inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]

def actualizar_inventario(inventario, ventas):
    inventario_actualizado = []

    for x in range(len(inventario)):
        inventario_actualizado.append(inventario[x] - ventas[x])
    return inventario_actualizado

resultado = actualizar_inventario(inventario, ventas)

print(f"El inventario actualizado es: {resultado}") 
