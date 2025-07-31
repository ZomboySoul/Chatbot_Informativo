"""
secciones.py

Agrupa todas las funciones asociadas a las distintas secciones informativas del menú,
como carreras, modalidades, requisitos, contacto, redes sociales y especialización.
"""
import time
import readchar
from utils import limpiar_pantalla, mostrar_seccion, formatear_parrafo
from datos import CARRERAS_INFO, CONTACTO, REQUISITOS
from colorama import Fore, Style


def mostrar_lista_carreras():
    """Imprime en pantalla una lista numerada de las carreras disponibles con su duración."""

    for i, carrera in enumerate(CARRERAS_INFO, start=1):
        print(f"{Fore.CYAN}{i}. {Fore.WHITE}{carrera['nombre']} {Fore.LIGHTBLACK_EX}({carrera['duracion']}){Style.RESET_ALL}")


def seleccionar_carrera():
    """
    Solicita al usuario un número de carrera.
    Retorna el diccionario de la carrera seleccionada o None si desea volver al menú.
    """

    seleccion = input(Fore.YELLOW + "\nIngrese número de carrera (1-5): ").strip()
    if seleccion == '':
        return None
    elif seleccion.isdigit() and 0 < int(seleccion) <= len(CARRERAS_INFO):
        return CARRERAS_INFO[int(seleccion) - 1]
    else:
        print(Fore.RED + "\n⚠️ Opción no válida. Intente nuevamente.")
        input("Presione Enter para continuar..." + Style.RESET_ALL)
        return "reintentar"


def mostrar_detalle_carrera(carrera):
    """
    Muestra todos los detalles de una carrera específica, incluyendo plan de estudios.

    Parámetros:
    - carrera (dict): Diccionario con los campos 'nombre', 'descripcion', 'duracion', etc.
    """
    
    limpiar_pantalla()
    mostrar_seccion(carrera['nombre'])         

    print(Fore.CYAN + f"📝 Descripción: {Fore.WHITE}{carrera['descripcion']}")
    print(Fore.CYAN + f"⏳ Duración: {Fore.WHITE}{carrera['duracion']}")
    print(Fore.CYAN + f"📅 Inscripción: {Fore.WHITE}{carrera['inscripcion']}")
    print(Fore.CYAN + f"🏫 Modalidad: {Fore.WHITE}{carrera['modalidad']}")
    print(Fore.CYAN + f"📋 Requisitos: {Fore.WHITE}{carrera['requisitos']}")
    print(Fore.CYAN + "\n📚 Plan de estudios:" + Style.RESET_ALL)

    for materia in carrera['plan_estudio']:
        print(Fore.GREEN + f"   • {materia}")

    print()


def carrera():
    """Muestra las carreras una por una, con navegación y toda la información detallada."""

    total = len(CARRERAS_INFO)
    indice = 0

    limpiar_pantalla()
    print(Fore.LIGHTBLACK_EX + "Cargando Carreras disponibles", end="", flush=True)
    for _ in range(3):
        time.sleep(0.2)
        print(".", end="", flush=True)
    time.sleep(0.3)

    while True:
        limpiar_pantalla()

        carrera = CARRERAS_INFO[indice]

        # Mostrar detalles
        print(Fore.CYAN + carrera['nombre'].upper().center(60) + Fore.RESET)
        print()
        for linea in formatear_parrafo(carrera['descripcion']):
            print(Fore.WHITE + linea)
        print()

        print(Fore.CYAN + f"📅 Inscripción: {Fore.WHITE}{carrera['inscripcion']}")
        print(Fore.CYAN + f"⏳ Duración: {Fore.WHITE}{carrera['duracion']}")
        print(Fore.CYAN + f"🏫 Modalidad: {Fore.WHITE}{carrera['modalidad']}")
        print(Fore.CYAN + f"📋 Requisitos: {Fore.WHITE}{carrera['requisitos']}\n")

        print(Fore.CYAN + "📚 Plan de estudios:")
        for materia in carrera['plan_estudio']:
            print(Fore.GREEN + f"   • {materia}")


        print()
        
        print(Fore.YELLOW + f"← {indice + 1} / {total} →".center(60) + Style.RESET_ALL)

        # Leer tecla
        tecla = readchar.readkey()
        if tecla == readchar.key.RIGHT:
            indice = (indice + 1) % total
            print(Fore.LIGHTBLACK_EX + "\nCambiando carrera", end="", flush=True)
            for _ in range(3):
                time.sleep(0.2)
                print(".", end="", flush=True)
            time.sleep(0.2)
        elif tecla == readchar.key.LEFT:
            indice = (indice - 1) % total
            print(Fore.LIGHTBLACK_EX + "\nCambiando carrera", end="", flush=True)
            for _ in range(3):
                time.sleep(0.2)
                print(".", end="", flush=True)
            time.sleep(0.2)
        elif tecla == readchar.key.ESC:
            return


def contacto():
    """Muestra la información de contacto del instituto con diseño visual y transición."""
    limpiar_pantalla()

    print(Fore.LIGHTBLACK_EX + "Cargando información de contacto", end="", flush=True)
    for _ in range(3):
        time.sleep(0.2)
        print(".", end="", flush=True)
    time.sleep(0.3)

    limpiar_pantalla()
    mostrar_seccion("CONTACTO INSTITUCIONAL")

    print(Fore.YELLOW + "📍 Dirección:" + Fore.WHITE, CONTACTO['direccion'])
    print(Fore.YELLOW + "📞 Teléfono:" + Fore.WHITE, CONTACTO['telefono'])
    print(Fore.YELLOW + "✉️ Email:" + Fore.WHITE, CONTACTO['email'])
    print(Fore.YELLOW + "🌐 Sitio Web:" + Fore.CYAN, CONTACTO['web'])
    print()

    print(Fore.CYAN + "👍 Facebook:" + Fore.WHITE, CONTACTO['redes']['facebook'])
    print(Fore.CYAN + "📸 Instagram:" + Fore.WHITE, CONTACTO['redes']['instagram'])
    twitter = CONTACTO['redes'].get('twitter', 'No disponible')
    print(Fore.CYAN + "🐦 Twitter:" + Fore.WHITE, twitter)

    input(Fore.LIGHTWHITE_EX + "\nPresione Enter para volver al menú...")


def requisitos():
    """Muestra los requisitos de inscripción con estilo de checklist y transición."""
    limpiar_pantalla()

    print(Fore.LIGHTBLACK_EX + "Cargando requisitos", end="", flush=True)
    for _ in range(3):
        time.sleep(0.2)
        print(".", end="", flush=True)
    time.sleep(0.3)

    limpiar_pantalla()
    mostrar_seccion("REQUISITOS DE INSCRIPCIÓN")

    print(Fore.YELLOW + "📋 Documentación requerida para todas las carreras:\n" + Style.RESET_ALL)

    for i, req in enumerate(REQUISITOS, start=1):
        print(Fore.GREEN + f"✔️  {i}. {Fore.WHITE}{req}")

    print("\n" + Fore.LIGHTBLACK_EX + "ℹ️  Asegurate de tener todos los documentos en original y copia." + Style.RESET_ALL)
    
    input(Fore.LIGHTWHITE_EX + "\nPresione Enter para volver al menú...")

