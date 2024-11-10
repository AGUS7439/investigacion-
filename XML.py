import xml.etree.ElementTree as ET

# Cargar y parsear el archivo XML
tree = ET.parse('gus.xml')
root = tree.getroot()


for elem in root.iter('nombre'):
    elem.text = 'Nuevo valor'


tree.write('gus.xml')
