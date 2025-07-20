"""
secciones.py

Agrupa todas las funciones asociadas a las distintas secciones informativas del menú,
como carreras, modalidades, requisitos, contacto, redes sociales y especialización.
"""


from utils import limpiar_pantalla, mostrar_seccion
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
    print(Fore.CYAN + "📝 Descripción: " +Fore.WHITE + f"{carrera['descripcion']}")
    print(Fore.CYAN + "⏳ Duración: " +Fore.WHITE + f"{carrera['duracion']}")
    print(Fore.CYAN + "📅 Período de inscripción: " +Fore.WHITE + f"{carrera['inscripcion']}")
    print(Fore.CYAN + "🏫 Modalidad: " +Fore.WHITE + f"{carrera['modalidad']}")
    print(Fore.CYAN + "📋 Requisitos: " +Fore.WHITE + f"{carrera['requisitos']}")
    print("\n📚 Plan de estudios:" + Style.RESET_ALL)

    for materia in carrera['plan_estudio']:
        print(Fore.GREEN + f" - {materia}" + Style.RESET_ALL)


def carrera():
    """Permite navegar entre las carreras y visualizar más información de cada una."""

    while True:
        limpiar_pantalla()
        mostrar_seccion("OFERTA ACADÉMICA 2025")
        mostrar_lista_carreras()
        print("\nPresione Enter para volver al menú principal")

        carrera = seleccionar_carrera()
        if carrera is None:
            return
        elif carrera == "reintentar":
            continue
        else:
            mostrar_detalle_carrera(carrera)
            input(Fore.WHITE + "\nPresione Enter para continuar...")


def modalidad():
    """Muestra información general de duración, modalidad e inscripción de todas las carreras."""

    limpiar_pantalla()
    mostrar_seccion("DURACIÓN Y MODALIDAD")
    print(Fore.CYAN + "Todas nuestras carreras:\n" + Style.RESET_ALL)
    for carrera in CARRERAS_INFO:
        print(f"{Fore.YELLOW}{carrera['nombre']}")
        print(f"{Fore.CYAN}Duración: {Fore.WHITE}{carrera['duracion']}")
        print(f"{Fore.CYAN}Modalidad: {Fore.WHITE}{carrera['modalidad']}")
        print(f"{Fore.CYAN}Inscripción: {Fore.WHITE}{carrera['inscripcion']}\n")
    print(Fore.LIGHTBLACK_EX + "* Pendiente de aprobación definitiva para ciclo lectivo 2025")
    input(Fore.WHITE + "\nPresione Enter para continuar...")


def contacto():
    """Muestra la información de contacto del instituto."""

    limpiar_pantalla()
    mostrar_seccion("CONTACTO INSTITUCIONAL")
    print(f"{Fore.CYAN}📍 Dirección: {Fore.WHITE}{CONTACTO['direccion']}")
    print(f"{Fore.CYAN}📞 Teléfono:  {Fore.WHITE}{CONTACTO['telefono']}")
    print(f"{Fore.CYAN}✉️  Email:    {Fore.WHITE}{CONTACTO['email']}")
    print(f"{Fore.CYAN}🌐 Sitio web:{Fore.WHITE} {CONTACTO['web']}")
    input(Fore.WHITE + "\nPresione Enter para continuar...")


def requisitos():
    """Muestra los requisitos de inscripción para las carreras."""
    limpiar_pantalla()
    mostrar_seccion("REQUISITOS DE INSCRIPCIÓN")
    print(Fore.CYAN + "Documentación requerida para todas las carreras:\n" + Style.RESET_ALL)
    for i, req in enumerate(REQUISITOS, start=1):
        print(f"{Fore.YELLOW}{i}. {Fore.WHITE}{req}")
    input(Fore.WHITE + "\nPresione Enter para continuar...")


def redes():
    """Muestra las redes sociales y página web del instituto."""
    limpiar_pantalla()
    mostrar_seccion("REDES SOCIALES")
    print(f"{Fore.CYAN}👍 Facebook:  {Fore.WHITE}{CONTACTO['redes']['facebook']}")
    print(f"{Fore.CYAN}📸 Instagram: {Fore.WHITE}{CONTACTO['redes']['instagram']}")
    print(f"{Fore.CYAN}🌐 Página:    {Fore.WHITE}{CONTACTO['web']}")
    input(Fore.WHITE + "\nPresione Enter para continuar...")


def especializacion():
    """Muestra información general de duración, modalidad e inscripción de todas las carreras."""

    limpiar_pantalla()
    mostrar_detalle_carrera(CARRERAS_INFO[-1])
    input(Fore.WHITE + "\nPresione Enter para continuar...")

