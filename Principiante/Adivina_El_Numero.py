# Proyecto 2

# Objetivo: Juego 'Adivina el número'

# Contexto: Se le pedirá al usuario su nombre y, a continuación, se le pedirá que adivine
# un número entero entre el 1 y el 100, y solo tendrá 8 intentos.

# El programa puede pedir cuatro cosas distintas:

   # - 1: Si el usuario introduce un número menor que 1 o mayor de 100, el programa dirá
   # algo como "eso no está permitido".

   # - 2: Si el usuario introduce un número menor al correcto, saltará un error.

   # - 3: Si el usuario introduce un número mayor al correcto, saltará un error.

   # - 4: Si el usuario introduce el número correcto, ganará el juego y el programa dirá cuántos intentos tomó al usuario adivinar el número.

   # - 5: Si el usuario gasta sus 8 intentos, perderá y el programa se cerrará.


# Librerías necesarias
from time import sleep
from random import randint



# Código introductorio
nombre_usuario = input("Ponga su nombre: ")
sleep(1.5)

print(f"Hola, {nombre_usuario}. ¡Bienvenido/a al juego 'Adivina el Número'!")
sleep(1.75)

print("A continuación, se generará el número aleatorio que tienes que adivinar")
sleep(3)
numero_aleatorio = randint(1,100)

print("¡Número aleatorio generado con éxito!")
sleep(1.5)
print("¡A jugar!")
sleep(1.5)
print("¡Buena suerte! ☻")

# Código del programa
intentos = 0

# Main Loop
while intentos < 8:
    #print("Estamos dentro del bucle")
    numero_adivinado = int(input("Adivina el número: "))
    intentos += 1
    match numero_adivinado:
        case num if num < 1 or num > 100:
            print("[!!] ¡Número fuera de rango! Inténtalo de nuevo...")
        case num if num < numero_aleatorio:
            print("[!] El número introducido es menor al número aleatorio")
        case num if num > numero_aleatorio:
            print("[!] El número introducido es mayor al número aleatorio")
        case num if num == numero_aleatorio:
            print(f"¡Felicidades! ¡Has adivinado el número! Con {intentos} intentos")
            break
        case _:
            print("[@] No se reconoce ese formato de entrada")
            break
