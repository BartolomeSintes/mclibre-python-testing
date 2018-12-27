import subprocess
import json
import requests
import os

r = requests.get("http://www.mclibre.org/python/testing/python.py")
values = json.loads(r.text)

errorReport = []

for i in values["tests"]:
    with open("test-values.txt", "w") as file:
        file.write(str(i))

    p = subprocess.Popen(['pytest', 'test-program.py', '--junitxml=result.txt'])
    p.wait()

    import xml.etree.ElementTree as ET
    tree = ET.parse('result.txt')
    root = tree.getroot()
    for neighbor in root.iter('testsuite'):
        if int(neighbor.attrib["failures"]) > 0:
            with open("obtained-result.txt", "r") as file:
                # file is saved as json and is read as a list
                texto = json.load(file)
            errorReport += [[i["input"], i["output"], texto]]
            if os.path.isfile("obtained-result.txt"):
                os.remove("obtained-result.txt")

    if os.path.isfile("test-values.txt"):
        os.remove("test-values.txt")

    if os.path.isfile("result.txt"):
        os.remove("result.txt")

if errorReport == []:
    print("No se han encontrado fallos en el programa")
else:
    for i in errorReport:
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
