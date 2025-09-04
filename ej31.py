
def publicar(usuario, texto, etiquetas=None, **kwargs):
    if etiquetas is None:
        etiquetas=[]

    publicacion = {
        "Usuario": usuario,
        "Texto": texto,
        "Etiquetas": etiquetas
    }

    for clave, valor in kwargs.items():
        publicacion[clave] = valor

    return publicacion

posteo = publicar(
    "Juan",
    "Mi primer post!", 
    etiquetas=["#hola", "#primerPost"],
    visibilidad="publica", likes=100
)

for clave, valor in posteo.items(): print(f"{clave}: {valor}")