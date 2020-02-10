#!/usr/bin/python3
# enable debugging
import cgi
import cgitb
import importlib
import io
import json
import os
import random
import sys
from mpts_ids import valid_exercise_ids

cgitb.enable()
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding="utf-8")


def valid_exercise_number(num):
    valid = False
    for i in valid_exercise_ids:
        if num in i[1]:
            valid = True
    return valid


def exercise_module_number(num):
    module = 0
    for i in valid_exercise_ids:
        if num in i[1]:
            module = i[0]
    return module


def generate_json(exercise_id):
    mpts_number = exercise_module_number(exercise_id)
    mpts = importlib.import_module("mpts_" + str(mpts_number))
    print('  "result": [')
    mpts.exercise(exercise_id)
    print(" ],")


def generate_json_error(error_code):
    print(f'  "error": {error_code}, ', end="")
    if error_code == 1:
        print('"message": "missing json-rpc field", ')
    elif error_code == 2:
        print('"message": "wrong json-rpc value", ')
    elif error_code == 3:
        print('"message": "missing method field", ')
    elif error_code == 4:
        print('"message": "wrong method value", ')
    elif error_code == 5:
        print('"message": "missing params field", ')
    elif error_code == 6:
        print('"message": "missing params - version field", ')
    elif error_code == 7:
        print('"message": "wrong params - version value", ')
    elif error_code == 8:
        print('"message": "missing params - exercise-id field", ')
    elif error_code == 9:
        print('"message": "wrong params - exercise-id value", ')
    elif error_code == 10:
        print('"message": "missing id field", ')


def check_request(form):
    request_ok = 0
    if "jsonrpc" not in form:
        request_ok = 1
    elif form["jsonrpc"] != "2.0":
        request_ok = 2
    elif "method" not in form:
        request_ok = 3
    elif form["method"] != "unit-test":
        request_ok = 4
    elif "params" not in form:
        request_ok = 5
    elif "version" not in form["params"]:
        request_ok = 6
    elif form["params"]["version"] != "0.1":
        request_ok = 7
    elif "exercise-id" not in form["params"]:
        request_ok = 8
    elif not (valid_exercise_number(form["params"]["exercise-id"])):
        request_ok = 9
    elif "id" not in form:
        request_ok = 10
    return request_ok


def main():
    data = json.loads(sys.stdin.read(int(os.environ.get("CONTENT_LENGTH", 0))))
    # print(json.loads(data))
    # print(data)
    # print(data["params"]["version"])
    # print("Datos en server:")
    print("Content-Type: application/json\r\n\r\n")
    print("{")
    print('  "jsonrpc": "2.0", ')
    error_code = check_request(data)
    if error_code == 0:
        generate_json(data["params"]["exercise-id"])
    else:
        generate_json_error(error_code)
    print(f'   "id": {data["id"]}')
    print("}")


if __name__ == "__main__":
    main()
