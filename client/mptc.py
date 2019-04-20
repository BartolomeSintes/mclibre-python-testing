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
                output.append(string)

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
            output.append(partial_output)

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

    parser.add_argument(
        "-w", "--write", action="store", help="download and save test values in file"
    )

    parser.add_argument(
        "-r", "--read", action="store", help="read test values from file"
    )

    args = parser.parse_args()
    testable = args.to_be_tested_py
    if testable[0:2] == ".\\" or testable[0:2] == "./":
        testable = testable[2:]
    if testable.find("\\") != -1 or testable.find("/") != -1:
        print(f"Error: Relative or absolute paths [{testable}] are not allowed.")
        print("Please, execute MPTC from the directory where your program is located.")
        exit()
    elif not (os.path.isfile(testable)):
        print(
            f"Error: Program to be tested [{testable}] not found. Please, check file name"
        )
        exit()

    if args.read is not None:
        try:
            with open(args.read, "r", encoding="utf-8") as file:
                values = json.load(file)
                random_id = values["id"]
        except:
            print(f"Error: {args.read} file not found.")
            exit()
    else:
        server_url = "http://smagris3.uv.es/mclibre/mclibre-python-testing/mclibre_python_testing_server.py"
        # server_url = "http://localhost/mclibre/consultar/python-testing/server/mclibre_python_testing_server.py"

        random_id = random.randint(0, 100_000)
        json_request = {
            "jsonrpc": "2.0",
            "method": "unit-test",
            "params": {"version": "0.1", "exercise-id": args.exercise_id},
            "id": random_id,
        }
        # print (json.dumps(json_request))
        r = requests.post(server_url, data=json.dumps(json_request))
        # print(r.text)
        values = r.json()
        # print(values)
        # for i in values["result"]:
        #    print(i["input"])
        #    print(i["random"])
        #    print(i["output"])
        #    print()

    if args.write is not None:
        try:
            with open(args.write, "w", encoding="utf-8") as file:
                file.write(json.dumps(values, ensure_ascii=False))
                print(f"Test values have been saved as {file.name}")
        except:
            print(f"Error: {args.write} file could not be created.")
            exit()
    else:
        print("-+-+-+-+-+-+-+-+- MCLIBRE PYTHON TESTING -+-+-+-+-+-+-+-+-")
        print("-+-+-+-+-+-+-+-+-        WELCOME         -+-+-+-+-+-+-+-+-")
        print()
        if "error" in values:
            print("An error has been detected:")
            print(f"  Error number:  {values['error']}")
            print(f"  Error message: {values['message']}")
        elif values["id"] != random_id:
            print("An error has been detected:")
            print(
                "  The id sent by the server is not the same that was sent to the server."
            )
        else:
            if len(values["result"]) == 1:
                print(f"{len(values['result'])} test will be executed.")
            else:
                print(f"{len(values['result'])} tests will be executed.")
            print()
            print("Please, wait until all tests have been executed.")
            print()
            print("A final report will be shown after.")
            print()
            print("-+-+-+-+-+-+-+-+-     TESTS EXECUTION    -+-+-+-+-+-+-+-+-")
            print()
            errorReport = []
            test_counter = 1
            for i in values["result"]:
                print(f"Running test {test_counter}. Please wait. ")
                with open("test_values.txt", "w", encoding="utf-8") as file:
                    file.write(str(i))
                create_test_program(testable)
                with open('stdout.txt', 'w') as file:
                    p = subprocess.Popen(
                        ["pytest", "test_program.py", "--junitxml=result.txt", "--quiet"],
                        stdout=file,
                    )
                    p.wait()
                failed_message = False
                with open('stdout.txt', 'r') as file:
                    line = file.readline()
                    while line:
                        if line.rstrip().find("1 passed in") != -1:
                            failed_message = True
                        line = file.readline()
                if failed_message:
                    print(f"Test {test_counter} passed. ", end="")
                else:
                    print(f"Test {test_counter} failed. ", end="")
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
            print()
            print("-+-+-+-+-+-+-+-+- MCLIBRE PYTHON TESTING -+-+-+-+-+-+-+-+-")
            print("-+-+-+-+-+-+-+-+-         RESULTS        -+-+-+-+-+-+-+-+-")
            print()
            print(f"Tested program: {testable}")
            print(f"MPTC number:    {args.exercise_id}")
            print()
            if len(values["result"]) > 1:
                print(f"{len(values['result'])} tests have been executed.")
            else:
                print(f"{len(values['result'])} test has been executed.")
            if errorReport == []:
                print()
                print("All tests have been passed. Congratulations!")
            else:
                if len(values["result"]) - len(errorReport) > 1:
                    print(
                        f"{len(values['result']) - len(errorReport)} tests have been passed."
                    )
                else:
                    print(
                        f"{len(values['result']) - len(errorReport)} test has been passed."
                    )
                if len(errorReport) > 1:
                    print(f"{len(errorReport)} tests have been failed.")
                else:
                    print(f"{len(errorReport)} test has been failed.")
                for i in errorReport:
                    print()
                    print("Failed test:")
                    if "input" in i[0]:
                        if len(i[0]) > 0:
                            print("  Input values:   ", end="")
                            for j in i[0]["input"]:
                                if j == "":
                                    print("[Intro] ", end="")
                                else:
                                    print(f"{j} ", end="")
                            print()
                    if "random" in i[0]:
                        if len(i[0]) > 0:
                            print("  Random values:   ", end="")
                            for j in i[0]["random"]:
                                print(f"{j} ", end="")
                            print()

                    if i[2] == SYNTAX_ERROR:
                        print(
                            "  Your program could not be executed properly. Please, check syntax manually."
                        )
                    elif i[2] == EXECUTION_ERROR:
                        print(
                            "  Your program could not be executed properly. Please, check manually."
                        )
                    else:
                        if len(i[0]["output"]) != len(i[1]):
                            print(
                                "  The program produces an incorrect number of outputs."
                            )
                        for j in range(min(len(i[0]["output"]), len(i[1]))):
                            if i[0]["output"][j] != i[1][j]:
                                print(f'  Expected result: "{i[0]["output"][j]}"')
                                print(f'  Obtained result: "{i[1][j]}"')
                        for j in range(
                            min(len(i[0]["output"]), len(i[1])),
                            max(len(i[0]["output"]), len(i[1])),
                        ):
                            print()
                            if 0 <= j < len(i[0]["output"]):
                                print(f'  Expected result: "{i[0]["output"][j]}"')
                            else:
                                print(f"  No result was expected.")
                            if 0 <= j < len(i[1]):
                                print(f'  Obtained result: "{i[1][j]}"')
                            else:
                                print(f"  No result was obtained.")
            print()


if __name__ == "__main__":
    main()
