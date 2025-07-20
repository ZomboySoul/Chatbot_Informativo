"""
interfaz.py

Contiene las funciones de interacción con el usuario, como la pantalla de bienvenida,
la validación del nombre, el menú principal y la despedida personalizada.
"""


import re
from colorama import Fore, Style
from utils import limpiar_pantalla

def validar_nombre(nombre):
    """Valida que el nombre ingresado tenga al menos dos palabras y solo contenga letras, espacios y tildes."""
   
    patron_nombre = re.compile(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")
    return len(nombre.split()) >= 2 and patron_nombre.match(nombre)


def mostrar_bienvenida():
    """
    Solicita al usuario que ingrese su nombre y apellido, valida el formato,
    y muestra una pantalla de bienvenida personalizada.
    """

    limpiar_pantalla()

    print("")
    print("BIENVENIDO AL SISTEMA INFORMATIVO".center(60))
    print("DEL INSTITUTO SUPERIOR N°57".center(60))


    print(Fore.CYAN + "Instituto de Formación Docente y Técnica".center(60))
    print(Fore.CYAN + "'Juana Paula Manso'\n".center(60) + Style.RESET_ALL)

    print("-"*25)

    # Validación de entrada de datos del usuario 
    while True:
        nombre = input(Fore.WHITE + "👤 Ingrese su nombre y apellido para comenzar: ").strip().title()

        if validar_nombre(nombre):
            break
        else:
            print(Fore.RED + "⚠️ Ingrese nombre y apellido válidos (solo letras y al menos dos palabras)." + Style.RESET_ALL)


    limpiar_pantalla()
    
    print("")
    print(Fore.GREEN + f"¡Bienvenido/a, {nombre}!".center(60))
    print(Fore.GREEN + "Gracias por utilizar nuestro chatbot informativo.".center(60))
    print(Fore.GREEN + "Vamos a recorrer juntos la oferta académica 2025.".center(60))
    
    input("\nPresione Enter para continuar...")

    return nombre


def mostrar_menu():
    from colorama import Fore
    from utils import mostrar_seccion
    
    """Muestra las opciones disponibles del menú principal del sistema."""

    mostrar_seccion("INSTITUTO SUPERIOR N°57")
    print(Fore.YELLOW + " 'JUANA P. MANSO' ".center(60) + Style.RESET_ALL)
    print()
    opciones = [
        "Carreras disponibles 2025",
        "Información sobre duración y modalidad",
        "Contacto y ubicación",
        "Requisitos de inscripción",
        "Redes sociales",
        "Especialización en Enfermería en Salud Mental",
        "Salir"
    ]

    for i, opcion in enumerate(opciones, start=1):
        print(f"{Fore.CYAN}{i}. {Fore.WHITE}{opcion}")
    print()


def despedida(nombre_completo):
    """Muestra un mensaje de agradecimiento personalizado al finalizar el sistema."""

    limpiar_pantalla()
    print("")
    print(Fore.RED + f" {nombre_completo.upper()}, GRACIAS POR UTILIZAR NUESTRO SISTEMA ".center(60))
    print(Fore.RED +  " Instituto 57 'Juana P. Manso'\n ".center(60) + Fore.RESET)

