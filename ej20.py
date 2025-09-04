
def configurar_app(**kwargs):
    configuraciones = {}
    for clave, valor in kwargs.items():
        configuraciones[clave] = valor
    return configuraciones

configuracion = configurar_app(Modo_oscuro=True, Idioma="es", Notificaciones=False)

print("Se aplicaron las siguientes configuraciones: ")
for clave, valor in configuracion.items():
    print(f"{clave}: {valor}")
    