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
    crear_docente("Alessandra Sanchez", 20045147, "Alumno"),
]

# Serializamos los datos en YAML
yaml_data = yaml.dump(docentes, default_flow_style=False)

# Serializamos los datos en JSON
json_data = json.dumps(docentes)

# Serializamos los datos en XML
xml_data = ET.tostring(
    ET.Element("docentes", attrib={"total": str((docentes))}),
    encoding="utf-8"
)

# Imprimimos los datos serializados
print("YAML:")
print(yaml_data)

print("JSON:")
print(json_data)
print("\n")

print("XML:")
print(xml_data)
