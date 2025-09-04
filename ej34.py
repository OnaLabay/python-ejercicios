
encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

def frecuencia_respuestas(encuestas):
    resultados = {}
    for pregunta, respuesta in encuestas.items():
        frecuencia = {}
        for respuesta in respuesta:
         if respuesta in frecuencia:
            frecuencia[respuesta] += 1
         else:
            frecuencia[respuesta] = 1
        resultados[pregunta] = frecuencia
    return resultados

frecuencia = frecuencia_respuestas(encuestas)

print("Análisis de encuestas")

for pregunta, freq in frecuencia.items():
    print(f"{pregunta}:")
    for respuesta, cantidad in freq.items():
        print(f"  Respuesta {respuesta}: {cantidad}")