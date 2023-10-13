import yaml
import json
import xml.etree.ElementTree as ET

# Definimos una función para crear un objeto docente
def crear_docente(nombre, numero_empleado, especialidad):
    return {
        "nombre": nombre,
        "numero_empleado": numero_empleado,
        "especialidad": especialidad
    }

# Creamos una lista de docentes
docentes = [
    crear_docente("Roberto Perez", 10023, "Haking etico"),
    crear_docente("Maria Azucena", 10024, "Direccion de proyectos 2"),
    crear_docente("Patricia Guadalupe", 10025, "Inteligencia de negocios"),
    crear_docente("Gabriel Alejandro", 10026, "Automatizacion de infraestructura digital"),
    crear_docente("Alan Dias", 10027, "sistemas de calidad"),
    crear_docente("Geltrudis pilar", 10028, "Ingles"),
    crear_docente("Roberto Perez", 10029, "Tutorias"),
    crear_docente("Adriana", 10030, "Equipos de alto rendimiento"),
    crear_docente("Zaul Hernandez", 19040067, "Alumno"),
]

