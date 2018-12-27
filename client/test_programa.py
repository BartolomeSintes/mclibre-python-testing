# basado en https://code-maven.com/mocking-input-and-output-for-python-testing

import programa
import requests
import pytest
import json

with open("valores-prueba.txt", "r") as fichero:
    texto = fichero.read()
    texto = texto.replace("'", '"')
    valores = json.loads(texto)

def test_programa():
    global valores
    
    input_values = valores["input"]
    output = []

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)

    programa.input = mock_input
    programa.print = lambda s : output.append(s)

    programa.main()

    with open("resultado-obtenido.txt", "w") as fichero:
        # Lo guardo en json porque es una lista y para leerlo no da problemas
        json.dump(output, fichero)

    assert output == valores["output"]

