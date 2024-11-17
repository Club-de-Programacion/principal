import random

def jugar():
    print("¡Bienvenido al juego de adivinanza!")
    print("Estoy pensando en un número entre 1 y 100. ¡Intenta adivinarlo!")

    # Número aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    while not adivinado:
        try:
            # Pedir al jugador que ingrese su suposición
            intento = int(input("Introduce tu número: "))
            intentos += 1

            # Comprobamos si el número es correcto
            if intento < numero_secreto:
                print("El número es más grande.")
            elif intento > numero_secreto:
                print("El número es más pequeño.")
            else:
                print(f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
                adivinado = True
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    # Opción para jugar nuevamente
    jugar_otra_vez = input("¿Quieres jugar otra vez? (sí/no): ").strip().lower()
    if jugar_otra_vez == 'sí' or jugar_otra_vez == 'si':
        jugar()
    else:
        print("¡Gracias por jugar! Hasta la próxima.")

# Iniciar el juego
jugar()