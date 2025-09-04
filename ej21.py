
puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78), ("Gonza", 88), ("Juana", 55), ("Clau", 100), ("Lu", 80)]

def ordenar(lista_puntuaciones):
    return sorted(lista_puntuaciones, key=lambda x: x[1], reverse=True)


resultado = ordenar(puntuaciones)
print(resultado)