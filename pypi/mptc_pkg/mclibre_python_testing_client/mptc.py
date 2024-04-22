import argparse
import json
import os
import random
import subprocess
import sys
import colorama

# pytest is a required module
try:
    exec("import pytest")
except:
    print("[ERROR] Módulo no instalado: PyTest")
    print("Por favor, instale PyTest y ejecute mptc de nuevo.")
    exit()

# requests is a required module
try:
    import requests
except:
    print("[ERROR] Módulo no instalado: Requests")
    print("Por favor, instale Requests y ejecute mptc de nuevo.")
    exit()


def create_test_program(program_to_be_tested):
    with open("test_program.py", "w", encoding="utf-8") as file:
        file.write(
            f"""# based en https://code-maven.com/mocking-input-and-output-for-python-testing

import importlib
import json
import os
import pytest
import requests

TOO_MANY_INPUT_ARGS = "Too many arguments in input() call"

program_file = str("{program_to_be_tested}").replace(".py", "")

program = importlib.import_module(program_file)

with open("test_values.txt", "r", encoding="utf-8") as file:
    texto = file.read()
    texto = texto.replace("'", '"')
    values = json.loads(texto)

    def test_program():
        global values

        if "input" in values:
            input_values = values["input"]
        else:
            input_values = []

        if "random" in values:
            random_values = values["random"]
        else:
            random_values = []

        if "choice" in values:
            choice_values = values["choice"]
        else:
            choice_values = []

        if "time" in values:
            time_values = values["time"]
        else:
            time_values = []

        output = []
        partial_output = ""

        def mock_input(*args):
            if len(args) > 1:
                raise ValueError(TOO_MANY_INPUT_ARGS)
            elif len(args) == 1:
                output.append(args[0])
            return input_values.pop(0)

        def generate_output(*args, **kwargs):
            nonlocal partial_output
            # TODO what happens if \\n is included in end?

            # if there is an end keyowrd argument, output is stored
            # in a string instead of added to the output
            if "end" in args[1]:
                if len(args[0]) != 0:
                    partial_output += str(args[0][0])
                    for j in range(1, len(args[0])):
                        partial_output = partial_output + " " + str(args[0][j])
                partial_output += str(args[1]["end"])
            else:
                string = partial_output
                # if there are several arguments in print(), they are added to the ouput
                if len(args[0]) == 0:
                    string += ""
                else:
                    string += str(args[0][0])
                    for j in range(1, len(args[0])):
                        string += " " + str(args[0][j])
                partial_output = ""
                if string[-2:] == ": " or string[-2:] == "? :" or string[-2:] == "= ":
                    output.append(string)
                else:
                    output.append(string.rstrip())

        program.input = mock_input

        program.print = lambda *args, **kwargs: generate_output(args, kwargs)

        try:
            program.random.randrange = lambda *args : random_values.pop(0)
        except:
            pass

        try:
            program.randrange = lambda *args : random_values.pop(0)
        except:
            pass

        try:
            program.random.choice = lambda *args : choice_values.pop(0)
        except:
            pass

        try:
            program.choice = lambda *args : choice_values.pop(0)
        except:
            pass

        try:
            program.time = lambda *args : time_values.pop(0)
        except:
            pass

        try:
            program.time.time = lambda *args : time_values.pop(0)
        except:
            pass

        program.main()

        if partial_output != "":
            output.append(partial_output.rstrip())

        with open("obtained_result.txt", "w", encoding="utf-8") as file:
            # saved as json because it is a list
            json.dump(output, file, ensure_ascii=False)

        assert output == values["output"]
"""
        )


