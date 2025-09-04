
usuarios = ["Ana", "Luis", "María"]


def configurar_perfiles(usuarios, **kwargs):
    perfiles = {}
    for usuario in usuarios: 
        configuraciones = [f"{clave}: {valor}" for clave, valor in kwargs.items()]
        perfiles[usuario] = configuraciones
    return perfiles

resultado = configurar_perfiles(usuarios, idioma="es", modo_oscuro=True, notificaciones=False)

for usuario, configuraciones in resultado.items():
    print(f"{usuario}: {configuraciones}")
    