"""
# >>> Se actualizará periódicamente
#############################################################################
Analizador de texto 
----------------------------------------------------------------------------------
El objetivo del proyecto es que, mediante un texto cualquiera que el usuario introduzca y después 3 letras a su elección, analicemos estos 5 casos:
    - Cuántas veces aparece cada letra (elegida anteriormente), solo minúsculas
    - Cuántas palabras hay en total
    - Mostrar la primera y la última letra
    - Mostrar las palabras en orden inverso
    - Y, por último, si en el texto aparece la palabra 'python'

"""

# Le decimos al usuario que escriba un texto cualquiera para operar sobre él.
texto_a_introducir = input("Introduce tu texto: ")

# Le decimos al usuario que indique 3 letras de su elección, para poder luego contar cuántas veces aparece en el texto cada una de ellas.
letras = []
letras.append(input("Escribe la primera letra: ").lower())
letras.append(input("Escribe la segunda letra: ").lower())
letras.append(input("Escribe la tercera letra: ").lower())

# Contamos cuántas veces aparece cada letra introducida anteriormente para comunicárselo al usuario.
print(f"La letra '{letras[0]}' aparece {texto_a_introducir.count(letras[0],0)} veces. "
      f"La letra '{letras[1]}' aparece {texto_a_introducir.count(letras[1],0)} veces. "
      f"La letra '{letras[2]}' aparece {texto_a_introducir.count(letras[2],0)} veces.\n")

# Le mostramos al usuario el texto introducido en forma de lista y dividido y la longitud del mismo.
lista_de_palabras = texto_a_introducir.split()
print(f"Texto dividido en elementos de lista: {lista_de_palabras}",'\n', f"Longitud del texto: {(len(lista_de_palabras))} palabras")

# Mostramos al usuario la primera y la última letra del texto introducido.
print(f"-- Primera letra introducida en el texto: \n{texto_a_introducir[0]}\n "
    f"-- Última letra introducida en el texto: \n{texto_a_introducir[-1]}\n")

# Mostramos al usuario su texto introducido pero en orden invertido.
print(f"Texto introducido pero en orden invertido: {texto_a_introducir[::-1]}")

# Mostramos al usuario si el texto contiene la palabra 'python' o no.
print(f"Verificación de si el texto introducido por el usuario contiene la palabra 'python': {bool('python' in texto_a_introducir)}")
