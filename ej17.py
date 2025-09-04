
empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}

def filtrar_por_salario(empleados, salario_dado):
    resultado = {}

    for id_empleado, info in empleados.items():
        nombre, edad, salario = info
        if salario > salario_dado:
            resultado[id_empleado] = info 
    return resultado

salario_dado = 2600

empleados_filtrados = filtrar_por_salario(empleados, salario_dado)

print(f"Empleados que ganan mas de {salario_dado}: ")
for id_empleado, info in empleados_filtrados.items():
    print(f"ID: {id_empleado}, Nombre: {info[0]}, Edad: {info[1]}, Salario: {info[2]}")

        
