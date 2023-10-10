import yaml
import xml.etree.ElementTree as ET
import json

def crear_datos():
    # Lista de nombres de docentes
    nombres = ["Juan Pérez", "María García", "Pedro López", "Ana Rodríguez"]

    # Lista de objetos de datos
    datos = []
    for nombre in nombres:
        datos.append({
            "nombre": nombre
        })

    return datos

def serializar_yaml(datos):
    # Serializa los datos en YAML
    yaml_data = yaml.safe_dump(datos)

    # Imprime los datos serializados en YAML
    print("Datos YAML:")
    print(yaml_data)

def serializar_xml(datos):
    # Crea el elemento raíz del documento XML
    root = ET.Element("docentes")

    # Agrega los elementos de datos al documento XML
    for dato in datos:
        docente = ET.SubElement(root, "docente")
        docente.set("nombre", dato["nombre"])

    # Serializa el documento XML
    xml_data = ET.tostring(root,)

    # Imprime los datos serializados en XML
    print("Datos XML:")
    print(xml_data)

def serializar_json(datos):
    # Serializa los datos en JSON
    json_data = json.dumps(datos)

    # Imprime los datos serializados en JSON
    print("Datos JSON:")
    print(json_data)

if __name__ == "__main__":
    # Crea los datos
    datos = crear_datos()

    # Serializa los datos en YAML, XML y JSON
    serializar_yaml(datos)
    serializar_xml(datos)
    "\n"
    serializar_json(datos)
