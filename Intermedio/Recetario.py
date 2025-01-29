
##### Recetario #####

import os
from pathlib import Path
from os import system

def limpiar_pantalla():
    return system('cls')


mi_ruta = Path("C:/Recetas/Recetas")
def contar_recetas(ruta):
    contador = 0
    lista_txt = []
    for txt in Path(ruta).rglob("**/*.txt"):
        contador += 1
        lista_txt.append(txt)
    print(F"Lista de Recetas: {lista_txt}\n\n")
    return contador

def inicio():
    limpiar_pantalla()
    print('*' * 50)
    print('*' * 5 + " ¡Bienvenido al Administrador de Recetas! " + '*' * 5)
    print('*' * 50)
    print('\n')
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"Total recetas: {contar_recetas(mi_ruta)}")

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 7):
        print("Elige una opción:")
        print("""
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoría nueva
        [4] - Eliminar receta
        [5] - Eliminar categoría
        [6] - Salir del programa""")
        eleccion_menu = input()
        limpiar_pantalla()
    return int(eleccion_menu)


def mostrar_categorias(ruta):
    print("Categorías:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        lista_categorias.append(carpeta)
        contador += 1
    return lista_categorias


def elegir_categoria(lista):
    eleccion_correcta = 'x'
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElige una categoría: ")
    return lista[int(eleccion_correcta) - 1]


def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1

    return lista_recetas



def elegir_recetas(lista):
    eleccion_receta = 'x'
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista) + 1):
        eleccion_receta = input("\nElige una receta: ")
    return lista[int(eleccion_receta) - 1]


def leer_receta(receta):
    print(Path.read_text(receta))


def crear_receta_nueva(ruta):
    exists = False

    while not exists:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + '.txt'
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada.")
            exists = True
        else:
            print("Lo siento. esa receta ya existe")



def crear_categoria_nueva(ruta):
    exists = False

    while not exists:
        print("Escribe el nombre de la nueva categoría: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu nueva categoría {nombre_categoria} ha sido creada.")
            exists = True
        else:
            print("Lo siento. esa categoría ya existe.")


def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada.")


def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f"La categoría {categoria.name} ha sido eliminada.")


def volver_al_inicio():
    eleccion_regresar = 'x'
    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\nPresione V para volver al menú.")




finalizar_programa = False

# Mostrar menú inicio

while not finalizar_programa:

    menu = inicio()

    if menu == 1:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("No hay recetas en esta categoría.")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            leer_receta(mi_receta)
        volver_al_inicio()


    elif menu == 2:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta_nueva(mi_categoria)
        volver_al_inicio()


    elif menu == 3:
        crear_categoria_nueva(mi_ruta)
        volver_al_inicio()


    elif menu == 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print("Lo siento, esta categoría está vacía.")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            eliminar_receta(mi_receta)
        volver_al_inicio()


    elif menu == 5:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_al_inicio()


    elif menu == 6:
        # Finalizar el programa
        finalizar_programa = True
