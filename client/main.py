import subprocess
import json
import requests
import os

r = requests.get("http://www.mclibre.org/python/testing/python.py")
valores = json.loads(r.text)

informeErrores = []

for i in valores["tests"]:
    with open("valores-prueba.txt", "w") as fichero:
        fichero.write(str(i))

    p = subprocess.Popen(['pytest', 'test_programa.py', '--junitxml=resultado.txt'])
    p.wait()

    import xml.etree.ElementTree as ET
    tree = ET.parse('resultado.txt')
    root = tree.getroot()
    for neighbor in root.iter('testsuite'):
        if int(neighbor.attrib["failures"]) > 0:
            with open("resultado-obtenido.txt", "r") as fichero:
                # Como está guardado en json, lo lee como lista
                texto = json.load(fichero)
            informeErrores += [[i["input"], i["output"], texto]]
            if os.path.isfile("resultado-obtenido.txt"):
                os.remove("resultado-obtenido.txt")

    if os.path.isfile("valores-prueba.txt"):
        os.remove("valores-prueba.txt")

    if os.path.isfile("resultado.txt"):
        os.remove("resultado.txt")

if informeErrores == []:
    print("No se han encontrado fallos en el programa")
else:
    for i in informeErrores:
        print("El programa no funciona correctamente en el siguiente caso:")
        print("  Valores de prueba:", i[0])
        if len(i[1]) != len(i[2]):
            print("  El programa no genera la misma cantidad de salidas")
        for j in range(min(len(i[1]), len(i[2]))):
            if i[1][j] != i[2][j]:
                print(f"  Resultado esperado: \"{i[1][j]}\"")
                print(f"  Resultado obtenido: \"{i[2][j]}\"")
        for j in range(min(len(i[1]), len(i[2])), max(len(i[1]), len(i[2]))):
            if 0 <= j < len(i[1]):
                print(f"  Resultado esperado: \"{i[1][j]}\"")
            else:
                print(f"  No se esperaba ningún resultado")
            if 0 <= j < len(i[2]):
                print(f"  Resultado obtenido: \"{i[2][j]}\"")
            else:
                print(f"  No se ha obtenido ningún resultado")
