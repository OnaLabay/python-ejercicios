
hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"]
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]

def hashtags_populares(hashtags, tendencias, umbral):
    resultado = []
    for hashtag, frecuencia in tendencias:
        if frecuencia > umbral:
            resultado.append(hashtag)
    return resultado

tendencia = hashtags_populares(hashtags, tendencias, umbral=100)
print("Hashtags en tendencia:", tendencia)