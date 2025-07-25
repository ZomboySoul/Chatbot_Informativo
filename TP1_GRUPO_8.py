"""
main.py

Archivo principal del sistema. Controla el flujo general del chatbot,
mostrando el menú principal e invocando las funciones correspondientes
a cada sección del sistema informativo del Instituto Superior N°57.
"""
import os
import re
from colorama import Fore, Style

# LISTAS GLOBALES 
CARRERAS_INFO = [
    {
        "nombre": "Profesorado de Educación Inicial",
        "duracion": "4 años",
        "descripcion": "Formación para educadores de nivel inicial.",
        "requisitos": "Título de Escuela Secundaria",
        "plan_estudio": [
            "1er año: Introducción a la educación, psicología infantil, didáctica general",
            "2do año: Desarrollo cognitivo, juego y aprendizaje, prácticas docentes I",
            "3er año: Diseño curricular, evaluación educativa, prácticas docentes II",
            "4to año: Gestión institucional, proyectos educativos, residencia docente"
        ],
        "inscripcion": "Marzo-Abril / Agosto-Septiembre",
        "modalidad": "Presencial"
    },
    {
        "nombre": "Profesorado de Inglés",
        "duracion": "4 años",
        "descripcion": "Formación para docentes de inglés con enfoque comunicativo.",
        "requisitos": "Título de Escuela Secundaria",
        "plan_estudio": [
            "1er año: Lengua Inglesa I, Fonética, Gramática Contrastiva",
            "2do año: Literatura Angloamericana, Didáctica Especial, Observación de Clases",
            "3er año: Lingüística Aplicada, Evaluación Educativa, Práctica Docente I",
            "4to año: Seminario de Investigación, Práctica Docente II, Residencia"
        ],
        "inscripcion": "Marzo-Abril / Agosto-Septiembre",
        "modalidad": "Presencial"
    },
    {
        "nombre": "Tecnicatura Superior en Enfermería",
        "duracion": "3 años",
        "descripcion": "Formación técnica en enfermería general.",
        "requisitos": "Título de Escuela Secundaria",
        "plan_estudio": [
            "1er año: Anatomía, Fisiología, Fundamentos de Enfermería",
            "2do año: Farmacología, Enfermería Médico-Quirúrgica, Prácticas Hospitalarias",
            "3er año: Salud Pública, Gestión en Enfermería, Práctica Profesional Supervisada"
        ],
        "inscripcion": "Febrero-Marzo / Julio-Agosto",
        "modalidad": "Presencial"
    },
    {
        "nombre": "Tecnicatura Superior en Ciencia de Datos e IA",
        "duracion": "3 años",
        "descripcion": "Formación en análisis de datos e inteligencia artificial aplicada.",
        "requisitos": "Título de Escuela Secundaria",
        "plan_estudio": [
            "1er año: Programación I, Matemática Discreta, Estadística",
            "2do año: Bases de Datos, Aprendizaje Automático, Visualización de Datos",
            "3er año: Big Data, Ética en IA, Proyecto Integrador"
        ],
        "inscripcion": "Marzo a Mayo",
        "modalidad": "Semipresencial"
    },
    {
        "nombre": "Especialización en Enfermería en Salud Mental",
        "duracion": "1 año",
        "descripcion": "Formación avanzada para enfermeros en salud mental.",
        "requisitos": "Título de Enfermería Profesional, Universitaria o Licenciatura",
        "plan_estudio": [
            "Módulo 1: Fundamentos de Salud Mental y Psiquiatría",
            "Módulo 2: Intervenciones en Crisis y Rehabilitación",
            "Módulo 3: Práctica Clínica Supervisada"
        ],
        "inscripcion": "Todo el año",
        "modalidad": "Virtual"
    }
]
CONTACTO = {
    "direccion": "Franklin Nº 166 e/ Alvear y Libres del Sur, Chascomús",
    "telefono": "(2241) 436710",
    "email": "isfdyt57chascomus@abc.gob.ar",
    "web": "https://isfdyt57chascomus.edu.ar/",
    "redes": {
        "facebook": "@Instituto57chascomus",
        "instagram": "@Instituto57chascomus"
    }
}
REQUISITOS = [
    "DNI (original y fotocopia de anverso y reverso)",
    "CUIL (original y fotocopia)",
    "Partida de nacimiento (original y copia)",
    "Certificado de aptitud física (vigente)",
    "Título secundario (original y copia legalizada)",
    "4 fotos 4x4 color (fondo blanco)"
]



#=========================================
# 🧩 1. Validación y Entrada de Usuario
#=========================================


def validar_nombre(nombre):
    """Valida que el nombre ingresado tenga al menos dos palabras y solo contenga letras, espacios y tildes."""
   
    patron_nombre = re.compile(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")
    return len(nombre.split()) >= 2 and patron_nombre.match(nombre) is not None


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
        nombre = input(Fore.WHITE + "👤 Ingrese su nombre: ").strip().title()
        apellido = input(Fore.WHITE + "👤 Ingrese su apellido: ").strip().title()

        nombreCompleto = nombre + " " + apellido

        if validar_nombre(nombreCompleto):
            break
        else:
            print(Fore.RED + "⚠️ Ingrese nombre y apellido válidos (solo letras y al menos dos palabras)." + Style.RESET_ALL)


    limpiar_pantalla()
    
    print("")
    print(Fore.GREEN + f"¡Bienvenido/a, {nombreCompleto}!".center(60))
    print(Fore.GREEN + "Gracias por utilizar nuestro chatbot informativo.".center(60))
    print(Fore.GREEN + "Vamos a recorrer juntos la oferta académica 2025.".center(60))
    
    input("\nPresione Enter para continuar...")

    return nombre


def despedida(nombre_completo):
    """Muestra un mensaje de agradecimiento personalizado al finalizar el sistema."""

    limpiar_pantalla()
    print("")
    print(Fore.RED + f" {nombre_completo.upper()}, GRACIAS POR UTILIZAR NUESTRO SISTEMA ".center(60))
    print(Fore.RED +  " Instituto 57 'Juana P. Manso'\n ".center(60) + Fore.RESET)


#=========================================
# 🗂 2. Control y Flujo del Chatbot
#=========================================


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


#=========================================
# 🎓 3. Secciones de Información Académica
#=========================================


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


#=========================================
# 📞 4. Secciones Institucionales
#=========================================


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
    input(Fore.WHITE + "\nPresione Enter para volver al Menu Principal...")


def redes():
    """Muestra las redes sociales y página web del instituto."""
    limpiar_pantalla()
    mostrar_seccion("REDES SOCIALES")
    print(f"{Fore.CYAN}👍 Facebook:  {Fore.WHITE}{CONTACTO['redes']['facebook']}")
    print(f"{Fore.CYAN}📸 Instagram: {Fore.WHITE}{CONTACTO['redes']['instagram']}")
    print(f"{Fore.CYAN}🌐 Página:    {Fore.WHITE}{CONTACTO['web']}")
    input(Fore.WHITE + "\nPresione Enter para continuar...")


#=========================================
# 🧼 5. Utilidades / Interfaz
#=========================================


def limpiar_pantalla():
    """Limpia la consola dependiendo del sistema operativo."""

    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_seccion(titulo):
    """Muestra un título centrado y decorado en pantalla para identificar secciones."""
    
    print()
    print(Fore.YELLOW + f"{titulo.upper():^60}")
    print()


if __name__ == "__main__":
    iniciar_chatbot()
