"""
utils.py

Incluye funciones utilitarias generales, como la limpieza de pantalla
y la presentación de títulos seccionados de forma decorativa.
"""


import os
from colorama import Fore


def limpiar_pantalla():
    """Limpia la consola dependiendo del sistema operativo."""

    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_seccion(titulo):
    """Muestra un título centrado y decorado en pantalla para identificar secciones."""
    
    print()
    print(Fore.YELLOW + f"{titulo.upper():^60}")
    print()

