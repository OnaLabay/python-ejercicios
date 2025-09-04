
def registro_empleado(nombre, edad, salario, **kwargs):
    empleado = { 
        "Nombre": nombre,
        "Edad": edad,
        "Salario":salario
    }
    
    for clave, valor in kwargs.items():
        empleado[clave] = valor
    return empleado

empleado1 = registro_empleado("Ana", 30, 3000, Direccion="Calle Falsa 123", Telefono="123456789")
print(empleado1)
        