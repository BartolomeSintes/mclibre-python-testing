import random


def add_test(input, output, comma):
    print("    {")
    print('       "input" : [', end="")
    for i in range(len(input) - 1):
        print(input[i], end="")
        print(", ", end="")
    print(input[-1], end="")
    print("],")
    print('       "output" : [', end="")
    for i in range(len(output) - 1):
        print('"' + output[i] + '", ', end="")
    print('"' + output[-1] + '"', end="")
    print("]")
    if comma:
        print("    },")
    else:
        print("    }")


def exercise_1():
    fecha = 4 * random.randrange(400, 600) + 1
    add_test(
        [fecha],
        [
            "COMPROBADOR DE AÑOS BISIESTOS",
            "Escriba un año y le diré si es bisiesto: ",
            "El año " + str(fecha) + " no es un año bisiesto.",
        ],
        True,
    )

    fecha = 4 * random.randrange(400, 600) + 2
    add_test(
        [fecha],
        [
            "COMPROBADOR DE AÑOS BISIESTOS",
            "Escriba un año y le diré si es bisiesto: ",
            "El año " + str(fecha) + " no es un año bisiesto.",
        ],
        True,
    )

    fecha = 4 * random.randrange(400, 600) + 3
    add_test(
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
    add_test(
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
    add_test(
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
    add_test(
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
