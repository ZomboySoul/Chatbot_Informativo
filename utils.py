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
    print(Fore.YELLOW + f"{'==='} {titulo.upper()} {'==='}".center(60) + Fore.RESET)
    print()


def formatear_parrafo(texto, ancho=60):
    """
    Devuelve el texto dividido en líneas centradas de un ancho máximo.
    """
    import textwrap
    lineas = textwrap.wrap(texto, width=ancho)
    return [linea.center(ancho) for linea in lineas]