def main():
    EXECUTION_ERROR = "Execution error"
    SYNTAX_ERROR = "Syntax error"

    parser = argparse.ArgumentParser(
        description="Herramienta de prueba para los ejercicios de programación del curso de Python de mclibre.org, disponible en https://www.mclibre.org/consultar/python/"
    )

    parser.add_argument(
        "to_be_tested_py",
        action="store",
        help="Nombre del archivo del programa de Python que va a ser probado",
    )

    parser.add_argument(
        "exercise_id",
        action="store",
        type=int,
        help="Identificador del conjunto de pruebas que se aplicarán al programa",
    )

    parser.add_argument(
        "-w",
        "--write",
        action="store",
        help="descarga y guarda los valores de test en un archivo",
    )

    parser.add_argument(
        "-r", "--read", action="store", help="lee valores de test de un archivo"
    )

    args = parser.parse_args()
    testable = args.to_be_tested_py
    if testable[0:2] == ".\\" or testable[0:2] == "./":
        testable = testable[2:]
    if testable.find("\\") != -1 or testable.find("/") != -1:
        print(f"Error: No se permiten caminos absolutos o relativos [{testable}].")
        print(
            "Por favor, ejecute MPTC en el directorio en el que se encuentra su programa."
        )
        exit()
    elif not (os.path.isfile(testable)):
        print(
            f"Error: No se encuentra el programa [{testable}]. Por favor, compruebe el nombre del fichero e inténtelo de nuevo."
        )
        exit()

    if args.read is not None:
        try:
            with open(args.read, "r", encoding="utf-8") as file:
                values = json.load(file)
                random_id = values["id"]
        except:
            print(f"Error: No se encuentra el fichero {args.read}.")
            exit()
    else:
        server_url = "https://www.mclibre.org/mclibre-python-testing/mclibre_python_testing_server.py"

        random_id = random.randint(0, 100_000)
        json_request = {
            "jsonrpc": "2.0",
            "method": "unit-test",
            "params": {"version": "0.1", "exercise-id": args.exercise_id},
            "id": random_id,
        }
        r = requests.post(server_url, data=json.dumps(json_request))
        values = r.json()

    if args.write is not None:
        try:
            with open(args.write, "w", encoding="utf-8") as file:
                file.write(json.dumps(values, ensure_ascii=False))
                print(
                    f"Los valores de prueba se han guardado en el fichero {file.name}"
                )
        except:
            print(f"Error: No se ha podido crear el fichero {args.write}.")
            exit()
    else:
        print()
        print(
            f"{colorama.Fore.YELLOW}-+-+-+-+-+-+-+-+- MCLIBRE PYTHON TESTING -+-+-+-+-+-+-+-+-{colorama.Style.RESET_ALL}"
        )
        print()
        print("-+-+-+-+-+-+-+-+-       BIENVENIDO       -+-+-+-+-+-+-+-+-")
        print()
        if "error" in values:
            print("Se ha detectado un error:")
            print(f"  Código de error:  {values['error']}")
            print(f"  Mensaje de error: {values['message']}")
        elif values["id"] != random_id:
            print("Se ha detectado un error:")
            print(
                "  La respuesta del servidor contiene un identificador de petición distinto al de la solicitud enviada."
            )
        else:
            if len(values["result"]) == 1:
                print(f"Se va a ejecutar {len(values['result'])} test.")
            else:
                print(f"Se van a ejecutar {len(values['result'])} tests.")
            print()
            print("Por favor, espere a que se ejecuten todos los tests.")
            print()
            print("Una vez ejecutados, se mostrará el resultado.")
            print()
            print("-+-+-+-+-+-+-+-+- EJECUCION DE LOS TESTS -+-+-+-+-+-+-+-+-")
            print()
            errorReport = []
            test_counter = 1
            for i in values["result"]:
                print(f"Ejecutando el test {test_counter}. Por favor, espere. ", end="")
                with open("test_values.txt", "w", encoding="utf-8") as file:
                    file.write(str(i))
                create_test_program(testable)
                with open("stdout.txt", "w") as file:
                    p = subprocess.Popen(
                        [
                            "pytest",
                            "test_program.py",
                            "--junitxml=result.txt",
                            "--quiet",
                        ],
                        stdout=file,
                    )
                    p.wait()
                failed_message = False
                too_many_inputs = False
                too_many_randoms = False

                with open("stdout.txt", "r") as file:
                    line = file.readline()
                    while line:
                        if line.rstrip().find("1 failed") != -1:
                            failed_message = True
                        if (
                            line.rstrip().find(">       return input_values.pop(0)")
                            != -1
                        ):
                            too_many_inputs = True
                        if line.rstrip().find(">   program.random.randrange") != -1:
                            too_many_randoms = True
                        if line.rstrip().find(">   program.randrange") != -1:
                            too_many_randoms = True
                        if line.rstrip().find(">   program.random.choice") != -1:
                            too_many_randoms = True
                        if line.rstrip().find(">   program.choice") != -1:
                            too_many_randoms = True
                        line = file.readline()

                if failed_message:
                    print(f"Test {test_counter} fallado. ")
                else:
                    print(f"Test {test_counter} superado. ")
                test_counter += 1

                import xml.etree.ElementTree as ET

                tree = ET.parse("result.txt")
                root = tree.getroot()
                for neighbor in root.iter("testsuite"):
                    if int(neighbor.attrib["errors"]) > 0:
                        errorReport += [[i, "", SYNTAX_ERROR]]
                    elif int(neighbor.attrib["failures"]) > 0:
                        try:
                            with open(
                                "obtained_result.txt", "r", encoding="utf-8"
                            ) as file:
                                # file is saved as json and is read as a list
                                texto = json.load(file)
                                # print(texto)
                            errorReport += [[i, texto, ""]]
                        except:
                            errorReport += [[i, "", EXECUTION_ERROR]]
                if os.path.isfile("obtained_result.txt"):
                    os.remove("obtained_result.txt")

                if os.path.isfile("test_values.txt"):
                    os.remove("test_values.txt")

                if os.path.isfile("result.txt"):
                    os.remove("result.txt")

                if os.path.isfile("test_program.py"):
                    os.remove("test_program.py")

                if os.path.isfile("stdout.txt"):
                    os.remove("stdout.txt")
            print()
            print("-+-+-+-+-+-+-+-+-       RESULTADOS       -+-+-+-+-+-+-+-+-")
            print()
            print(f"Programa probado: {testable}")
            print(f"Número MPTC:      {args.exercise_id}")
            print()
            if len(values["result"]) > 1:
                print(f"Se han ejecutado {len(values['result'])} tests.")
            else:
                print(f"Se ha ejecutado {len(values['result'])} test.")
            if errorReport == []:
                print()
                print(
                    f"{colorama.Fore.GREEN}Se han superado todos los tests. ¡Enhorabuena!{colorama.Style.RESET_ALL}"
                )
            else:
                if len(values["result"]) - len(errorReport) != 1:
                    print(
                        f"Se han superado {len(values['result']) - len(errorReport)} tests."
                    )
                else:
                    print(
                        f"Se ha superado {len(values['result']) - len(errorReport)} test."
                    )
                if len(errorReport) != 1:
                    print(f"Han fallado {len(errorReport)} tests.")
                else:
                    print(f"Ha fallado {len(errorReport)} test.")
                for i in errorReport:
                    print()
                    print("Test fallado:")
                    if "input" in i[0]:
                        if len(i[0]) > 0:
                            print("  Valores de entrada:   ", end="")
                            for j in i[0]["input"]:
                                if j == "":
                                    print("[Intro] ", end="")
                                else:
                                    print(f"{j} ", end="")
                            print()
                            print()
                    if "random" in i[0]:
                        if len(i[0]) > 0:
                            print("  Valores aleatorios:   ", end="")
                            for j in i[0]["random"]:
                                print(f"{j} ", end="")
                            print()
                            print()
                    if too_many_inputs:
                        print(
                            "  El programa pide al usuario más datos de los esperados."
                        )
                        print()
                    elif too_many_randoms:
                        print(
                            "  El programa parece generar más números aleatorios de los esperados."
                        )
                        print()
                    elif i[2] == SYNTAX_ERROR:
                        print(
                            "  El programa parece tener un error de sintaxis. Por favor, compruebe que puede ejecutarlo manualmente."
                        )
                        print()
                    elif i[2] == EXECUTION_ERROR:
                        print(
                            "  El programa no puede ejecutarse. Por favor, compruebe que contiene la función main()."
                        )
                        print()
                    else:
                        if len(i[0]["output"]) != len(i[1]):
                            print(
                                "  El programa genera un número incorrecto de cadenas de salida."
                            )
                            print()
                        for j in range(min(len(i[0]["output"]), len(i[1]))):
                            if i[0]["output"][j] != i[1][j]:
                                print(f'  Resultado esperado: "{i[0]["output"][j]}"')
                                print(f'  Resultado obtenido: "{i[1][j]}"')
                                print()
                        for j in range(
                            min(len(i[0]["output"]), len(i[1])),
                            max(len(i[0]["output"]), len(i[1])),
                        ):
                            if 0 <= j < len(i[0]["output"]):
                                print(f'  Resultado esperado: "{i[0]["output"][j]}"')
                            else:
                                print(f"  No se esperaba ningún resultado.")
                            if 0 <= j < len(i[1]):
                                print(f'  Resultado obtenido: "{i[1][j]}"')
                            else:
                                print(f"  No se obtuvo ningún resultado.")
                            print()
                if len(errorReport) > 1:
                    print(
                        f"{colorama.Fore.RED}{len(errorReport)} tests han fallado. Por favor, corrija el programa y pruebe de nuevo.{colorama.Style.RESET_ALL}"
                    )
                else:
                    print(
                        f"{colorama.Fore.RED}{len(errorReport)} test ha fallado. Por favor, corrija el programa y pruebe de nuevo.{colorama.Style.RESET_ALL}"
                    )

            print()


if __name__ == "__main__":
    main()
