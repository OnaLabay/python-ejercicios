
ventas_diarias = [200, 450, 300, 400, 350, 500, 600]

def total_y_promedio_ventas(ventas_diarias):
    total = sum(ventas_diarias)
    promedio = total // len(ventas_diarias)
    return total, promedio

total, promedio = total_y_promedio_ventas(ventas_diarias)

print(f"La suma de las ventas diarias es de: {total}")
print(f"El promedio de las ventas diarias es de: {promedio}")