# Chatbot Informativo – Instituto Superior N.º 57 “Juana Paula Manso”

Este chatbot interactivo en consola, desarrollado en Python, permite a los usuarios acceder de manera ágil y amigable a toda la información relevante del Instituto Superior N.º 57 “Juana Paula Manso”.  
Entre sus funciones, brinda detalles sobre la oferta académica, requisitos de inscripción, modalidades de cursada, datos de contacto, redes sociales y más.

## 📝 Descripción

El chatbot ofrece una interfaz interactiva por consola que permite a los usuarios explorar de manera clara y ordenada la información institucional del Instituto Superior N.º 57.  
Su estructura basada en menús facilita la navegación y el acceso a cada sección, integrando validaciones básicas para una experiencia más robusta.

A través del sistema, los usuarios pueden consultar:

- La oferta académica disponible y los detalles de cada carrera.
- Modalidad de cursada, duración y períodos de inscripción.
- Datos de contacto institucional y ubicación.
- Requisitos necesarios para inscribirse.
- Redes sociales oficiales y sitio web.
- Información específica sobre la especialización en Enfermería en Salud Mental.

## ⚙️ Características principales

- Limpieza automática de pantalla, adaptada al sistema operativo (Windows/Linux).
- Validación de nombre y apellido con soporte para caracteres especiales (tildes, ñ, etc.).
- Interfaz visual mejorada mediante el uso de colores en consola con la librería `colorama`.
- Menús numerados e intuitivos que facilitan la navegación del usuario.
- Estructura modular con funciones separadas, lo que permite un mantenimiento sencillo y una ampliación escalable del sistema.

## 📦 Requisitos

Para ejecutar correctamente el chatbot, es necesario contar con lo siguiente:

- Python 3.6 o superior instalado.
- Paquete `colorama` para el uso de colores en consola.

Para instalar la dependencia externa, ejecutá:

```bash
pip install colorama
```

## ▶️ Uso

1. Cloná o descargá este repositorio en tu equipo.
2. Asegurate de tener Python instalado y el paquete `colorama` correctamente configurado.
3. Accedé a la carpeta del proyecto desde la terminal o consola.

### Ejecutar el chatbot

En la terminal, ejecutá el siguiente comando:

```bash
python chatbot_consola.py
```

## 🗂️ Estructura del proyecto

- **main.py**: Archivo principal que ejecuta el chatbot y coordina el flujo del programa.
- **interfaz.py**: Maneja la interacción con el usuario (bienvenida, menú, despedida, validación de nombre).
- **secciones.py**: Contiene las funciones relacionadas a las secciones informativas (carreras, requisitos, contacto, etc.).
- **utils.py**: Funciones de utilidad general como limpiar pantalla y mostrar títulos.
- **datos.py**: Archivo con los datos estáticos del instituto (carreras, contacto, requisitos).

## 🤝 Contribuciones

Las contribuciones al proyecto son bienvenidas.  
Si deseas proponer mejoras, corregir errores o agregar nuevas funcionalidades, podés hacerlo mediante un **issue** o abriendo un **pull request** en este repositorio.

Toda sugerencia será valorada para continuar mejorando la herramienta.

## 📄 Licencia

Este proyecto fue desarrollado con fines educativos y se encuentra disponible para su uso, distribución o adaptación **sin fines comerciales**.

---

## 👨‍💻 Desarrollado por el Grupo 8

**Integrantes:**

- Elías Campos
- Agustín Lezcano
- Alejandro Olivera
- Carlos Olivera
