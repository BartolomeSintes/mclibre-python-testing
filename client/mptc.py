import argparse
import json
import os
import random
import subprocess
import sys

# pytest is a required module
try:
    exec("import pytest")
except:
    print("[ERROR] Missing module: PyTest")
    print("Please install PyTest and try again")
    exit()

# requests is a required module
try:
    import requests
except:
    print("[ERROR] Missing module: Requests")
    print("Please install Requests and try again")
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

program_file = str("{program_to_be_tested}").replace(".py", "")

program = importlib.import_module(program_file)

with open("test_values.txt", "r", encoding="utf-8") as file:
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
        program.print = lambda s: output.append(s)

        program.main()

        with open("obtained_result.txt", "w", encoding="utf-8") as file:
            # saved as json because it is a list
            json.dump(output, file, ensure_ascii=False)

        assert output == values["output"]
"""
        )


def main():
    parser = argparse.ArgumentParser(
        description="Testing tool for some of the programming exercises in mclibre.org's Python course available at http://www.mclibre.org/consultar/python/"
    )

    parser.add_argument(
        "to_be_tested_py",
        action="store",
        help="File name of the python program that will be tested",
    )

    parser.add_argument(
        "exercise_id",
        action="store",
        type=int,
        help="id of the tests that will be applied to the program",
    )

    args = parser.parse_args()
    # testable = args.to_be_tested_py

    if not (os.path.isfile(args.to_be_tested_py)):
        print(
            f"Error: Program to be tested [{args.to_be_tested_py}] not found. Please, check file name"
        )
        exit()

    server_url = "http://smagris3.uv.es/mclibre/mclibre-python-testing/mclibre_python_testing_server.py"
    # server_url = "http://localhost/mclibre/consultar/python-testing/server/mclibre_python_testing_server.py"

    random_id = random.randint(0, 100_000)
    json_request = {
        "jsonrpc": "2.0",
        "method": "unit-test",
        "params": {"version": "0.1", "exercise-id": args.exercise_id},
        "id": random_id
    }
    #print (json.dumps(json_request))
    r = requests.get(server_url, data=json.dumps(json_request))
    #print(r)
    values = r.json()
    #print(values)

    print("-+-+-+-+-+-+-+-+-+-+ MCLIBRE PYTHON TESTING -+-+-+-+-+-+-+-+-+-+")
    print("-+-+-+-+-+-+-+-+-+-+        WELCOME         -+-+-+-+-+-+-+-+-+-+")
    if "error" in values:
        print()
        print("An error has been detected:")
        print(f"  Error number:  {values['error']}")
        print(f"  Error message: {values['message']}")
    elif values["id"] != random_id:
        print()
        print("An error has been detected:")
        print("  The id sent by the server is not the same that was sent to the server")
    else:

        print(f"{len(values['result'])} tests will be executed")
        print("Please, wait until all tests have been executed")
        print("PyTest will print some messages while the tests are being executed")
        print("and a final report will be shown after")
        print("-+-+-+-+-+-+-+-+-+-+        PYTEST         -+-+-+-+-+-+-+-+-+-+")
        errorReport = []
        for i in values["result"]:
            with open("test_values.txt", "w", encoding="utf-8") as file:
                file.write(str(i))
            create_test_program(args.to_be_tested_py)

            p = subprocess.Popen(
                ["pytest", "test_program.py", "--junitxml=result.txt", "--quiet"]
            )
            p.wait()

            import xml.etree.ElementTree as ET

            tree = ET.parse("result.txt")
            root = tree.getroot()
            for neighbor in root.iter("testsuite"):
                if int(neighbor.attrib["failures"]) > 0:
                    with open("obtained_result.txt", "r", encoding="utf-8") as file:
                        # file is saved as json and is read as a list
                        texto = json.load(file)
                        print(texto)
                    errorReport += [[i["input"], i["output"], texto]]
            if os.path.isfile("obtained_result.txt"):
                os.remove("obtained_result.txt")

            if os.path.isfile("test_values.txt"):
                os.remove("test_values.txt")

            if os.path.isfile("result.txt"):
                os.remove("result.txt")

            if os.path.isfile("test_program.py"):
                os.remove("test_program.py")

        print()
        print()
        print("-+-+-+-+-+-+-+-+-+-+ MCLIBRE PYTHON TESTING -+-+-+-+-+-+-+-+-+-+")
        print("-+-+-+-+-+-+-+-+-+-+        RESULTS         -+-+-+-+-+-+-+-+-+-+")
        print()
        if len(values["result"]) > 1:
            print(f"{len(values['result'])} tests have been executed")
        else:
            print(f"{len(values['result'])} test has been executed")
        if errorReport == []:
            print()
            print("All test have passed")
        else:
            if len(values["result"]) - len(errorReport) > 1:
                print(f"{len(values['result']) - len(errorReport)} tests have passed")
            else:
                print(f"{len(values['result']) - len(errorReport)} test has passed")
            if len(errorReport) > 1:
                print(f"{len(errorReport)} tests have failed")
            else:
                print(f"{len(errorReport)} test has failed")
            for i in errorReport:
                print()
                print("Failed test:")
                if len(i[0]) > 0:
                    print("  Tested values:", i[0][0])
                else:
                    print("  Tested values: None")
                if len(i[1]) != len(i[2]):
                    print("  The program produces an incorrect number of outputs")
                for j in range(min(len(i[1]), len(i[2]))):
                    if i[1][j] != i[2][j]:
                        print(f'  Expected result: "{i[1][j]}"')
                        print(f'  Obtained result: "{i[2][j]}"')
                for j in range(min(len(i[1]), len(i[2])), max(len(i[1]), len(i[2]))):
                    if 0 <= j < len(i[1]):
                        print(f'  Expected result: "{i[1][j]}"')
                    else:
                        print(f"  No result was expected")
                    if 0 <= j < len(i[2]):
                        print(f'  Obtained result: "{i[2][j]}"')
                    else:
                        print(f"  No result obtained")


if __name__ == "__main__":
    main()
