from random import choice
from time import sleep
import sys

# --- Lista de palabras disponibles ---
lista_palabras = [
    'caballo', 'plomo', 'empanada', 'pared', 'pesa', 'mesa', 'cilindro', 'campamento', 
    'repoblar', 'inconsciente', 'errático', 'ciudadela', 'jungla', 'derecho', 'parafrasear', 
    'enfrentamiento', 'trabajo', 'paciencia', 'esfuerzo', 'guardería', 'hiponatremia', 
    'cienciología', 'ordenador', 'titulación', 'electrocardiograma', 'cerebro', 'sastre', 
    'válvula', 'debilitamiento'
]

# --- Definición de funciones ---

def escoger_palabra_de_lista(lista_palabras):
    """
    Selecciona una palabra al azar de la lista de palabras y la retorna como una lista de caracteres.
    """
    return list(choice(lista_palabras))

def generar_guiones_para_palabra(palabra_al_azar):
    """
    Genera una lista de guiones bajos que representan la palabra.
    Cada guion corresponde a una letra de la palabra.
    """
    return ['_' for _ in palabra_al_azar]

def pedir_y_validar_letra_al_usuario(palabra_al_azar, lista_guiones):
    """
    Maneja el ingreso del usuario, valida la letra adivinada y actualiza el estado del juego.
    """
    intentos = 0

    while intentos < 7:
        # Pedir una letra al usuario
        letra = input("Escoge una letra: ").strip().lower()

        # Validar la entrada
        if len(letra) != 1:
            print("Error! Tienes que introducir una sola letra.")
            continue

        if not letra.isalpha():
            print("Error! Solo se admiten letras.")
            continue

        # Comprobar si la letra está en la palabra
        if letra not in palabra_al_azar:
            print(f"Letra no encontrada en la palabra! Inténtalo de nuevo.\n Intentos restantes: {6 - intentos}")
            intentos += 1
        else:
            print("Letra encontrada en la palabra! Continúa")
            # Actualizar todas las posiciones donde la letra coincide
            posiciones = [i for i, char in enumerate(palabra_al_azar) if char == letra]
            for pos in posiciones:
                lista_guiones[pos] = letra

            # Mostrar el estado actual de la palabra
            print(f"Estado de la palabra: {lista_guiones}")

            # Comprobar si el usuario ha adivinado toda la palabra
            if lista_guiones == palabra_al_azar:
                print(f"¡Enhorabuena! Has adivinado la palabra! Te quedaban {6 - intentos} intentos.")
                return True

    print(f"[!] Intentos agotados. La palabra era: {''.join(palabra_al_azar)}. Suerte la próxima vez.")
    return False

def main():
    """
    Función principal para orquestar el juego del ahorcado.
    """
    # Configurar el juego
    palabra_al_azar = escoger_palabra_de_lista(lista_palabras) # Argumento de la función declarado explícitamente, al ser referenciado y almacenado en la variable.
    lista_guiones = generar_guiones_para_palabra(palabra_al_azar) # Argumento de la función declarado explícitamente, al ser referenciado y almacenado en la variable.

    # Debugging: Descomenta esta línea para revelar la palabra
    # print(f"Palabra seleccionada: {''.join(palabra_al_azar)}")

    # Iniciar el juego
    pedir_y_validar_letra_al_usuario(palabra_al_azar, lista_guiones)

# Ejecutar el programa si se ejecuta directamente
if __name__ == "__main__":
    main()

