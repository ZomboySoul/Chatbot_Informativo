"""
chatbot_consola.py

Chatbot informativo para el Instituto Superior N°57 "Juana P. Manso".
Permite a los usuarios consultar la oferta académica, requisitos, contacto,
modalidad de cursada, redes sociales y más.

Estructura basada en un menú interactivo por consola, con validaciones básicas
y funciones separadas para cada sección.
"""
import re
import os
from colorama import init, Fore, Style
from datos import CARRERAS_INFO, CONTACTO, REQUISITOS
init(autoreset=True)


# ========================================================
# 🔧 FUNCIONES DE UTILIDAD GENERAL
# ========================================================


def limpiar_pantalla():
    """Limpia la consola dependiendo del sistema operativo."""

    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_seccion(titulo):
    """Muestra un título centrado y decorado en pantalla para identificar secciones."""
    
    print()
    print(Fore.YELLOW + f"{titulo.upper():^60}")
    print()


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


def validar_nombre(nombre):
    """Valida que el nombre ingresado tenga al menos dos palabras y solo contenga letras, espacios y tildes."""
   
    patron_nombre = re.compile(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")
    return len(nombre.split()) >= 2 and patron_nombre.match(nombre)


# ========================================================
# 🧑‍🎓 FUNCIONES RELACIONADAS A LA OFERTA ACADÉMICA
# ========================================================


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


def especializacion():
    """Muestra información general de duración, modalidad e inscripción de todas las carreras."""

    limpiar_pantalla()
    mostrar_detalle_carrera(CARRERAS_INFO[-1])
    input(Fore.WHITE + "\nPresione Enter para continuar...")


# ========================================================
# 📄 FUNCIONES DE INFORMACIÓN GENERAL DEL INSTITUTO
# ========================================================


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


# ========================================================
# 🤖 FUNCIONES DE INTERACCIÓN CON EL USUARIO
# ========================================================


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
    print(Fore.RED +  " Instituto 57 'Juana P. Manso'\n ".center(60))


# ========================================================
# 🚀 FUNCIÓN PRINCIPAL
# ========================================================


def iniciar_chatbot():
    """Controla el flujo general del programa, desde la bienvenida hasta la despedida."""
    
    menu_opciones = {
       "1": carrera,
       "2": modalidad,
       "3": contacto,
       "4": requisitos,
       "5": redes,
       "6": especializacion,
       "7": lambda: despedida(nombre_completo)
    }

    nombre_completo = mostrar_bienvenida()
    
    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input(Fore.LIGHTMAGENTA_EX + "\nIngrese una opción (1-7): " + Fore.RESET).strip()

        accion = menu_opciones.get(opcion)

        if accion:
            accion()
            if opcion == "7":
                return  # sale del programa
        else:
            print(Fore.RED + "\n⚠️ Opción no válida. Por favor ingrese un número del 1 al 7." + Style.RESET_ALL)
            input("Presione Enter para continuar...")


# ========================================================
# ▶️ EJECUCIÓN DEL PROGRAMA
# ========================================================


if __name__ == "__main__":
    iniciar_chatbot()
