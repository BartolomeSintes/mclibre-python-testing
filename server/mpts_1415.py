import mpts_common
import datetime
import math
import random

NOT_LAST_TEST = True
LAST_TEST = False


def exercise(exercise_id):

    if exercise_id == 141511:
        # Exercise 141511 BEGINNING
        # /examenes/14-15/examen-150520.html

        # Valor negativo
        cm = -random.randrange(1, 11)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CENTÍMETROS A KENS Y SHAKUS",
                    "Escriba la cantidad de centímetros: ",
                    "Por favor, escriba un número positivo.",
                ],
            ],
        )

        # Valor positivo
        # si calculaba cm a partir de sh y k al azar no coincidía
        # pero no tengo claro si sacando cm al azar coincidría siempre
        sh = random.randrange(0, 59999) / 10000
        k = 10 * random.randrange(0, 10)
        shs = sh + k * 6
        cm = round(shs * 30.3)
        shs = round(cm / 30.3, 2)
        k = round(shs // 6)
        sh = round(shs - k * 6, 2)

        mpts_common.add_test(
            LAST_TEST,
            ["input", [cm]],
            [
                "output",
                [
                    "CONVERTIDOR DE CENTÍMETROS A KENS Y SHAKUS",
                    "Escriba la cantidad de centímetros: ",
                    f"{cm} cm son {shs} shakus, es decir {k} ken(s) y {sh} shaku(s).",
                ],
            ],
        )

        # Exercise 141511 END

    elif exercise_id == 141521:
        # Exercise 141521 BEGINNING
        # /examenes/14-15/examen-150525.html

        # primero mayor que el segundo
        a = random.randrange(-10000, 10000)
        b = random.randrange(-20000, a)
        a = a / 100
        b = b / 100

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "DISTANCIA",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    f"La distancia entre {a} y {b} es {a - b}",
                ],
            ],
        )

        # segundo mayor que el primero
        a = random.randrange(-10000, 10000)
        b = random.randrange(a + 1, 20000)
        a = a / 100
        b = b / 100

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "DISTANCIA",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    f"La distancia entre {a} y {b} es {b - a}",
                ],
            ],
        )

        # iguales
        a = random.randrange(-10000, 10000)
        a = a / 100
        b = a

        mpts_common.add_test(
            LAST_TEST,
            ["input", [a, b]],
            [
                "output",
                [
                    "DISTANCIA",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    f"La distancia entre {a} y {b} es 0.0",
                ],
            ],
        )

        # Exercise 141521 END

    elif exercise_id == 141522:
        # Exercise 141522 BEGINNING
        # /examenes/14-15/examen-150525.html

        # c < a < b
        c = random.randrange(-1000, 1000)
        a = random.randrange(c + 1, 2000)
        b = random.randrange(a + 1, 3000)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "MÁS CERCA, MÁS LEJOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    f"{c} está más cerca de {a} que de {b}",
                ],
            ],
        )

        # a < c < (a+b)/2 < b
        a = random.randrange(-1000, 1000)
        b = random.randrange(a + 10, 2000)
        c = random.randrange(a + 1, math.ceil((a + b) / 2))

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "MÁS CERCA, MÁS LEJOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    f"{c} está más cerca de {a} que de {b}",
                ],
            ],
        )

        # a < (a+b)/2 < b
        a = random.randrange(-1000, 1000, 2)
        b = random.randrange(a + 10, 2000, 2)
        c = round((a + b) / 2)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "MÁS CERCA, MÁS LEJOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    f"{c} está a la misma distancia de {a} que de {b}",
                ],
            ],
        )

        # a < c < (a+b)/2 < b
        a = random.randrange(-1000, 1000)
        b = random.randrange(a + 10, 2000)
        c = random.randrange(math.ceil((a + b) / 2) + 1, b)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "MÁS CERCA, MÁS LEJOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    f"{c} está más cerca de {b} que de {a}",
                ],
            ],
        )

        # a < b < c
        a = random.randrange(-1000, 1000)
        b = random.randrange(a + 100, 2000)
        c = random.randrange(b + 1, 3000)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "MÁS CERCA, MÁS LEJOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    f"{c} está más cerca de {b} que de {a}",
                ],
            ],
        )

        # c < b < a
        c = random.randrange(-1000, 1000)
        b = random.randrange(c + 1, 2000)
        a = random.randrange(b + 1, 3000)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "MÁS CERCA, MÁS LEJOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    f"{c} está más cerca de {b} que de {a}",
                ],
            ],
        )

        # b < c < (a+b)/2 < a
        b = random.randrange(-1000, 1000)
        a = random.randrange(b + 10, 2000)
        c = random.randrange(b + 1, math.ceil((a + b) / 2))

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "MÁS CERCA, MÁS LEJOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    f"{c} está más cerca de {b} que de {a}",
                ],
            ],
        )

        # b < (a+b)/2 < a
        b = random.randrange(-1000, 1000, 2)
        a = random.randrange(b + 10, 2000, 2)
        c = round((a + b) / 2)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "MÁS CERCA, MÁS LEJOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    f"{c} está a la misma distancia de {a} que de {b}",
                ],
            ],
        )

        # b < c < (a+b)/2 < a
        b = random.randrange(-1000, 1000)
        a = random.randrange(b + 10, 2000)
        c = random.randrange(math.ceil((a + b) / 2) + 1, a)

        mpts_common.add_test(
            NOT_LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "MÁS CERCA, MÁS LEJOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    f"{c} está más cerca de {a} que de {b}",
                ],
            ],
        )

        # b < a < c
        b = random.randrange(-1000, 1000)
        a = random.randrange(b + 100, 2000)
        c = random.randrange(a + 1, 3000)

        mpts_common.add_test(
            LAST_TEST,
            ["input", [a, b, c]],
            [
                "output",
                [
                    "MÁS CERCA, MÁS LEJOS",
                    "Escriba un número: ",
                    "Escriba otro número: ",
                    "Escriba otro número más: ",
                    f"{c} está más cerca de {a} que de {b}",
                ],
            ],
        )
        # Exercise 141522 END
