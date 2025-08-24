def productoMasCaro(productos):
    masCaro = productos[0]

    for producto in productos:
        if producto[1] > masCaro[1]:
            masCaro = producto
    return masCaro




productos = [ ("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30) ]

resultado = productoMasCaro(productos)

print(f"El producto mas caro es {resultado}")