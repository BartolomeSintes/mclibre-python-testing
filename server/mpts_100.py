import random

NOT_LAST_TEST = True
LAST_TEST = False


def add_test(input, output, comma):
    print("    {")
    print('       "input" : [', end="")
    if len(input) == 1:
        print(input[0], end="")
    elif len(input) > 1:
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


def exercise(exercise_id):
    if exercise_id == 1000:
        # Exercise 1000 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-variables.html

        # Comprueba salida
        add_test(
            [],
            [
                "¡Hola, mundo!",
            ],
            LAST_TEST,
        )
        # Exercise 1000 END

    elif exercise_id == 1001:
        # Exercise 1000 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-variables.html

        # Comprueba salida
        add_test(
            [],
            [
                "SALUDANDO",
                "¡Hola, mundo!",
                "¡Adios, amigo!",
            ],
            LAST_TEST,
        )

        # Exercise 1000 END

    elif exercise_id == 1002:
        # Exercise 1001 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-variables.html

        # número pequeño
        numero = random.randrange(0, 10)

        add_test(
            [numero],
            [
                "ESCRIBA NÚMERO",
                "Escriba un número entero: ",
                f"Ha escrito el número {numero}",
            ],
            NOT_LAST_TEST,
        )
        # número negativo
        numero = random.randrange(-100, 0)

        add_test(
            [numero],
            [
                "ESCRIBA NÚMERO",
                "Escriba un número entero: ",
                f"Ha escrito el número {numero}",
            ],
            LAST_TEST,
        )

    elif exercise_id == 1003:
        # Exercise 1003 BEGINNING
        # http://www.mclibre.org/consultar/python/ejercicios/ej-variables.html

        # número pequeño
        a = random.randrange(0, 100) / 10
        b = random.randrange(0, 100) / 10
        c = a + b

        add_test(
            [a, b],
            [
                "SUMA NÚMEROS",
                "Escriba un número: ",
                "Escriba otro número: ",
                f"{a} + {b} = {c}",
            ],
            LAST_TEST,
        )