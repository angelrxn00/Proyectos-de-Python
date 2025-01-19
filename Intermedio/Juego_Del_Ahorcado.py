from random import choice

# --- List of available words ---
lista_palabras = [
    'caballo', 'plomo', 'empanada', 'pared', 'pesa', 'mesa', 'cilindro', 'campamento',
    'repoblar', 'inconsciente', 'errático', 'ciudadela', 'jungla', 'derecho', 'parafrasear',
    'enfrentamiento', 'trabajo', 'paciencia', 'esfuerzo', 'guardería', 'hiponatremia',
    'cienciología', 'ordenador', 'titulación', 'electrocardiograma', 'cerebro', 'sastre',
    'válvula', 'debilitamiento'
]

# --- Function Definitions ---

def escoger_palabra_de_lista(lista_palabras):
    """
    Selects a random word from the list of words and returns it as a list of characters.
    """
    palabra_al_azar = list(choice(lista_palabras))
    return palabra_al_azar


def generar_guiones_para_palabra(palabra_al_azar):
    """
    Generates a list of underscores representing the word.
    Each underscore corresponds to a letter in the word.
    """
    lista_guiones = ['_' for _ in palabra_al_azar]
    return lista_guiones


def pedir_y_validar_letra_al_usuario(palabra_al_azar, lista_guiones):
    """
    Handles user input, validates the guessed letter, and updates the state of the game.
    """
    intentos = 0

    while intentos < 7:
        # Ask the user for a letter
        letra = input("Escoge una letra: ").strip().lower()

        # Validate the input
        if len(letra) != 1:
            print("Error! Tienes que introducir una sola letra.")
            continue

        elif not letra.isalpha():
            print("Error! Solo se admiten letras.")
            continue

        # Check if the letter is in the word
        if letra not in palabra_al_azar:
            print(f"Letra no encontrada en la palabra! Inténtalo de nuevo.\n Intentos restantes: {6 - intentos}")
            intentos += 1
        else:
            print("Letra encontrada en la palabra! Continúa")
            # Update all positions where the letter matches
            positions = [i for i, char in enumerate(palabra_al_azar) if char == letra]
            for pos in positions:
                lista_guiones[pos] = letra

            # Display the current state of the word
            print(f"Estado de la palabra: {lista_guiones}")

            # Check if the user has guessed the entire word
            if lista_guiones == palabra_al_azar:
                print(f"¡Enhorabuena! Has adivinado la palabra! La palabra era: {''.join(palabra_al_azar)}! Te quedaban {6 - intentos} intentos.")
                return True

    print(f"[!] Intentos agotados. La palabra era: {''.join(palabra_al_azar)}. Suerte la próxima vez.")
    return False


def main():
    """
    Main game loop that ties everything together.
    """
    # Set the game up
    palabra_al_azar = escoger_palabra_de_lista(lista_palabras)
    lista_guiones = generar_guiones_para_palabra(palabra_al_azar)

    # Debugging: Uncomment this line to reveal the word
    # print(f"Palabra seleccionada: {''.join(palabra_al_azar)}")

    # Start the game
    pedir_y_validar_letra_al_usuario(palabra_al_azar, lista_guiones)


if __name__ == "__main__": #
    main()
