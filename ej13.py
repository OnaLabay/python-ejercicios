
estudiantes = {
    101: {"nombre":"Ana", "edad":16, "calificaciones":{"matematicas":85, "ciencias":90}},
    102: {"nombre":"Luis", "edad":17, "calificaciones":{"matematicas":78, "ciencias":88}}
}

def promedio(registro, matricula):

    if matricula in registro: 
        calificaciones = registro[matricula]["calificaciones"]
        notas = calificaciones.values()
        promedio = sum(notas) / len(notas)
        return promedio
    
    else:
        return None
    

matricula = 102

resultado = promedio(estudiantes, matricula)
if resultado is not None:
    print(f"El promedio de {estudiantes[matricula]['nombre']} es {resultado:.2f}")
else: 
    print("Matricula no encontrada")