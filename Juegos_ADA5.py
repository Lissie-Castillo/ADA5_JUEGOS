import random

def dado():
    a = [1, 2, 3, 4, 5, 6]
    print(f"Gira gira gira... tu número de la suerte es: {random.choice(a)}")

def moneda():
    a = random.randint(1, 2)
    if a == 1:
        print("Gira gira gira... tu lado de la suerte es: Cara")
    else:
        print("Gira gira gira... tu lado de la suerte es: Cruz")

opcion=""
while opcion != "3":
    opcion = input("¿Estás listo para jugar?\nSelecciona el juego de tu preferencia:\n1. Dado\n2. Moneda\n3. Salir\n")

    if opcion == "1":
        dado()
    elif opcion == "2":
        moneda()
    elif opcion == "3":
        print("¡Gracias por jugar! Hasta luego. 👋")
    else:
        print("Opción no válida, por favor elige 1, 2 o 3.")

