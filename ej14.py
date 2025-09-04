
temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

def analisis_temp(datos):
    media = sum(datos) / len(datos)
    maxima = max(datos)
    minima = min(datos)

    return media, maxima, minima

media, maxima , minima = analisis_temp(temperaturas)

print("TEMPERATURAS DEL MES:")
print(f"La media es: {media:.2f}")
print(f"La máxima es: {maxima}")
print(f"La mínima es: {minima}")