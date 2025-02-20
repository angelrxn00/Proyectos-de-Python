# En una estructura de directorios, hay que encontrar números de serie repartidos por varios archivos, con el formato
# - [N] + [tres caracteres de texto] + [-] + [5 números]



# Para ello, necesitamos iterar de manera recursiva cada uno de los directorios, y leer los archivos para buscar
# ese patrón de números con RegEx (Regular Expressions), e iterar con os.walk()



# Para este proyecto, aplicaremos RegEx y unos módulos extra como 'datetime' para la fecha, 'time' para medir el
# tiempo de ejecución, y 'os' para poder interactuar con el sistema operativo



import os, time, re

from datetime import datetime

# Ponemos la fecha de hoy
print(f"Fecha de hoy: {datetime.now():%d-%m-%Y}") # Fecha formateada

# Inicio del tiempo de ejecución
inicio = time.time()


def iterar_dir():
    patron = r"N\w{3}-\d{5}"
    ruta = "C:\\CursosUdemy\\Dia9Curso_MasModulos\\Proyecto 9"

    for carpeta, subcarpeta, archivos in os.walk(ruta):

        for arch in archivos:

            ruta_unida = os.path.join(carpeta, arch)
            with open(ruta_unida, encoding="utf-8", errors="ignore") as f:

                contenido = f.read()

                verificar = re.findall(patron, contenido, re.DOTALL)

                if verificar:

                    print("-----------------------------")

                    print(f"{arch:<20} | {' | '.join(verificar):<20}")

# Fin de la ejecución del programa
fin = time.time()
iterar_dir()

# Hallamos cuánto tiempo demoró en ejecutarse la función
print(f"Tiempo de diferencia: {fin - inicio}")
