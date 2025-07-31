"""
interfaz.py

Contiene las funciones de interacción con el usuario, como la pantalla de bienvenida,
la validación del nombre, el menú principal y la despedida personalizada.
"""


import re
import time
from colorama import Fore, Style
from utils import limpiar_pantalla


def validar_nombre(nombre):
    """Valida que el nombre ingresado tenga al menos dos palabras y solo contenga letras, espacios y tildes."""
   
    patron_nombre = re.compile(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")
    return len(nombre.split()) >= 2 and patron_nombre.match(nombre) is not None


def escribir_lento(texto, delay=0.03):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(delay)
    print()


def mostrar_bienvenida():
    """
    Solicita al usuario que ingrese su nombre y apellido, valida el formato,
    y muestra una pantalla de bienvenida personalizada.
    """

    limpiar_pantalla()

    marco = f"{Fore.BLUE}{'*' * 60}{Style.RESET_ALL}"
    print("\n" + marco)
    print(Fore.CYAN + f"{'BIENVENIDO/A AL SISTEMA INFORMATIVO':^60}")
    print(f"{'INSTITUTO SUPERIOR N°57 “Juana Paula Manso”':^60}" + Style.RESET_ALL)
    print(marco + "\n")


    escribir_lento(Fore.YELLOW + "🤖 ¡Hola! Soy tu asistente virtual del Instituto 57.".center(60))
    escribir_lento("Te acompañaré para conocer toda la información de carreras 2025.\n".center(60) + Style.RESET_ALL)

    # Validación de nombre
    while True:
        nombre = input(Fore.WHITE + "👤 Ingrese su nombre: ").strip().title()
        apellido = input(Fore.WHITE + "👤 Ingrese su apellido: ").strip().title()
        nombreCompleto = nombre + " " + apellido

        if validar_nombre(nombreCompleto):
            break
        else:
            print(Fore.RED + "⚠️ Ingrese nombre y apellido válidos (solo letras y al menos dos palabras)." + Style.RESET_ALL)

    limpiar_pantalla()
    
    escribir_lento(Fore.GREEN + f"¡Bienvenido {nombreCompleto}".center(60))
    escribir_lento(Fore.GREEN + "Gracias por utilizar nuestro chatbot informativo".center(60))
    escribir_lento(Fore.GREEN + "Vamos a recorrer juntos la oferta académica 2025".center(60) + Style.RESET_ALL)
    
    print(Fore.LIGHTWHITE_EX + "\nIniciando el sistema, por favor espere..." + Style.RESET_ALL)
    time.sleep(3) 
    limpiar_pantalla()

    return nombreCompleto


def mostrar_menu():
    from colorama import Fore
    from utils import mostrar_seccion
    import readchar

    """Muestra las opciones disponibles del menú principal del sistema."""
    
    opciones = [
        "Carreras disponibles 2025",
        "Contacto y ubicación",
        "Requisitos de inscripción",
        "Salir"
    ]

    indice = 0
    while True:
        limpiar_pantalla()

        mostrar_seccion("INSTITUTO SUPERIOR N°57")
        print(Fore.YELLOW + "JUANA P. MANSO\n".center(60) + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + "Usá ↑ ↓ y presioná Enter para seleccionar".center(60) + Style.RESET_ALL)
        print()

        for i, opcion in enumerate(opciones):
            if i == indice:
                print(Fore.GREEN + f"> {opcion}".center(60) + Style.RESET_ALL)
            else:
                print(f"  {opcion}".center(60))
        
        tecla = readchar.readkey()
        if tecla == readchar.key.UP:
            indice = (indice - 1) % len(opciones)
        elif tecla == readchar.key.DOWN:
            indice = (indice + 1) % len(opciones)
        elif tecla == readchar.key.ENTER:
            return str(indice + 1)


def despedida(nombre_completo):
    """Muestra un mensaje de agradecimiento personalizado al finalizar el sistema."""

    limpiar_pantalla()
    print("\n")
    print(Fore.RED + "✨" + " " * 5 + f"¡GRACIAS POR UTILIZAR NUESTRO SISTEMA, {nombre_completo.upper()}!".center(50) + " " * 5 + "✨")
    print(Fore.RED + " " * 10 + "Instituto 57 'Juana P. Manso'".center(50) + "\n" + Style.RESET_ALL)

    print(Fore.LIGHTBLACK_EX + "Cerrando sesión", end="", flush=True)
    for _ in range(5):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print("\n" + Style.RESET_ALL)
    time.sleep(2)
    limpiar_pantalla()