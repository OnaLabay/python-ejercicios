
def eventos(*args):
    print("Lista de eventos:")
    for x, evento in enumerate(args, start=1):
        print(f"{x}. {evento}")

eventos("Concierto", "Exposición de Arte", "Conferencia", "Recital", "Partido")