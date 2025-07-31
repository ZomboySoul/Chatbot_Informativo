"""
main.py

Archivo principal del sistema. Controla el flujo general del chatbot,
mostrando el menú principal e invocando las funciones correspondientes
a cada sección del sistema informativo del Instituto Superior N°57.
"""


from interfaz import mostrar_bienvenida, mostrar_menu, despedida
from secciones import carrera, contacto, requisitos
from utils import limpiar_pantalla
from colorama import Fore, Style


def iniciar_chatbot():
    """Controla el flujo general del programa, desde la bienvenida hasta la despedida."""
    
    menu_opciones = {
       "1": carrera,
       "2": contacto,
       "3": requisitos,
       "4": lambda: despedida(nombre_completo)
    }

    nombre_completo = mostrar_bienvenida()
    
    while True:
        limpiar_pantalla()
        
        opcion = mostrar_menu()

        accion = menu_opciones.get(opcion)

        if accion:
            accion()
            if opcion == "4":
                return  # sale del programa
        else:
            print(Fore.RED + "\n⚠️ Opción no válida. Por favor ingrese un número del 1 al 7." + Style.RESET_ALL)
            input("Presione Enter para continuar...")


if __name__ == "__main__":
    iniciar_chatbot()
