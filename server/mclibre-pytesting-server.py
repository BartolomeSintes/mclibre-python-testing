#!/usr/bin/python3
# -*- coding: utf-8 -*-
# enable debugging
import cgi
import cgitb
import random
import sys
import os
import json

cgitb.enable()


def imprime_principio():
    print("{")
    print('  "jsonrpc": "2.0",')
    print('  "result": [')


def imprime_caso(entrada, salida, coma):
    print("    {")
    print('       "input" : [', end="")
    for i in range(len(entrada) - 1):
        print(entrada[i], end="")
        print(", ", end="")
    print(entrada[-1], end="")
    print("],")
    print('       "output" : [', end="")
    for i in range(len(salida) - 1):
        print('"' + salida[i] + '", ', end="")
    print('"' + salida[-1] + '"', end="")
    print("]")
    if coma:
        print("    },")
    else:
        print("    }")


def imprime_final(id):
    print(" ],")
    print(f' "id": {id}')
    print("}")


def generate_json(id):
    print("Content-Type: 'application/json; charset=utf-8'\n")
    print()
    imprime_principio()

    fecha = 4 * random.randrange(400, 600) + 1
    imprime_caso(
        [fecha],
        [
            "COMPROBADOR DE AÑOS BISIESTOS",
            "Escriba un año y le diré si es bisiesto: ",
            "El año " + str(fecha) + " no es un año bisiesto.",
        ],
        True,
    )

    fecha = 4 * random.randrange(400, 600) + 2
    imprime_caso(
        [fecha],
        [
            "COMPROBADOR DE AÑOS BISIESTOS",
            "Escriba un año y le diré si es bisiesto: ",
            "El año " + str(fecha) + " no es un año bisiesto.",
        ],
        True,
    )

    fecha = 4 * random.randrange(400, 600) + 3
    imprime_caso(
        [fecha],
        [
            "COMPROBADOR DE AÑOS BISIESTOS",
            "Escriba un año y le diré si es bisiesto: ",
            "El año " + str(fecha) + " no es un año bisiesto.",
        ],
        True,
    )

    # Múltiplo de 400: No es bisisesto
    fecha = 400 * random.randrange(1, 7)
    imprime_caso(
        [fecha],
        [
            "COMPROBADOR DE AÑOS BISIESTOS",
            "Escriba un año y le diré si es bisiesto: ",
            "El año " + str(fecha) + " es un año bisiesto porque es múltiplo de 400.",
        ],
        True,
    )

    # Múltiplo de 100 que no es múltiplo de 400: Es bisisesto
    fecha = 400 * random.randrange(1, 5) + 100 * random.randrange(1, 4)
    imprime_caso(
        [fecha],
        [
            "COMPROBADOR DE AÑOS BISIESTOS",
            "Escriba un año y le diré si es bisiesto: ",
            "El año "
            + str(fecha)
            + " no es un año bisiesto porque es múltiplo de 100 sin ser múltiplo de 400.",
        ],
        True,
    )

    # Múltiplo de 4 que no es múltiplo de 100: Es bisiesto
    fecha = 100 * random.randrange(10, 25) + 4 * random.randrange(1, 20)
    imprime_caso(
        [fecha],
        [
            "COMPROBADOR DE AÑOS BISIESTOS",
            "Escriba un año y le diré si es bisiesto: ",
            "El año "
            + str(fecha)
            + " es un año bisiesto porque es múltiplo de 4 sin ser múltiplo de 100.",
        ],
        False,
    )

    imprime_final(id)


def generate_json_error(error_code, id):
    print("Content-Type: 'application/json; charset=utf-8'\n")
    print()
    print("{")
    print('  "jsonrpc": "2.0", ')
    print(f'  "error": {error_code}', end="")
    if error_code == 1:
        print(',  "message": "missing json-rpc field" ')
    elif error_code == 2:
        print(',  "message": "wrong json-rpc value" ')
    elif error_code == 3:
        print(',  "message": "missing method field" ')
    elif error_code == 4:
        print(',  "message": "wrong method value" ')
    elif error_code == 5:
        print(',  "message": "missing params field" ')
    elif error_code == 6:
        print(',  "message": "missing params - version field" ')
    elif error_code == 7:
        print(',  "message": "wrong params - version value" ')
    elif error_code == 8:
        print(',  "message": "missing params - exercise-id field" ')
    elif error_code == 9:
        print(',  "message": "wrong params - exercise-id value" ')
    elif error_code == 10:
        print(',  "message": "missing id field" ')
    print()
    print(f', "id": {id}')
    print("}")


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
    elif form["params"]["exercise-id"] != 1:
        request_ok = 9
    elif "id" not in form:
        request_ok = 10
    return request_ok


def main():
    #form = cgi.FieldStorage()
    #print(form)
    #print("Datos en server:")
    data = json.loads(sys.stdin.read(int(os.environ.get('CONTENT_LENGTH', 0))))
    #print(json.loads(data))
    #print(data)
    #print(data["params"]["version"])
    #print("Datos en server:")
    error_code = check_request(data)
    if error_code == 0:
        generate_json(data["id"])
    else:
        generate_json_error(error_code, data["id"])


if __name__ == "__main__":
    main()
