# basado en https://code-maven.com/mocking-input-and-output-for-python-testing

import program
import requests
import pytest
import json

with open("test-values.txt", "r") as file:
    texto = file.read()
    texto = texto.replace("'", '"')
    values = json.loads(texto)

def test_program():
    global values

    input_values = values["input"]
    output = []

    def mock_input(s):
        output.append(s)
        return input_values.pop(0)

    program.input = mock_input
    program.print = lambda s : output.append(s)

    program.main()

    with open("obtained-result.txt", "w") as file:
        # saved as json because it is a list
        json.dump(output, file)

    assert output == values["output"]

