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

