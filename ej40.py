
estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

def ranking_estudiantes(estudiantes):
    promedios = {}
    
    for id_est, materias in estudiantes.items():
        todas_notas = []
        for notas in materias.values():
            todas_notas.extend(notas)
        promedio_general = sum(todas_notas) / len(todas_notas)
        promedios[id_est] = round(promedio_general, 2)
    
    ranking = sorted(promedios.items(), key=lambda x: x[1], reverse=True)
    return ranking

ranking = ranking_estudiantes(estudiantes)
print("Ranking de estudiantes (ID, Promedio):")
for id_est, promedio in ranking:
    print(f"ID {id_est}: {promedio}")

