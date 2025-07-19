# # nuevo_ultima_version.py

import tkinter as tk
from tkinter import font
import threading

# ==============================================================================
# DATOS DEL INSTITUTO: Organizamos la información en estructuras clave.
# Tomados directamente de chatbot_consola.py
# ==============================================================================

# CARRERAS_INFO: Una lista de diccionarios. Cada diccionario representa una carrera
# y contiene todos sus detalles relevantes. Esta estructura permite almacenar
# información compleja y bien organizada para cada oferta académica.
CARRERAS_INFO = [
    {
        "nombre": "Profesorado de Educación Inicial",  # Clave 'nombre' para el nombre de la carrera.
        "duracion": "4 años",  # Clave 'duracion' para el tiempo de estudio.
        "descripcion": "Formación para educadores de nivel inicial.",  # Descripción breve de la carrera.
        "requisitos": "Título de Escuela Secundaria",  # Requisito de ingreso.
        "plan_estudio": [  # 'plan_estudio' es una lista de strings para describir el plan año por año.
            "1er año: Introducción a la educación, psicología infantil, didáctica general",
            "2do año: Desarrollo cognitivo, juego y aprendizaje, prácticas docentes I",
            "3er año: Diseño curricular, evaluación educativa, prácticas docentes II",
            "4to año: Gestión institucional, proyectos educativos, residencia docente"
        ],
        "inscripcion": "Marzo-Abril / Agosto-Septiembre",  # Períodos de inscripción.
        "modalidad": "Presencial"  # Modalidad de cursada (Presencial, Semipresencial, Virtual).
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

# CONTACTO: Un diccionario para almacenar toda la información de contacto del instituto.
# Usa un diccionario anidado para 'redes' para organizar aún más esa información específica.
CONTACTO = {
    "direccion": "Franklin Nº 166 e/ Alvear y Libres del Sur, Chascomús",  # Dirección física.
    "telefono": "(2241) 436710",  # Número telefónico.
    "email": "isfdyt57chascomus@abc.gob.ar",  # Correo electrónico oficial.
    "web": "https://isfdyt57chascomus.edu.ar/",  # Sitio web oficial.
    "redes": {  # Diccionario anidado para las redes sociales.
        "facebook": "@Instituto57chascomus",
        "instagram": "@Instituto57chascomus"
    }
}

# REQUISITOS: Una lista simple de strings, donde cada string es un requisito de inscripción.
REQUISITOS = [
    "DNI (original y fotocopia de anverso y reverso)",
    "CUIL (original y fotocopia)",
    "Partida de nacimiento (original y copia)",
    "Certificado de aptitud física (vigente)",
    "Título secundario (original y copia legalizada)",
    "4 fotos 4x4 color (fondo blanco)"
]

def rounded_rect(canvas, x1, y1, x2, y2, radius=15, **kwargs):
    """Crea un rectángulo con bordes redondeados para las burbujas de chat"""
    points = [
        x1+radius, y1,
        x2-radius, y1,
        x2, y1,
        x2, y1+radius,
        x2, y2-radius,
        x2, y2,
        x2-radius, y2,
        x1+radius, y2,
        x1, y2,
        x1, y2-radius,
        x1, y1+radius,
        x1, y1
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot - Instituto 57 Juana Manso")
        self.root.geometry("650x720")
        self.root.resizable(True, True) # Permitir redimensionar la ventana
        self.root.configure(bg="#1e1e1e")
        
        # Fuentes
        self.font_title = font.Font(family="Segoe UI", size=22, weight="bold")
        self.font_chat = font.Font(family="Segoe UI", size=12)
        self.font_bold = font.Font(family="Segoe UI", size=13, weight="bold")
        self.font_small = font.Font(family="Segoe UI", size=10)
        
        # Cabecera centrada
        header_frame = tk.Frame(root, bg="#1e1e1e")
        header_frame.pack(fill=tk.X, pady=10)
        
        center_frame = tk.Frame(header_frame, bg="#1e1e1e")
        center_frame.pack(expand=True)
        
        tk.Label(center_frame, text="🤖", font=("Segoe UI Emoji", 48), 
                bg="#1e1e1e", fg="white").pack(side=tk.LEFT)
        tk.Label(center_frame, text="Instituto 57 Juana Manso", 
                font=self.font_title, bg="#1e1e1e", fg="white").pack(side=tk.LEFT, padx=10)
        
        # Área de chat con scroll
        chat_frame = tk.Frame(root, bg="#2b2b2b")
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0,10))
        
        self.canvas = tk.Canvas(chat_frame, bg="#2b2b2b", highlightthickness=0)
        self.scrollbar = tk.Scrollbar(chat_frame, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.message_frame = tk.Frame(self.canvas, bg="#2b2b2b")
        # Guarda el ID de la ventana dentro del canvas para poder modificarla
        self.message_frame_id = self.canvas.create_window((0, 0), window=self.message_frame, anchor="nw")
        
        # Vincular el ajuste del scrollbar al tamaño del message_frame
        self.message_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        # Vincular el ajuste del ancho del window para que las burbujas se reajusten
        self.canvas.bind("<Configure>", self._on_canvas_configure)


        # Entrada de usuario
        bottom_frame = tk.Frame(root, bg="#1e1e1e")
        bottom_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.entry = tk.Entry(bottom_frame, font=self.font_chat, bg="#3c3c3c", fg="white", 
                            insertbackground="white", relief=tk.FLAT)
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5)
        self.entry.bind("<Return>", self.procesar)
        
        send_btn = tk.Button(bottom_frame, text="Enviar", font=self.font_chat, 
                            bg="#0f62fe", fg="white", activebackground="#0050d1",
                            activeforeground="white", relief=tk.FLAT, command=self.procesar)
        send_btn.pack(side=tk.LEFT, padx=10)
        
        # Estado inicial
        self.estado = "inicio"
        self.nombre_usuario = ""
        
        # Mensaje de bienvenida
        self.bot("👋 ¡Hola! Bienvenido/a al Instituto de Formación Docente N°57.")
        self.bot("📝 Por favor, ingresá tu nombre y apellido para comenzar.")
    
    def _on_canvas_configure(self, event):
        """Ajusta el ancho del message_frame y redibuja las burbujas."""
        # Asegura que el frame que contiene las burbujas tenga el mismo ancho que el canvas
        self.canvas.itemconfigure(self.message_frame_id, width=event.width)
        
        # Forzar una actualización completa del message_frame para asegurar que tenga su nuevo ancho
        self.message_frame.update_idletasks()
        
        # Iterar a través de todos los contenedores de burbujas (hijos de message_frame)
        for bubble_container in self.message_frame.winfo_children():
            # Cada contenedor debería tener un Canvas como su hijo
            for bubble_canvas in bubble_container.winfo_children():
                if isinstance(bubble_canvas, tk.Canvas):
                    # Asegurarse de que es uno de nuestros canvases de burbujas
                    if hasattr(bubble_canvas, 'text_item_id') and hasattr(bubble_canvas, 'rounded_rect_id'):
                        
                        bubble_canvas_actual_width = bubble_canvas.winfo_width()
                        if bubble_canvas_actual_width < 100:
                            bubble_canvas_actual_width = 100
                        
                        padding_x = 15
                        padding_y = 10
                        radius = 15 # Definir radius aquí también, ya que se usa al redibujar
                        
                        text_wrap_width = bubble_canvas_actual_width - (2 * padding_x) - 10
                        if text_wrap_width < 10:
                            text_wrap_width = 10
                        
                        bubble_canvas.itemconfigure(bubble_canvas.text_item_id, width=text_wrap_width)
                        
                        bubble_canvas.update_idletasks() # Crucial para refrescar el bbox
                        x1, y1, x2, y2 = bubble_canvas.bbox(bubble_canvas.text_item_id)
                        
                        actual_text_width = x2 - x1
                        actual_text_height = y2 - y1
                        
                        new_canvas_width = actual_text_width + (2 * padding_x)
                        new_canvas_height = actual_text_height + (2 * padding_y)

                        if new_canvas_width < bubble_canvas_actual_width:
                            new_canvas_width = bubble_canvas_actual_width
                        
                        bubble_canvas.config(width=new_canvas_width, height=new_canvas_height)

                        if bubble_canvas.is_user_bubble: 
                            bubble_canvas.coords(bubble_canvas.text_item_id, new_canvas_width - padding_x, padding_y)
                        else:
                            bubble_canvas.coords(bubble_canvas.text_item_id, padding_x, padding_y)

                        # Borrar el rectángulo antiguo y dibujar uno nuevo con las dimensiones correctas
                        bubble_canvas.delete(bubble_canvas.rounded_rect_id)
                        color = "#0f62fe" if bubble_canvas.is_user_bubble else "#3c3c3c" # Re-definir color
                        bubble_canvas.rounded_rect_id = rounded_rect(bubble_canvas, 2, 2, new_canvas_width-2, new_canvas_height-2, 
                                                                     radius=radius, fill=color, outline=color)
                        
                        bubble_canvas.tag_raise(bubble_canvas.text_item_id)

        # Actualizar la región de scroll del canvas principal
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def bot(self, text, bold=False):
        """Muestra un mensaje del bot"""
        self._add_bubble(text, is_user=False, bold=bold)

    def user(self, text):
        """Muestra un mensaje del usuario"""
        self._add_bubble(text, is_user=True)

    def _add_bubble(self, text, is_user, bold=False):
        """Crea una burbuja de chat con estilo WhatsApp"""
        container = tk.Frame(self.message_frame, bg="#2b2b2b")
        container.pack(fill=tk.X, expand=True, anchor="e" if is_user else "w", padx=10, pady=4)
        
        canvas = tk.Canvas(container, bg="#2b2b2b", highlightthickness=0)
        canvas.pack(fill=tk.X, expand=True) 

        # Almacenar si es una burbuja de usuario para su uso posterior en el redimensionamiento
        canvas.is_user_bubble = is_user

        # CRÍTICO: Forzar la actualización del canvas de la burbuja para que obtenga su ancho real
        canvas.update_idletasks() 
        bubble_canvas_actual_width = canvas.winfo_width()
        
        # Asegurar un ancho mínimo
        if bubble_canvas_actual_width < 100:
            bubble_canvas_actual_width = 100

        padding_x = 15
        padding_y = 10
        radius = 15
        color = "#0f62fe" if is_user else "#3c3c3c"
        text_color = "white"
        
        # Definir el anclaje y la justificación del texto
        text_anchor = "ne" if is_user else "nw"
        text_justify = "right" if is_user else "left"
        
        # Calcular el ancho para el ajuste de línea del texto
        text_wrap_width = bubble_canvas_actual_width - (2 * padding_x) - 10 
        if text_wrap_width < 10:
            text_wrap_width = 10

        # Definir la coordenada X inicial del texto
        if is_user:
            text_x_coord = bubble_canvas_actual_width - padding_x 
        else:
            text_x_coord = padding_x 

        # Crear el item de texto (importante crearlo primero para obtener sus dimensiones)
        text_item_id = canvas.create_text(text_x_coord, padding_y, anchor=text_anchor, text=text, 
                                          font=self.font_bold if bold else self.font_chat, 
                                          fill=text_color, 
                                          width=text_wrap_width, 
                                          justify=text_justify)
        # Almacenar el ID del item de texto en el canvas
        canvas.text_item_id = text_item_id

        # Forzar actualización para obtener la caja delimitadora real del texto
        canvas.update_idletasks() 
        x1, y1, x2, y2 = canvas.bbox(text_item_id)
        
        # Calcular el ancho y alto necesarios para el canvas de la burbuja
        actual_text_width = x2 - x1
        actual_text_height = y2 - y1
        
        canvas_width = actual_text_width + (2 * padding_x)
        canvas_height = actual_text_height + (2 * padding_y)

        # Asegurarse de que el canvas de la burbuja sea al menos tan ancho como su espacio asignado
        if canvas_width < bubble_canvas_actual_width:
             canvas_width = bubble_canvas_actual_width

        # Re-configurar el tamaño del canvas de la burbuja
        canvas.config(width=canvas_width, height=canvas_height)
        
        # Dibujar el rectángulo redondeado de la burbuja *después* del texto y asegurar que esté detrás
        # Borrar el rectángulo antiguo si existe para evitar superposiciones
        if hasattr(canvas, 'rounded_rect_id') and canvas.rounded_rect_id:
            canvas.delete(canvas.rounded_rect_id)

        rounded_rect_id = rounded_rect(canvas, 2, 2, canvas_width-2, canvas_height-2, 
                    radius=radius, fill=color, outline=color)
        # Almacenar el ID del rectángulo redondeado en el canvas
        canvas.rounded_rect_id = rounded_rect_id
        
        # Traer el texto al frente (esencial para la visibilidad)
        canvas.tag_raise(text_item_id) 

        # Auto-scroll al final del chat
        self.canvas.update_idletasks()
        self.canvas.yview_moveto(1.0)


    def mostrar_menu_principal(self):
        """Muestra el menú principal con todas las opciones, replicando chatbot_consola.py"""
        menu_text = """
📚 Menú Principal:
1. Carreras disponibles 2025
2. Información sobre duración y modalidad
3. Contacto y ubicación
4. Requisitos de inscripción
5. Redes sociales
6. Especialización en Enfermería en Salud Mental
7. Salir
"""
        self.bot(menu_text)

    def mostrar_carreras(self):
        """Muestra la lista de carreras disponibles para elegir detalles"""
        texto = "🎓 Carreras Disponibles 2025:\n"
        for i, c in enumerate(CARRERAS_INFO):
            texto += f"{i+1}. {c['nombre']} ({c['duracion']})\n"
        texto += "\n📌 Escribí el número de la carrera para más detalles o 'menu' para volver."
        self.bot(texto)
        self.estado = "carrera"

    def mostrar_duracion_modalidad(self):
        """Muestra la duración y modalidad de todas las carreras"""
        self.bot("⏳ Duración y Modalidad de Carreras:")
        for c in CARRERAS_INFO:
            self.bot(f"🔹 {c['nombre']}\n   Duración: {c['duracion']}\n   Modalidad: {c['modalidad']}\n   Inscripción: {c['inscripcion']}\n")
        self.bot("* Pendiente de aprobación definitiva para ciclo lectivo 2025")
        self.mostrar_menu_principal()
        self.estado = "menu"

    def mostrar_contacto_ubicacion(self):
        """Muestra la información de contacto y ubicación del instituto"""
        self.bot("📞 Contacto Institucional:", bold=True)
        self.bot(f"📍 Dirección: {CONTACTO['direccion']}")
        self.bot(f"📞 Teléfono: {CONTACTO['telefono']}")
        self.bot(f"✉️ Email: {CONTACTO['email']}")
        self.bot(f"🌐 Sitio web: {CONTACTO['web']}")
        self.mostrar_menu_principal()
        self.estado = "menu"

    def mostrar_requisitos_inscripcion(self):
        """Muestra los requisitos de inscripción"""
        self.bot("📋 Requisitos de Inscripción:", bold=True)
        self.bot("Documentación requerida para todas las carreras:")
        for i, req in enumerate(REQUISITOS):
            self.bot(f"{i+1}. {req}")
        self.mostrar_menu_principal()
        self.estado = "menu"

    def mostrar_redes_sociales(self):
        """Muestra las redes sociales del instituto"""
        self.bot("📱 Redes Sociales:", bold=True)
        self.bot(f"👍 Facebook: {CONTACTO['redes']['facebook']}")
        self.bot(f"📸 Instagram: {CONTACTO['redes']['instagram']}")
        self.bot(f"🌐 Página oficial: {CONTACTO['web']}")
        self.mostrar_menu_principal()
        self.estado = "menu"

    def mostrar_especializacion_salud_mental(self):
        """Muestra los detalles de la Especialización en Enfermería en Salud Mental"""
        salud_mental_carrera = next((c for c in CARRERAS_INFO if "Salud Mental" in c["nombre"]), None)
        if salud_mental_carrera:
            self.mostrar_detalle_carrera_generico(salud_mental_carrera)
        self.mostrar_menu_principal()
        self.estado = "menu"

    def mostrar_detalle_carrera_generico(self, carrera):
        """Muestra los detalles completos de una carrera dada."""
        self.bot(carrera['nombre'], bold=True)
        self.bot(f"📝 Descripción: {carrera['descripcion']}")
        self.bot(f"⏳ Duración: {carrera['duracion']}")
        self.bot(f"📅 Período de inscripción: {carrera['inscripcion']}")
        self.bot(f"🏫 Modalidad: {carrera['modalidad']}")
        self.bot(f"📋 Requisitos: {carrera['requisitos']}")
        self.bot("\n📚 Plan de estudios:")
        for materia in carrera['plan_estudio']:
            self.bot(f" - {materia}")
        self.bot("🔁 Escribí 'menu' para volver al menú principal o 'carreras' para ver la lista otra vez.")
        self.estado = "detalle"

    def procesar(self, event=None):
        """Procesa la entrada del usuario"""
        entrada = self.entry.get().strip()
        if not entrada:
            return
        
        self.user(entrada)
        self.entry.delete(0, tk.END)
        
        # Estado inicial - Pedir nombre
        if self.estado == "inicio":
            self.nombre_usuario = entrada.title()
            self.bot(f"🤖 ¡Genial, ahora sí, {self.nombre_usuario}, podemos comenzar!")
            self.bot("Bienvenido/a al chatbot informativo del Instituto 57.")
            self.bot("Comencemos con el recorrido por nuestra oferta académica.")
            self.mostrar_menu_principal()
            self.estado = "menu"
        
        # Menú principal
        elif self.estado == "menu":
            if entrada == "1":
                self.mostrar_carreras()
            elif entrada == "2":
                self.mostrar_duracion_modalidad()
            elif entrada == "3":
                self.mostrar_contacto_ubicacion()
            elif entrada == "4":
                self.mostrar_requisitos_inscripcion()
            elif entrada == "5":
                self.mostrar_redes_sociales()
            elif entrada == "6":
                self.mostrar_especializacion_salud_mental()
            elif entrada == "7":
                self.bot(f"👋 {self.nombre_usuario.upper()}, GRACIAS POR UTILIZAR NUESTRO SISTEMA.")
                self.bot("Instituto 57 'Juana P. Manso'")
                self.entry.config(state="disabled")
            else:
                self.bot("❌ Opción inválida. Elegí del 1 al 7.")
        
        # Lista de carreras
        elif self.estado == "carrera":
            if entrada.lower() == "menu":
                self.mostrar_menu_principal()
                self.estado = "menu"
            else:
                try:
                    i = int(entrada) - 1
                    if 0 <= i < len(CARRERAS_INFO):
                        self.mostrar_detalle_carrera_generico(CARRERAS_INFO[i])
                    else:
                        self.bot("❌ Número inválido. Probá con otra opción.")
                except ValueError:
                    self.bot("❌ Por favor, ingresá un número válido.")
        
        # Detalle de carrera
        elif self.estado == "detalle":
            if entrada.lower() == "menu":
                self.mostrar_menu_principal()
                self.estado = "menu"
            elif entrada.lower() == "carreras":
                self.mostrar_carreras()
            else:
                self.bot("❓ Escribí 'menu' para volver o 'carreras' para la lista.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()