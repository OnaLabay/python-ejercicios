
suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}

def actualizar_suscripcion(usuario, suscripcion, **kwargs):
    if usuario not in suscripciones:
        suscripciones[usuario] = []
  
    if suscripcion not in suscripciones[usuario]:
        suscripciones[usuario].append(suscripcion)
  
    if kwargs:
        suscripciones[usuario + "_opciones"] = kwargs  
    
    return suscripciones

estado_actual = actualizar_suscripcion(usuario="Luis", suscripcion="mensual", auto_renovacion=True)
print(estado_actual)