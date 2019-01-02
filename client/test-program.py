# based en https://code-maven.com/mocking-input-and-output-for-python-testing

import requests
import pytest
import json
import importlib

# Name of the Python program that will be tested
program_file = "program"

program = importlib.import_module(program_file)

with open("test-values.txt", "r", encoding="utf-8") as file:
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

    with open("obtained-result.txt", "w", encoding="utf-8") as file:
        # saved as json because it is a list
        json.dump(output, file, ensure_ascii=False)

    assert output == values["output"]

