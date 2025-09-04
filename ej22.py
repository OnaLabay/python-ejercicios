
paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

def crear_diccionario(paquetes):
    diccionario = {}
    for destino, precio, dias in paquetes:
        diccionario[destino] = precio * dias
    return diccionario
    
print(crear_diccionario(paquetes))